figuras = [["cuadrados",6,[3,1]],
          ["trinagulos",5,[1,2]],
          ["rectangulos",4,[2,2]],
          ["circulos",3,[2,3]]]

figuras[0][1] = 5
figuras[0][2] = [1,3]
figuras[3][2][0] = 2
for f in figuras:
  print(f)