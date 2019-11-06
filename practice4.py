import string

from time import sleep

# filename = "input.txt"
#
# dict_name = {}
# with open(filename, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip()
#         line = line.split(". ")
#         dict_name[line[0]] = int(line[1])
# print("Loooosers\n")
# total = 0
# for key, value in dict_name.items():
#     total += value
#     if value < 3:
#         print("FIO: {:15} and score {}".format(key, value))
#
# print("Avg = {}".format(round(total / len(dict_name)),0))
# print("Avg = {:.3f}".format(total / len(dict_name)))
#
#
# filename = "text.txt"
#
# split_value = ('!', '.', '...')
# with open(filename, 'r') as f:
#     text = f.read()
#     for char in split_value:
#         text = text.replace(char, ".")
#     text = text.replace('\n', " ")
#     sentences = text.split(". ")
#     number_sentences = 0
#     number_words = 0
#     number_letters = 0
#     number_all_letters = 0
#     number_decimal = 0
#     number_special = 0
#     for s in sentences:
#         print("{}".format(s))
#         number_sentences += 1
#         words = s.split(" ")
#         for w in words:
#             number_words += 1
#             for l in w:
#                 if l.isalpha():
#                     number_letters += 1
#                 elif l.isdecimal():
#                     number_decimal += 1
#                 elif l == '(' or l == ')' or l == '%' or l == '"' or l == '?' or l == ',' or l == '.':
#                     number_special += 1
#                 number_all_letters += 1
#
#     print("\nNumber of sentences is: {}\nNumber of words is: {}\nNumber of all letters is: {}"
#           "\nNumber of alpha is: {}\nNumber of decimal is: {}\nNumber of brackets is: {}"
#           .format(number_sentences, number_words, number_all_letters, number_letters, number_decimal, number_special))

# with open("output.txt", 'w') as f:
#     for i in range(12):
#         f.write("{0:<3} {:^3} {:>5}\n".format(i, i ** 2, i ** 3))

# with open("output.txt", 'w') as f:
#     for i in range(1, 16):
#         f.write("{:<2} = {:0>4b}\n".format(i, i))

# n = 10
# m = 10
# s = 5
# with open("output.txt", 'w') as f:
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 f.write("{:{}} ".format(i * j, s))
#                 if j == m:
#                     f.write("{:{}}\n".format(i * j, s))

n = 5
with open("output.txt", 'w') as f:
    while j < n:
        for i in range(1, n + 1):
                f.write("{:3} ".format(j))
                if j == m:
                    f.write("{:3}\n".format(j))

with open("output.txt", 'r') as f:
    print(f.read())
