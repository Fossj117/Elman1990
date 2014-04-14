import numpy as np
from pybrain.datasets import SupervisedDataSet

class SentStreamConverter(object):

    def __init__(self, sent_stream, cat_to_ex):

        self.sent_stream = sent_stream
        self.vocab = self._get_vocab(cat_to_ex)
        
        self.vec_len = len(self.vocab)
        print "VOCAB LEN IS %d" % self.vec_len

        self.DS = self._generate_Pybrain_DS()

    def getDataset(self):
        return self.DS

    def _get_vocab(self, cat_to_ex):
        labels = set([word for _, lis in cat_to_ex.items() for word in lis])
        labels = dict((x,i) for i,x in enumerate(labels))
        return labels

    def _word_to_vec(self, word):
        vec = np.zeros(self.vec_len, dtype='float32')
        vec[self.vocab[word]] = 1

        return vec
            
    def _generate_Pybrain_DS(self):

        vect_stream = []
        for word in self.sent_stream:
            vect_stream.append(self._word_to_vec(word))
        
        to_conv = zip(vect_stream, vect_stream[1:])
        to_conv.append((vect_stream[-1], vect_stream[0])) #add wrap around

        DS = SupervisedDataSet(29,29)
        for inp, targ in to_conv:
            DS.appendLinked(inp,targ)

        return DS
            

