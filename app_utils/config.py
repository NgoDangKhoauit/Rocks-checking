import os

INDEX_DIR = "data/index"
STATEMENTS_PATH = "data/statements.txt"

RETRIEVER_MODEL = "sentence-transformers/msmarco-distilbert-base-tas-b"
RETRIEVER_MODEL_FORMAT = "sentence_transformers"
RETRIEVER_TOP_K = 5

NLI_MODEL = os.environ.get("NLI_MODEL", "valhalla/distilbart-mnli-12-1")
print(f"Used NLI model: {NLI_MODEL}")

PROMPT_MODEL = os.environ.get("PROMPT_MODEL", "google/flan-t5-small")
print(f"Used Prompt model: {PROMPT_MODEL}")
