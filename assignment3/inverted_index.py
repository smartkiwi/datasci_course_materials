__author__ = 'vvlad'


import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    doc_id = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w,doc_id)


def reducer(key, list_of_values):
    # key: word
    # value: list of doc_ids
    total = 0

    mr.emit((key, list(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':

    inputfile = "./data/books.json"
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]

    inputdata = open(inputfile)
    mr.execute(inputdata, mapper, reducer)