# -*- coding: utf-8 -*-        
from gensim.models import word2vec
import os
import logging
train_dir="./mesh"
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)
class Mysentences(object):
    def __init__(self,dirname):
        self.dirname = dirname
    def __iter__(self):
        for filename in os.listdir(self.dirname):
            file_path = self.dirname + "/" + filename
            for line in open(file_path,encoding = 'gb18030',errors='ignore'):
                words = line.split(" ")
                result_words = []
                for word in words:
                    if word and word!='\n':
                        result_words.append(word)
                yield result_words

sentences=Mysentences(train_dir)
model = word2vec.Word2Vec(sentences, min_count=5, size = 200)
model.save("./train_demo")