__author__ = 'vvlad'
__author__ = 'vvlad'


import MapReduce
import sys

"""
Sequence Trim in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: friendA
    # value: friendB
    #a = record[0]
    b = record[1]
    if len(b)>10:
        b = record[1][:-10]
    mr.emit_intermediate(b,1)


def reducer(key, list_of_values):
    # key: trimmed string
    # value: list of values

    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':

    inputfile = "./data/dna.json"
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]

    inputdata = open(inputfile)
    mr.execute(inputdata, mapper, reducer)
