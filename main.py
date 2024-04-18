from board import Board

b1 = Board([1,2,3],1,3,"","prawo")
print(b1.history)

b2 = Board([1,2,3],b1.rows,b1.columns,b1.history,"gora")
b3 = Board([1,2,3],b1.rows,b1.columns,b1.history,"dol")
print(b2.history)

a = set()
a.add(b1)
a.add(b2)
a.add(b3)
print(a)