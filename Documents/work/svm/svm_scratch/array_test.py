import numpy as np
a = np.array([1, 2, 3]) #[1 2 3]
b = np.array([[1, 2, 3]]) #[[1 2 3]]
c = np.array([[1, 2], [3, 4]])
d = np.array([5, 6])
array_concatenation = np.c_[c, d]
print a, b, c #(3,) (1, 3) (2, 2)
#[[1 2]
# [3 4]]
print a.shape, b.shape, c.shape
e = np.ones(c.shape[0])
print e, e.shape
print "concatenation c and d"
print array_concatenation
print "array_concatenation[:, 1]"
c_column = array_concatenation[:, 1] #column 2
c_column = array_concatenation[:, 1] #column 3
c_multicolumn = array_concatenation[:, [1, 2]]
c_row = array_concatenation[1, :]
c_multirow = array_concatenation[: 1] #[[1 2 5]], cannot called multirow actually.
print c_column, c_row, c_multirow
print array_concatenation[1, 2]
print c[0]