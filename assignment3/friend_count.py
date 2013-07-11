__author__ = 'vvlad'
__author__ = 'vvlad'


import MapReduce
import sys

"""
Friends Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: friendA
    # value: friendB
    a = record[0]
    #b = record[1]
    mr.emit_intermediate(a,1)


def reducer(key, list_of_values):
    # key: friendA
    # value: list of friend counts
    total = 0
    for v in list_of_values:
        total+=v

    mr.emit((key, total ))

# Do not modify below this line
# =============================
if __name__ == '__main__':

    inputfile = "./data/friends.json"
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]

    inputdata = open(inputfile)
    mr.execute(inputdata, mapper, reducer)
