from collections import defaultdict
import sys
import json
import re
import operator


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def load_args_default():
    if len(sys.argv) > 2:
        sys_argv = sys.argv
    else:
        sys_argv = ["", "AFINN-111.txt", "__output.txt"]
    return sys_argv


def extract_tweet_text_loc(tweet_file):
    for l in tweet_file.readlines():
        try:
            tweet_obj = json.loads(l)
            if tweet_obj.has_key('text') and tweet_obj.get('place') is not None and tweet_obj['place'].get('full_name') and tweet_obj['place'].get('country_code')=='US':
                state = get_state(tweet_obj['place']['full_name'])
                if state is not None:
                    yield (tweet_obj['text'],state)
        except ValueError:
            pass

def get_state(location_str):
    r = re.search(', (..)$',location_str)
    if r is not None:
        return r.group(1)
    return None

def extract_words(text):
    for word in text.split():
        yield word

class SentimentCalculator(object):
    """class to keep sentiment dictionary"""
    def __init__(self,sentiment_dict):
        self._d = sentiment_dict

    def calculate_word(self,word):
        return self._d.get(word,0)

    def calculate_text(self,text):
        sent = 0
        for w in extract_words(text):
            sent+=self.calculate_word(w)
        return sent


def main():
    sys_argv = load_args_default()

    sent_file = open(sys_argv[1])
    tweet_file = open(sys_argv[2])
    #hw()
    sent_dict = load_sentiments(sent_file)
    sc = SentimentCalculator(sent_dict)
    locdict = defaultdict(float)
    for text,loc in extract_tweet_text_loc(tweet_file):

        sc_calculate_text = sc.calculate_text(text)
        locdict[loc]+=sc_calculate_text
        #print "score: %s: %s" % (sc_calculate_text,text)
        #print sc_calculate_text
    #print locdict
    if len(locdict)>0:
        print (sorted(locdict.iteritems(), key=operator.itemgetter(1)))[-1:][0][0]



def load_sentiments(fp):
    sentiments = dict()
    for l in fp.readlines():
        (token,sentiment) = l.split("\t")
        sentiments[token] = float(sentiment.rstrip())
    return sentiments


if __name__ == '__main__':
    main()
