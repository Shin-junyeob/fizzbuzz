def fibo(num = 3):
    lst = [0] * num
    lst[0] = lst[1] = 1
    for i in range(2, num):
        lst[i] = lst[i-2] + lst[i-1]
    return lst


if __name__ == '__main__':
    num = int(input('num = '))
    if num < 3:
        print('too small ! num has to bigger then "3"')
    else:
        ans = fibo(num)
        print(f'fibo_lst: {ans}')
        print(f'lst[{num}] is {ans[num-1]}')
