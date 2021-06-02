seq = []
#justForInisialization
gap = -4
mismatch = 0
match = 4

def readFiles():
    path1 = input("Your sequence file path (1) : ")
    path2 = input("Your sequence file path (2) : ")
    gap = int(input("Gap penalty : "))
    mismatch = int(input("Mismatch value: "))
    match = int(input("Match value: "))
    try:
        f = open(path1)
        d = f.readlines()
        seq.append({
            "name" : d[0][1:-1],
            "seq" : d[1]
        })
        f2 = open(path2)
        d2 = f2.readlines()
        seq.append({
            "name" : d2[0][1:-1],
            "seq" : d2[1]
        })
        f.close()
    except:
        seq.append({
            "name" : "seq1",
            "seq" : "CGCACCACCTCCCGGCTCCTGCGAC"
        })
        seq.append({
            "name" : "seq2",
            "seq" : "CGCACCACCGGCTCCTGCGAC"
        })
readFiles()

m = len(seq[1]["seq"]) + 1
n = len(seq[0]["seq"]) + 1
A = [[1 for i in range(n)] for j in range(m)]

def bottomUp():
  A[0][0] = 0
  for i in range(1, n):
    A[0][i] *= i*gap
  for i in range(1, m):
    A[i][0] *= i*gap
  
  for i in range(1, m):
    for j in range(1, n):
      if seq[1]["seq"][i-1] == seq[0]["seq"][j-1]:
        maks = max(A[i-1][j]+gap, A[i-1][j-1]+match, A[i][j-1]+gap)
      else:
        maks = max(A[i-1][j]+gap, A[i-1][j-1]+mismatch, A[i][j-1]+gap)
      A[i][j] = maks
bottomUp()

def trace(i, j, seq1, seq2, str1, str2):
  now = A[i][j]
  if seq[1]["seq"][str2] == seq[0]["seq"][str1]:
    seq1 += seq[0]["seq"][str1]
    seq2 += seq[1]["seq"][str2]
    str1 -=1
    i = i-1
    str2 -=1
    j = j-1
  elif (now - gap) == A[i-1][j]:
    seq1 += "_" 
    seq2 += seq[1]["seq"][str2]
    str2 -=1
    i = i-1
  elif (now - gap) == A[i][j-1]:
    seq2 += "_"
    seq1 += seq[0]["seq"][str1]
    str1 -=1
    j = j-1
  else:
    seq1 += seq[0]["seq"][str1]
    seq2 += seq[1]["seq"][str2]
    str1 -=1
    i = i-1
    str2 -=1
    j = j-1
  return i, j, seq1, seq2, str1, str2

def topDown():
  i = m-1
  j = n-1
  seq1 = ""
  seq2 = ""
  str1 = j-1
  str2 = i-1
  while(i!=0 and j!=0):
    i, j, seq1, seq2, str1, str2 = trace(i, j, seq1, seq2, str1, str2)
  seq1 = seq1[::-1]
  seq2 = seq2[::-1]
  print("Best Alignment:")
  print(seq[0]["name"], " : ", seq1)
  print(seq[1]["name"], " : ",seq2)
topDown()
  


