# Membuat class

# class student:
#     def __init__(self, nama, usia):
#         self.nama = nama
#         self.usia = usia

# data = [
#     {"nama": "Andi", "usia": 21},
#     {"nama": "Budi", "usia": 22},
#     {"nama": "Caca", "usia": 23},
#     {"nama": "Deni", "usia": 24}
# ]

# Andi = student(data[0]["nama"], data[0]["usia"])
# Budi = student(data[1]["nama"], data[1]["usia"])
# Caca = student(data[2]["nama"], data[2]["usia"])
# Deni = student(data[3]["nama"], data[3]["usia"])

# print(Andi.usia)

# Generate class from input(s)

# a = int(input("Berapa banyak objek yang akan dimasukkan: "))
# b = []
# c = []
# d = []
# z = []
# i = 1

# while i <= a:
#     print("")
#     e = input(f"Masukkan nama objek{i}: ")
#     b.append(e)
#     f = input(f"Masukkan tahun dibuatnya objek{i}: ")
#     c.append(f)
#     g = input(f"Masukkan warna objek{i}: ")
#     d.append(g)
#     i += 1

# class Objek:
#     def __init__(self, nama, tahun, warna):
#         self.nama = nama
#         self.tahun = tahun
#         self.warna = warna

# for i in range(len(b)):
#     nama = "objek" + str(i+1)
#     vars()[nama] = Objek(b[i], c[i], d[i])
#     z.append(nama)

# print("")
# print(objek1.nama)
# print(objek2.tahun)
# print(objek3.warna)