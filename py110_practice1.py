import random
# from string import ascii_letters, digits, hexdigits

#
# def pow2(x):
#     return x ** 2

# a = [1, 2, 3, 4, 5]
# output = []
# for x in a:
#     output.append(pow2(x))
# print(output)

# lambda_pow2 = lambda x: x ** 2
# for i in range(1, 11):
#     print(lambda_pow2(i))

# print(list(map(lambda x: x ** 2, range(1, 11))))

# Рейтинг языков программирования
# prog_lang = [
#     {'Nov 2019': 7, 'Nov 2018': 1, 'Programming Language': 'Java', 'Ratings %': 16},
#     {'Nov 2019': 2, 'Nov 2018': 2, 'Programming Language': 'C', 'Ratings %': 16},
#     {'Nov 2019': 3, 'Nov 2018': 4, 'Programming Language': 'Python', 'Ratings %': 10},
#     {'Nov 2019': 4, 'Nov 2018': 7, 'Programming Language': 'C++', 'Ratings %': 6},
#     {'Nov 2019': 5, 'Nov 2018': 6, 'Programming Language': 'C#', 'Ratings %': 4},
#     {'Nov 2019': 1, 'Nov 2018': 3, 'Programming Language': 'Pascal', 'Ratings %': 3},
#     {'Nov 2019': 6, 'Nov 2018': 5, 'Programming Language': 'Test', 'Ratings %': 2}
#     ]
# print(list(map(lambda x: x['Programming Language'], prog_lang)))
# print(list(filter(lambda x: x > 5, map(lambda x: x['Ratings %'], prog_lang))))

# print(list(map(lambda x: x['Programming Language'], filter(lambda x: x['Ratings %'] >= 10, prog_lang))))
# change = map(lambda x: "{:>6}: {} -> {}".format(x['Programming Language'],
#                                                 x['Nov 2018'],
#                                                 x['Nov 2019']),
#              prog_lang)
# for s in change:
#     print(s)
#
# list(map(lambda x: x['Programming Language'], filter(lambda x: x['Ratings %'] >= 10, prog_lang)))
#
# list(map(lambda x: f"2018: {x['Programming Language']} - {x[Nov 2019:]}", filter(lambda x:)))

# list_ = [random.randint(-10,10) for _ in range(10)]
# print(list_)
# print([x for x in list_ if x > 0])
# print(list(filter(lambda x: x > 0, list_)))
# print(list(filter(lambda x: x % 2 == 0 and x < 0, list_)))

def add(x):
    return x + 2


a = [1, 2, 3]
output = []
list_ = [random.random() for _ in range(10)]

for i in a:
    output.append(add(i))
print(output)