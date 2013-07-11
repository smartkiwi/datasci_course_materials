__author__ = 'vvlad'
__author__ = 'vvlad'
__author__ = 'vvlad'


import MapReduce
import sys

"""
Matrix Multiplication in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(r):
    # key: friendA
    # value: friendB
    #a = record[0]
#    (m,i,j,v) = record
    N = 5
    if r[0]=='a':
        (m,i,j,v) = r
        for k in xrange(0, N):
            mr.emit_intermediate((i,k),r)
    if r[0]=='b':
        (m,j,k,v) = r
        for i in xrange(0, N):
            mr.emit_intermediate((i,k),r)

def reducer(key, list_of_values):
    # key: trimmed string
    # value: list of values

    a = dict()
    b = dict()
    for r in list_of_values:
        if r[0]=='a':
            (__,i,j,v) = r
            a[j] = v
        if r[0]=='b':
            (__,j,k,v) = r
            b[j] = v
    s = 0
    for j in xrange(0,5):
        s+=a.get(j,0)*b.get(j,0)


    r = list(key)
    r.append(s)
    mr.emit(tuple(r))

# Do not modify below this line
# =============================
if __name__ == '__main__':

    inputfile = "./data/matrix.json"
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]

    inputdata = open(inputfile)
    mr.execute(inputdata, mapper, reducer)
