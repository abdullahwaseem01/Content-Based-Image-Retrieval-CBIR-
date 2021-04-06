from scipy.spatial import distance
import numpy as np
from gmpy2 import mpz, hamdist, pack
import pandas as pd

def ham_d(A, B):
  h_dist = 0
  if len(A) == len(B):
    for i in range(len(A)):
      if A[i] != B[i]:
        h_dist = h_dist + 1
    if (h_dist > 50):
      print(B)

    print(h_dist)
  else:
    print('Image array not of equal length')


