r, c = map(int, input("Enter rows and columns: ").split())
z = 0
print("Enter elements:")
for i in range(r):
    row = list(map(int, input().split()))
    z += row.count(0)

if z > (r * c) // 2:
    print("Matrix is Sparse")
else:
    print("Matrix is Not Sparse")
