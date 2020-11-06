# baseline model (lower bound score)
# marks every potential sentence boundary as a sentence boundary
# sentence_boundary_indices records every index at which a sentence boundary occurs

from brown_corpus import indices_answerkey, text_chunk

sentence_boundaries = [".", "?", "!"]
sentence_boundary_indices = [0]

for i in range(len(text_chunk)):
    if text_chunk[i] in sentence_boundaries:
        sentence_boundary_indices.append(i)

correct = len(list(set(indices_answerkey) & set(sentence_boundary_indices)))
precision = correct/len(indices_answerkey)
recall = correct/len(sentence_boundary_indices)
fmeasure = 2/(1/precision + 1/recall)

print("Baseline scores for Brown Corpus")
print("Precision: ", precision)
print("Recall: ", recall)
print("F-measure: ", fmeasure)