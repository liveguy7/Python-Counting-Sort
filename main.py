cl = []

def counting_sort(a,n):
  cl = [0] * n
  c = [0] * 100
  for i in range(100):
    c[i] = 0
  for j in range(n):
    c[a[j]] += 1
  for i in range(1,99):
    c[i] += c[i-1]
  for j in range(n-1, -1, -1):
    cl[c[a[j]] - 1] = a[j]
    c[a[j]] -= 1
    print(cl)

col = [0, 2, 1, 4, 6, 2, 1, 1, 0, 3, 7, 7, 9]
length = len(col)
print(col)
counting_sort(col,length)
#print(col)







