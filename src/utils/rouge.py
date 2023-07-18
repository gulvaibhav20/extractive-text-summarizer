from rouge_score import rouge_scorer
from prettytable import PrettyTable

def read_files(human_generated_summary_path, auto_generated_summary_path):
    with open(human_generated_summary_path, encoding="utf8") as f:
        human_generated_summary = "\n".join(f.readlines())

    with open(auto_generated_summary_path, encoding="utf8") as f:
        auto_generated_summary = "\n".join(f.readlines())

    return human_generated_summary, auto_generated_summary


def calculate_rouge(human_generated_summary_path, auto_generated_summary_path):
    # Reading the input files
    human_generated_summary, auto_generated_summary = read_files(human_generated_summary_path, auto_generated_summary_path)

    # Generating the Rouge scores
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(human_generated_summary, auto_generated_summary)

    print("\n\nROUGE SCORES:")
    table = PrettyTable(['Rouge-Score Method', 'Precision', 'Recall', 'F-Score'])
    table.add_row(["Rouge-1", round(scores.get("rouge1").precision, 4), round(scores.get("rouge1").recall, 4), round(scores.get("rouge1").fmeasure, 4)])
    table.add_row(["Rouge-2", round(scores.get("rouge2").precision, 4), round(scores.get("rouge2").recall, 4), round(scores.get("rouge2").fmeasure, 4)])
    table.add_row(["Rouge-L", round(scores.get("rougeL").precision, 4), round(scores.get("rougeL").recall, 4), round(scores.get("rougeL").fmeasure, 4)])
    print(table)
    
    return True
