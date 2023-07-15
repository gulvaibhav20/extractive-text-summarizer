import re
import numpy as np
import pandas as pd
from utils import constant

from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import networkx as nx
from gensim import corpora
from rank_bm25 import BM25Plus

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from math import log
from pylcs import lcs


def get_wordnet_pos(word):
    # Map POS tag to first character lemmatize() accepts
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def similarity_original(text_data):
    sim = np.zeros([len(text_data), len(text_data)]) # Initialization
    for i, sentence_1 in enumerate(text_data):
        for j, sentence_2 in enumerate(text_data):
            sent_1 = set(sentence_1) # Unique words
            sent_2 = set(sentence_2)
            if(i == j):
                sim[i][j] = 0
            else:
                common = float(len(list(sent_1 & sent_2)))
                if(len(sentence_1) and len(sentence_2) > 1):
                    denominator = float(log(len(sentence_1)) + log(len(sentence_2)))
                else:
                    denominator = 1.0
                
                sim[i][j] = common / denominator
    return sim


def similarity_tf_idf(text_data):
    sentence_data = []
    for sentence in text_data:
        sent = " ".join(sentence)
        sentence_data.append(sent)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sentence_data)
    feature_names = vectorizer.get_feature_names_out()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist,columns = feature_names)
    arr = df.to_numpy()
    column_value = df.shape[1]
    sim = np.zeros([len(text_data), len(text_data)])

    for A in range(df.shape[0]):
        for B in range(df.shape[0]):
            sim[A][B] = cosine_similarity(arr[A].reshape(1,column_value),arr[B].reshape(1,column_value))[0,0]
    
    return sim


def similarity_lcs(text_data):
    sentence_data = []
    for sentence in text_data:
        sent = " ".join(sentence)
        sentence_data.append(sent)

    sim = np.zeros([len(text_data), len(text_data)])
    for i, sentence_1 in enumerate(sentence_data):
        for j, sentence_2 in enumerate(sentence_data):
            if(i == j):
                sim[i][j] = 0
            else:
                sim[i][j] = lcs(sentence_1, sentence_2)
    return sim


def similarity_bm(text_data):
    
    dictionary = corpora.Dictionary(text_data) # BAG_OF_WORDS MODEL
    corpus = [dictionary.doc2bow(text) for text in text_data]
    bm25_obj = BM25Plus(corpus)

    similarity = []

    for i, sentence in enumerate(text_data):
        query = dictionary.doc2bow(sentence)
        score = bm25_obj.get_scores(query)
        similarity.append(score)
    
    sim = np.array(similarity)    
    return sim


def generate_similarity_matrix(text, algorithm = constant.PROPOSED_ALGORITHM):
    if(algorithm == constant.PROPOSED_ALGORITHM):
        first_matrix = similarity_original(text)
        second_matrix = similarity_bm(text)

        # Normalization
        first_matrix = first_matrix / first_matrix.max()
        second_matrix = second_matrix / second_matrix.max()
        
        return (first_matrix + second_matrix)
    
    elif(algorithm == constant.TF_IDF_COSINE_ALGORITHM):
        matrix = similarity_tf_idf(text)
        return matrix / matrix.max()

    elif(algorithm == constant.TEXT_RANK_ALGORITHM):
        matrix = similarity_original(text)
        return matrix / matrix.max()
    
    elif(algorithm == constant.BM_ALGORITHM):
        matrix = similarity_bm(text)
        return matrix / matrix.max()
    
    elif(algorithm == constant.LCS_ALGORITHM):
        matrix = similarity_lcs(text)
        return matrix / matrix.max()

    else:
        print("ERROR : WRONG INPUT FOR ALGORITHM ATTRIBUTE")
        return -1


def summarize (text, algorithm = constant.PROPOSED_ALGORITHM, iterations = constant.MAX_ITERATIONS, ratio = constant.SUMM_RATIO):
    # Tokenization
    sentences = sent_tokenize(text)
    sentences_clean = [re.sub(r'[^\w\s]','',sentence.lower()) for sentence in sentences]

    # Stop words removal
    stop_words = stopwords.words('english')
    sentence_tokens = [[words for words in sentence.split(' ') if words not in stop_words] for sentence in sentences_clean]

    # POS Tagging and Lemmatization
    text_data = []
    lemmatizer = WordNetLemmatizer()
    for sentence in sentence_tokens:
        word_list = [word for word in sentence if word]
        tags = pos_tag(word_list)
        text_line = []
        for word, tag in tags:
            text_line.append(lemmatizer.lemmatize(word, pos = get_wordnet_pos(tag)))
        text_data.append(text_line)

    # Similarity Matrix
    similarity_matrix = generate_similarity_matrix(text_data, algorithm)
    
    # Page Rank
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph, max_iter = iterations)

    # Best sentences
    top_sentence = {sentence:scores[index] for index,sentence in enumerate(sentences)}
    number = int(len(sentence_tokens)*(ratio))
    top = dict(sorted(top_sentence.items(), key=lambda x: x[1], reverse=True)[:number])
    text_list = []
    for sent in sentences:
        if sent in top.keys():
            text_list.append(sent)

    summary = "\n".join(text_list)
    return summary
