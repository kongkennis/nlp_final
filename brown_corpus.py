# brown.csv is raw corpus file, parsed into:
# - sentences: list of all correct sentences
# - indices_answerkey: list of indices where correct sentence boundary is
# - text_chunk: list with all sentences/tokens put together, our development corpus  

import pandas as pd

file = pd.read_csv("brown.csv")
sentence_column = file.tokenized_text
sentences_raw = sentence_column.tolist()

sentence_boundaries = [".", "!", "?"]

sentences = []
for sentence in sentences_raw:
    if sentence[-1] in sentence_boundaries:
        sentences.append(sentence)

text_chunk = []
for i in range(len(sentences)):
    tokens = sentences[i].split()
    for token in tokens:
        text_chunk.append(token)

indices_answerkey = [0]
tokens = sentences[0].split()
indices_answerkey.append(len(tokens) - 1)

for i in range(1, len(sentences)):
    tokens = sentences[i].split()
    indices_answerkey.append(len(tokens) + indices_answerkey[-1])

