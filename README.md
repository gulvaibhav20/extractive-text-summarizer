<a name="readme-top"></a>

[![Python][Python.com]][Python-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="assets/logo.png" alt="Logo" width="120" height="120">
  </a>
  <h3 align="center"><strong> Extractive Text Summarizer </strong></h3>
  <p align="center">
    Using Integrated TextRank and BM25+ algorithm
    <br />
    <a href="https://www.mdpi.com/2063824"><strong>Explore the research publication »</strong></a>
    <br />
    <br />
  </p>
</div>


<!-- OVERVIEW -->
## Overview

![Extractive Text Summarizer Output][product-screenshot]

This repository contains the Python implementation of my research publication titled <strong>"Extractive Article Summarization Using Integrated TextRank and BM25+ Algorithm"</strong>. The project aims to provide a practical implementation of the extractive text summarization technique proposed in the research publication.
<br />
<br />

<strong>Features:</strong>
* Covers the implementation of the multiple similarity matrix variations in the TextRank's extractive text summarization algorithm. The variations include:
  * Integrated TextRank and BM25+ Algorithm **(Proposed model)**
  * Original TextRank Algorithm
  * BM25+ similarity-based TextRank Algorithm
  * TF-IDF-Cosine similarity-based TextRank Algorithm
  * LCS similarity-based TextRank Algorithm
* Configurable summarization parameters for controlling the length and quality of the generated summaries.
* Support for processing various types of text documents, such as articles, blog posts, research papers, and more.
* Support for **Rouge score evaluation**
<br />
<br />

<strong>Summarization Process:</strong><center>

![Summarization Process Flowchart][summarization-process]
</center>
The summarization process consists of three main phases where the first phase starts by retrieving textual data from the article source, followed by the preprocessing of the textual data. Preprocessing includes stopword removal, tokenization, POS tagging, and lemmatization. In the next phase, the similarity between each sentence pair of the article has been calculated then the article is modeled as a graph using the similarity matrix. Finally, in the last phase, a modified TextRank algorithm has been applied and the article summary is generated.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- BUILT WITH -->
## Built With

The project is primarily built using the **Python** programming language with the help of the following libraries:

* [NLTK - Natural Language Toolkit](https://www.nltk.org/)
* [Networkx - Network Analysis in Python](https://networkx.org/)
* [Gensim](https://radimrehurek.com/gensim/)
* [Scikit-Learn](https://scikit-learn.org/)
* [Numpy - Numerical Python](https://numpy.org/)
* [Pandas - Python Data Analysis Library](https://pandas.pydata.org/)
* [Rank-BM25](https://pypi.org/project/rank-bm25/)
* [Rouge-Score](https://pypi.org/project/rouge-score/)
* [Prettytable](https://pypi.org/project/prettytable/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To start using the project, you first have to setup your local machine to meet the system prerequisites. For this, just follow the below steps:

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/gulvaibhav20/extractive-text-summarizer.git
    ```
2. Navigate to the source code directory **(src)** inside the project repository:
    ```sh
    cd extractive-text-summarizer/src
    ```
3. Install the required Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Use the `src/main.py` to start using the extractive text summarizer.

<br />

> **NOTE:** Head over to the [main source code repository][config-readme] to understand the configurations and input/output settings for the summarizer.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE -->
## Usage

1. Prepare the text document / article URL you want to summarize. (*Note:* The document should be in plain text format i.e. in **(.txt)** format)
2. Modify the summarization parameters in the **src/config.ini** file based on your personal preference.
3. Run the summarization script:
    ```sh
    python src/main.py
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CITATION -->
## Citation

If you use this implementation in your research or publication, please cite the original research paper:

- <strong> [MLA] : </strong> Gulati, Vaibhav, et al. "Extractive Article Summarization Using Integrated TextRank and BM25+ Algorithm." Electronics 12.2 (2023): 372.
- <strong> [APA] : </strong> Gulati, V., Kumar, D., Popescu, D. E., & Hemanth, J. D. (2023). Extractive Article Summarization Using Integrated TextRank and BM25+ Algorithm. Electronics, 12(2), 372.
- <strong> [Chicago] : </strong> Gulati, Vaibhav, Deepika Kumar, Daniela Elena Popescu, and Jude D. Hemanth. "Extractive Article Summarization Using Integrated TextRank and BM25+ Algorithm." Electronics 12, no. 2 (2023): 372.
- <strong> [Harvard] : </strong> Gulati, V., Kumar, D., Popescu, D.E. and Hemanth, J.D., 2023. Extractive Article Summarization Using Integrated TextRank and BM25+ Algorithm. Electronics, 12(2), p.372.
- <strong> [Vancouver] : </strong> Gulati V, Kumar D, Popescu DE, Hemanth JD. Extractive Article Summarization Using Integrated TextRank and BM25+ Algorithm. Electronics. 2023 Jan 11;12(2):372.
- <strong> [BibTex] : </strong>
```bibTex
@article{gulati2023extractive,
  title={Extractive Article Summarization Using Integrated TextRank and BM25+ Algorithm},
  author={Gulati, Vaibhav and Kumar, Deepika and Popescu, Daniela Elena and Hemanth, Jude D},
  journal={Electronics},
  volume={12},
  number={2},
  pages={372},
  year={2023},
  publisher={MDPI}
}
```
<br />
<br />


<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated !**. If you find any bugs or have ideas for improvements, please open an issue or submit a pull request. Follow the below steps to contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature`)
5. Open a Pull Request

**PS:** Don't forget to give the project a star! Thanks again!
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/gulvaibhav20/extractive-text-summarizer.svg?style=for-the-badge
[contributors-url]: https://github.com/gulvaibhav20/extractive-text-summarizer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gulvaibhav20/extractive-text-summarizer.svg?style=for-the-badge
[forks-url]: https://github.com/gulvaibhav20/extractive-text-summarizer/network/members
[stars-shield]: https://img.shields.io/github/stars/gulvaibhav20/extractive-text-summarizer.svg?style=for-the-badge
[stars-url]: https://github.com/gulvaibhav20/extractive-text-summarizer/stargazers
[issues-shield]: https://img.shields.io/github/issues/gulvaibhav20/extractive-text-summarizer.svg?style=for-the-badge
[issues-url]: https://github.com/gulvaibhav20/extractive-text-summarizer/issues
[license-shield]: https://img.shields.io/github/license/gulvaibhav20/extractive-text-summarizer.svg?style=for-the-badge
[license-url]: https://github.com/gulvaibhav20/extractive-text-summarizer/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/vaibhav-gulati/

[product-screenshot]: assets/screenshot.png
[Python.com]: https://img.shields.io/badge/Built%20With%20Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[summarization-process]: assets/flowchart.png
[config-readme]: https://github.com/gulvaibhav20/extractive-text-summarizer/tree/main/src
