# the matVec takes a matrix and a vector and mulitplies them together
def matVec(M,V):
  '''
  Inputs
    M - matrix with a x b dimensions
    V - matrix with b x d dimensions
  Output
    C - matrix with a dimensions a x def
  Details
    This algorithim is to do a matrix and vector multiplication from M and V and make C, a vector. This algorithim stores the new list C and the function returns the list C.
  '''
  C = []
  #This is the empty set C that is being solved for
  for i in range(len(M)):
  #This iterates the block executing the length of the matrix.
    total = 0
    for j in range(len(V)):
      total = total + (M[i][j] * V[j])
      #This is multiplying the matrix and vector toghether and adding the total to the product.
    C.append(total)
    #This adds the data together.
  return C
  #This is returning the data to make the vector C

M1 = [[1,2],[3,4]]
V1 = [1,2]
print(matVec(M1,V1))
print(True)

M2 = [5,6]
V2 = [[3,4],[1,4]]
print(matVec(M2,V2))

M3 = 'python'
V3 = 2
print(matVec(M3,V3))
