# Fact Checking

### Indexing pipeline
* [Crawling](https://github.com/NgoDangKhoauit/Rocks-checking/tree/main/notebooks/get_wikipedia_data.ipynb): Crawl data from Wikipedia, starting from the page [List of mainstream rock performers](https://en.wikipedia.org/wiki/List_of_mainstream_rock_performers) and using the [python wrapper](https://github.com/goldsmith/Wikipedia)
* [Indexing](https://github.com/NgoDangKhoauit/Rocks-checking/tree/main/notebooks/indexing.ipynb)
  * Preprocess the downloaded documents into chunks consisting of 2 sentences
  * Chunks with less than 10 words are discarded, because they are not very informative
  * Instantiate a [FAISS](https://github.com/facebookresearch/faiss) Document store and store the passages on it
  * Create embeddings for the passages, using a Sentence Transformer model and save them in FAISS. The retrieval task will involve [*asymmetric semantic search*](https://www.sbert.net/examples/applications/semantic-search/README.html#symmetric-vs-asymmetric-semantic-search)
  * Save FAISS index.

### Search pipeline

* The user enters a factual statement
* Compute the embedding of the user statement using the same Sentence Transformer used for indexing (`msmarco-distilbert-base-tas-b`)
* Retrieve the K most relevant text passages stored in FAISS (along with their relevance scores)
* **Text entailment task**: compute the text entailment between each text passage (premise) and the user statement (hypothesis), using a Natural Language Inference model (`microsoft/deberta-v2-xlarge-mnli`). For every text passage, we have 3 scores (summing to 1): entailment, contradiction, and neutral.
* Aggregate the text entailment scores: compute their weighted average, where the weight is the relevance score. **Now it is possible to tell if the knowledge base confirms, is neutral, or disproves the user statement.**
* *Empirical consideration: if in the first N passages (N<K),  there is strong evidence of entailment/contradiction (partial aggregate scores > 0.5), it is better not to consider (K-N) less relevant documents.*

### Repository structure
* [Rock_fact_checker.py](Rock_fact_checker.py) and [pages folder](./pages/): multi-page Streamlit web app
* [app_utils folder](./app_utils/): python modules used in the web app
* [notebooks folder](./notebooks/): Jupyter/Colab notebooks to get Wikipedia data and index the text passages (using Haystack)
* [data folder](./data/): all necessary data, including original Wikipedia data, FAISS Index and prepared random statements

### Installation

 To install this project locally, follow these steps:
* `git clone https://github.com/NgoDangKhoauit/Rocks-checking`
* `cd Rocks-checking`
* `pip install -r requirements.txt`

To run the web app, simply type: `streamlit run Rock_fact_checker.py`
