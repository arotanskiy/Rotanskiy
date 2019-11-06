a = 2347
a1000 = a // 1000
print(a1000)
a100 = a % 1000 // 100
print(a100)
a10 = a % 100 // 10
print(a10)
a1 = a % 10 // 1
print(a1)

split_a = list(str(a))
print(split_a)
print(""" Test description \n continue""")

string = "Monty Python"
revert = str(string[::-1])
print(revert)
print("M" in string)
revert_list = list(revert)
print(revert_list)
revive = "".join(revert_list)
print(revive)