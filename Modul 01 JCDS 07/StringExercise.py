# Menghitung huruf di kata/kalimat tanpa count

# a = input("Input a word: ")
# b = input("Letter to count: ")
# c = a.lower().replace(b, "")
# d = len(a) - len(c)
# print(f"There is/are {d} letter(s) of \"{b}\" in \"{a}\" \n")

# Menghitung kata di kalimat tanpa count

# e = input("Input a sentence: ")
# f = input("Word to count: ")
# g = e.lower().split(" ")
# h = len(g)

# for i in g:
#     if i in f:
#         g.remove(i)

# j = len(g)
# k = h - j

# print(f"There is/are {k} word(s) of \"{f}\" in \"{e}\" \n")

# Membalik kalimat tanpa reverse dan [::-1]

# def sentence_reverser(b):
#     c = b.split()
#     d = []

#     for i in range(len(c)):
#         d.append(c[len(c) - 1 - i])
    
#     d = " ".join(d)
#     return d

# a = input("Input a sentence: ")

# print(f"Reverse sentence: {sentence_reverser(a)}")

# Mengganti huruf vokal dengan huruf "o"

# def vocal(b):
#     c = b.replace("a", "o")
#     d = c.replace("i", "o")
#     e = d.replace("u", "o")
#     f = e.replace("e", "o")
#     g = f.replace("A", "O")
#     h = g.replace("I", "O")
#     i = h.replace("U", "O")
#     j = i.replace("E", "O")
#     return(j)

# a = input("Sentence: ")
# print(f"Output: {vocal(a)}")