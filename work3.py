def task1():
    s = 0
    i = 1
    N = 10
    max_ = 500
    while True:
        if i % 2 == 0:
            s += i**2
            print("sum is: ", s)
            print("iteration: ", i)
        i += 1
        if s > max_:
            break
        # elif i > N:
        #     break



def task3(N, a):
    flag = True
    while True:
        if N % a == 0:
            N = N // a
            if N == 1:
                break
        else:
            flag = False
            break
    return flag


def task4():
    start = 10
    end = 30
    while start <= end:
        print(start)
        start += 1
    pass

def bank(account, percent):
    n = 0  # количесство лет
    gain = 30000
    init = account
    while True:
        account += round(account * percent * 0.01)
        # print(account)
        n += 1
        if account > init + gain:
            print("\nTo have {} y.e. gain with {}% per year you need to wait "
                  "{} years and sum will be {}".format(gain, percent, n, account))
            break
    return n


def task6(sum):
    values = [1, 2, 4, 8, 16, 32, 64]
    dict_ = {v: 0 for v in reversed(values)}
    for v in dict_:
        dict_[v] = sum // v
        sum = sum % v
    # return dict(map(reversed, dict_.items()))
    return {value: key for key, value in dict_.items()}
    # return sorted(dict_, key=dict_.get)

if __name__ == "__main__":
    # num = int(input("Fill a number:\n"))
    # osn = int(input("Fill an osnovanie:\n"))
    # result = task3(num, osn)
    # if result:
    #     print("\n{} is power of {}".format(num, osn))
    # else:
    #     print("Number isn't power of 2")

    # bank(100000, 7.15)

    pocket = task6(150)
    print(pocket)
    for p in pocket:
        print("Kupurs value: ", p)
        print("Number of kupurs: {}\n".format(pocket[p]))