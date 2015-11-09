import SocketServer
import sys
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

def word_feats(words):
    return dict([(word, True) for word in words])
 
def word_feats_sentence(sentence):
	return word_feats(sentence.split(' '))


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
	

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        
        print "{} wrote:".format(self.client_address[0])
        print self.data + " " + str(classifier.classify(word_feats_sentence(self.data)))
        
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    global classifier
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')
    negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
    posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4
    trainfeats = negfeats + posfeats 
    classifier = NaiveBayesClassifier.train(trainfeats)
    
    server.serve_forever()



    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    

