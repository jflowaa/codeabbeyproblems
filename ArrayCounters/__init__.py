def get_list(file):
    list = file.readline()
    return list.split()


def count_numbers(list):
    for i in range(0, iter[0]):
        if list[i] in countList:
            countList[list[i]] += 1
        else:
            countList[list[i]] = 1
    return countList


file = open('data.txt', 'r')
iter = [int(i) for i in (file.readline()).split()]
numberRange = iter[1]
countList = {}
list = [int(i) for i in get_list(file)]
print(count_numbers(list))
