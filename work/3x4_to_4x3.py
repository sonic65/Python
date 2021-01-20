matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
 
for x in range(len(matrix)):
  print (matrix[x])
  pass
hehe = [[row[i] for row in matrix] for i in range(4)]
print (hehe)