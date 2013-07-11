import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def load_sentiments(fp):
    sentiments = dict()
    for l in fp.readlines():
        (token,sentiment) = l.split("\t")
        sentiments[token] = float(sentiment.rstrip())
    return sentiments

def load_args_default():
    if len(sys.argv) > 2:
        sys_argv = sys.argv
    else:
        sys_argv = ["", "AFINN-111.txt", "output.txt"]
    return sys_argv


def extract_tweet_text(tweet_file):
    for l in tweet_file.readlines():
        tweet_obj = json.loads(l)
        if tweet_obj.has_key('text'):
            yield tweet_obj['text']


def extract_words(text):
    for word in text.split():
        yield word


class SentimentCalculator(object):
    """class to keep sentiment dictionary"""
    def __init__(self,sentiment_dict):
        self._d = sentiment_dict
        """dict of list"""
        self._new_d = dict()

    def calculate_word(self,word):
        return self._d.get(word,0)

    def calculate_text(self,text):
        sent = 0
        unknown_words = set()
        for w in extract_words(text):
            if self.is_unknown(w):
                unknown_words.add(w)
            score = self._d.get(w,0)
            sent+=score
        self.update_new_dict(unknown_words,sent)
        return sent




    def is_unknown(self,word):
        return not self._d.has_key(word)

    def update_new_dict(self, unknown_words, sent):
        for w in unknown_words:
            if self._new_d.has_key(w):
                self._new_d[w].append(sent)
            else:
                self._new_d[w] = [sent]

    def new_terms(self):
#        for t in sorted(self._new_d.keys()):

        for t in self._new_d.keys():
            v  = self._new_d[t]
            term_sent = sum(v) / len(v)
            #print u'%s\t%s' % (t, term_sent)
            try:
                print t,term_sent
#            try:
#                print u'%s\t%s (%s,%s)' % (t, term_sent,sum(v),len(v))
#                #print u'{0}\t{1}'.format(t.encode('utf-8','ignore'), term_sent)
            except UnicodeError:
                print t.encode('utf-8'),term_sent



def main():
    sys_argv = load_args_default()

    sent_file = open(sys_argv[1])
    tweet_file = open(sys_argv[2])
    #hw()
    sent_dict = load_sentiments(sent_file)
    sc = SentimentCalculator(sent_dict)
    for text in extract_tweet_text(tweet_file):
        sc_calculate_text = sc.calculate_text(text)
        #print "score: %s: %s" % (sc_calculate_text,text)

    sc.new_terms()


if __name__ == '__main__':
    main()
