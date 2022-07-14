# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        N = reader.length()
        ga, gb = 1, 0
        inda, indb = 3, None

        f0123, f0124 = reader.query(0, 1, 2, 3), reader.query(0, 1, 2, 4)
        for i in range(4, N):
            f012i = reader.query(0, 1, 2, i)
            if f0123 == f012i:
                ga += 1
            else:
                gb += 1
                indb = i

        for i in (0, 1, 2):
            arr = [0, 1, 2, 4]
            arr.remove(i)

            if reader.query(*sorted(arr + [3])) == reader.query(*sorted(arr + [i])):
                ga += 1
            else:
                gb += 1
                indb = i
        if ga > gb:
            return inda
        elif gb > ga:
            return indb
        else:
            return -1


