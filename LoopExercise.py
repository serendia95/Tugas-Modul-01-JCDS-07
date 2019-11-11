# Password checker

# password = False
# p = "281095"
# count = 1
# count1 = 3

# print("Ketik password: ")

# while password == False:
#     a = input("")
    
#     if a == p:
#         print("Password Benar!")
#         password = True
#     else:
#         if count < count1:
#             print("Password Salah! Ketik password:")
#             count += 1
#         else:
#             print("Silahkan coba lagi dalam 30 detik!")
#             break

# Pyramid maker

# a = 1
# b = 10
# c = 9

# for i in range(a, b, 2):
#     print((c * "   ") + (i * " * "))
#     c -= 1

# Number eliminator

# a = [1, 2, 6, 4, 6, 3, 4, 7, 9, 3]
# b = []

# for i in a:
#     if i < 5:
#         b.append(i)
# print(b)

# Number eliminator (one liner)

# a = [1, 2, 6, 4, 6, 3, 4, 7, 9, 3]

# print([i for i in a if i < 5])

# Word in sentence reverser

# a = "Hai aku Lintang"
# a = a.split(" ")
# b = []

# for i in range(len(a)):
#     b.append(a[i][::-1])

# b = " ".join(b)
# print(b)

# Caesar Cipher

# a = "abcdefghijklmnopqrstuvwxyz"
# b = input("Inpur word to cipher: ")
# c = -1
# d = []

# for i in b:
#     ii = a.index(i)

#     if ii + c > 25:
#         ii = ii + c - 26
#     elif ii + c < 0:
#         ii = 26 + ii + c
#     else:
#         ii += c

#     d.append(a[ii])
#     e = "".join(d)

# print(e)

# Numbers pyramid

# a = 0
# b = 5
# c = ""

# for i in range(b):
#     for j in range(b - i):
#         c = c + f"{j + 1} "
#     c = c + "\n"
# print(c)
        
# for i in range(a, b):
#     c = c + f"{b - i} "
#     print(c)

# for i in range(a, b):
#     print(f"{i + 1} " * (b - i))

# Menghitung pangkat tanpa pow dan **

# a = 3
# b = 3
# c = 1

# while b > 0:
#     c = c * a
#     b -= 1
# print(c)

# Bubble Sort

# x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1]

# def bubbleSort(list) :

#     for i in range(len(list), 0, -1):

#         for j in range(0, i-1):

#             if (list[j] > list[j + 1]):

#                 temp = list[j]

#                 list[j] = list[j + 1]

#                 list[j + 1] = temp

#     return list

# print(bubbleSort(x))

# Prime numbers generator

# def prime(a):
#     b = []
#     c = False

#     for i in range(1, a+1):
#         if i > 1: 
#             if i == 2:
#                 c = True
#             else:
#                 for j in range(2, i): 
#                     if (i % j) == 0:
#                         c = False
#                         break
#                     else: 
#                         c = True
#         if c == True:
#             b.append(i)
#     return b

# a = 100

# print(prime(a))