def multiplicacion(N1, N2, C1, R):
  if C1 == N1:
    print(R)
  else:
    R += N2
    C1 += 1
    multiplicacion(N1, N2, C, R)


N1 = input(intpuy())
N2 = input(intput())
multiplicacion(N1, N2, C, R)
