__author__ = 'vvlad'


import MapReduce
import sys

"""
Imlpements relation join
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #table = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id,record)
    #words = value.split()
    #for w in words:
    #    mr.emit_intermediate(w,doc_id)


def reducer(key, records_bag):
    # key: word
    # value: list of doc_ids
    total = 0
    order = []
    for r in records_bag:
        if r[0]=='order':
            order = r
            break
    for r in records_bag:
        if r[0]=='line_item':
            res = list(order)
            res.extend(r)
            mr.emit(res)

# Do not modify below this line
# =============================
if __name__ == '__main__':

    inputfile = "./data/records.json"
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]

    inputdata = open(inputfile)
    mr.execute(inputdata, mapper, reducer)
