from scipy.spatial import distance
import pandas as pd

def ham_d(A, B):
  h_dist = 0
  if len(A) == len(B):
    for i in range(len(A)):
      if A[i] != B[i]:
        h_dist = h_dist + 1
    if (h_dist > 30):
      print(B)

    print(h_dist)
  else:
    print('Image array not of equal length')

for i in range(60000):
  A= pd.read_excel('MNISTBarcodeDataset.xlsx').iloc[i,0]
  B= pd.read_excel('MNISTBarcodeDataset.xlsx').iloc[i+10,0]
  ham_d(A,B)

