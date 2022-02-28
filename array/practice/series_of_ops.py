

def callOps(ops):
    sums = 0
    record = []
    for i in range(len(ops)):
        if ops[i].isdigit():
            record.append(int(ops[i]))
        elif ops[i] == 'C':
            record.pop()
        elif ops[i] == 'D':
            record.append(record[-1] * 2)
        elif ops[i] == '+':
            record.append(sum(record))
    print(record)
    return sum(record)


if __name__ == '__main__':
    arr = ['5', '2', 'C', 'D', '+']
    callOps(arr)
