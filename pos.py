import nltk
from nltk.tokenize import word_tokenize nltk.download("punkt")
nltk.download("averaged_percepton_tagger.eng")
sentence = "The quick brown for jumps over the lazy day."
tokens = word.tokenize(sentence)
tags=nltk_pos_tag(tokens.lang = "eng")
print("POS tags: ",tags)
