def run(a = 0, b = 15):
    list = []

    while a <= b:
        list.append(a)
        a += 1
    return list    


if __name__ == '__main__':
    print(run(1))
