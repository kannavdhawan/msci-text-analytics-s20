import numpy as np
def tokenizer(pos,neg):
    tokenized_pos=[]
    tokenized_neg=[]
    tokens=[]
    # lowercasing it as it won't omit words during stopword removal.
    pos=pos.lower()
    neg=neg.lower()
# -------splitting by \n -- sentence tokenization-------
    
    positive_reviews_split=pos.splitlines() # returns a list [Review 1, Review 2, Review 3, ...Review n]
    negative_reviews_split=neg.splitlines()
    # print(positive_reviews_split[1:3])

#----word tokenization----
    for i in positive_reviews_split:
        pass
        tokenized_pos.append(i.split())
    print("Tokenized pos subset-->")
    print(tokenized_pos[0:3]) 

    tokens.append(tokenized_pos)

    for j in negative_reviews_split:
        pass
        tokenized_neg.append(j.split())
    print("Tokenized neg subset-->")
    print(tokenized_neg[0:3])
    tokens.append(tokenized_neg)
    return tokens