from re import X
import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """
  
  #print(np.shape(X1))
  p = X1
  q = X2
  n = len(q)
  A = np.zeros((n,9))
  for i in range(n):
    A[i, 0:3] =  p[i,0]*q[i,:]
    A[i, 3:6] =  p[i,1]*q[i,:]
    A[i, 6:9] =  p[i,2]*q[i,:]
  
  #print(A)

  U, s , Vt = np.linalg.svd(A)
  
  E = [[Vt[8,0], Vt[8,1], Vt[8,2]], [Vt[8,3], Vt[8,4], Vt[8,5]], [Vt[8,6], Vt[8,7], Vt[8,8]]]

  E = np.transpose(E)

  U, s , Vt = np.linalg.svd(E)

  s = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]

  E = np.matmul(U, np.matmul(s, Vt))

  """ END YOUR CODE
  """
  return E
