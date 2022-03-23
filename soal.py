awal = int(input("angka awal: "))
akhir = int(input("angka akhir: "))
x = []
y = []
for i in range(awal, akhir+1):
    if i%2 == 1:
        y.append(i)

print("nilai ganjil: ", y)