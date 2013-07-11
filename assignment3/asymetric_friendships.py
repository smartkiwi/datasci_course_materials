__author__ = 'vvlad'
__author__ = 'vvlad'
__author__ = 'vvlad'


import MapReduce
import sys

"""
Asymetric Friendship Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: friendA
    # value: friendB
    a = record[0]
    b = record[1]
    key = tuple(sorted((a,b)))
    mr.emit_intermediate(key,(a,b))


def reducer(key, list_of_p_f_pairs):
    # key: person
    # value: list of directed person to friend pairs
    if len(list_of_p_f_pairs)==1:
        mr.emit(list_of_p_f_pairs[0])
        mr.emit(tuple(reversed(list_of_p_f_pairs[0])))




# Do not modify below this line
# =============================
if __name__ == '__main__':

    inputfile = "./data/friends.json"
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]

    inputdata = open(inputfile)
    mr.execute(inputdata, mapper, reducer)
