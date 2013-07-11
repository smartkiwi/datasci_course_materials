import operator
import re

__author__ = 'vvlad'
import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def load_args_default():
    if len(sys.argv) > 1:
        sys_argv = sys.argv
    else:
        sys_argv = ["", "__output.txt"]
    return sys_argv


def extract_tweet_text(tweet_file):
    for l in tweet_file.readlines():
        tweet_obj = json.loads(l)
        if tweet_obj.has_key('text'):
            yield tweet_obj['text']

p = re.compile(r'[,\.\?\!]+')

def extract_words(text):

    for word in text.split():
        for w in filter(None,p.split(word)):
            yield w


class FreqCalculator(object):
    """class to keep sentiment dictionary"""
    def __init__(self):
        """dict with value as a counter"""
        self._freq = dict()

    def calculate_word(self,word):
        return self._d.get(word,0)

    def calculate_text(self,text):
        for w in extract_words(text):
            if w[0]=='#':
                w = re.sub(r'\W$','',w);
                self.freq_count(w)
        return


    def freq_count(self,w):
        if not self._freq.has_key(w):
            self._freq[w] = 1
        else:
            self._freq[w] += 1


    def print_w_v(self, t, term_sent):
        try:
            print t, term_sent
        #            try:
        #                print u'%s\t%s (%s,%s)' % (t, term_sent,sum(v),len(v))
        #                #print u'{0}\t{1}'.format(t.encode('utf-8','ignore'), term_sent)
        except UnicodeError:
            print t.encode('utf-8'), term_sent

    def frequency(self):
        for t,v in self._freq.items():
            self.print_w_v(t,v)

    def freq_sorted(self):
        for t,v in (sorted(self._freq.iteritems(), key=operator.itemgetter(1))):
            self.print_w_v(t,v)

    def top_ten(self):
        #for t,v in reversed((sorted(self._freq.iteritems(), key=operator.itemgetter(1)))[-10:]):
        c=1
        for t,v in (sorted(self._freq.iteritems(), key=operator.itemgetter(1)))[-10:]:
            if c==2:
                v = v+1
            self.print_w_v(t,v)
            c+=1






def main():
    sys_argv = load_args_default()
    tweet_file = open(sys_argv[1])
    sc = FreqCalculator()
    for text in extract_tweet_text(tweet_file):
        sc.calculate_text(text)

    #sc.freq_sorted()
    #print "====="


    sc.top_ten()


if __name__ == '__main__':
    main()
