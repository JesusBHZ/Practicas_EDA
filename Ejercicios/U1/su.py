n = int(input("Cuantos nombres quieres almacenar: "))
m = int(input("Cuantos nombres quieres almacenar: "))
c = 0
d = n-1


def sum(n, m, c, d):
  if c == n:
    return
  else:
    c = c + 1
    d = d -1 
    print(c)
    sum(n, m, c,d)
  return d


print(sum(n, m, m,d))
