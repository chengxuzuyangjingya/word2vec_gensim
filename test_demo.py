# -*- coding: utf-8 -*-   
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)
model = word2vec.Word2Vec.load("./train_demo")

print ("\nproperties和performance的余弦距离")
print (model.similarity('properties','performance'))

print ("\nin和to的余弦距离")
print (model.similarity('in','to'))

print ("properties最接近的词语")
for i in model.most_similar("properties"):
    print (i[0],i[1])