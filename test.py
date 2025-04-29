import torch
from datasets import load_dataset
from sentence_transformers.util import semantic_search

faqs_embeddings = load_dataset('abhikumar63/embeddings_example', data_files="embeddings.csv")
dataset_embeddings = torch.from_numpy(faqs_embeddings["train"].to_pandas().to_numpy()).to(torch.float)

question = ["How can Medicare help me?"]
output = query(question)

query_embeddings = torch.FloatTensor(output)

hits = semantic_search(query_embeddings, dataset_embeddings, top_k=5)

# print(faqs_embeddings)
for item in hits[0]:
    print(item)

for i in range(len(hits[0])):
    print(texts[hits[0][i]['corpus_id']])
