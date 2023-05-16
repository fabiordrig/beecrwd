import string
alphabet = list(string.ascii_lowercase)



quantity = int(input())
for i in range(quantity):
    test_quantity = int(input())

    result = 0
    result_list = []

    for i in range(test_quantity):
        test = input()
        test = test.lower()
        test_list = list(test)
        result_list.append(test_list)

    for i in range(len(result_list)):
        for j in range(len(result_list[i])):
            result += alphabet.index(result_list[i][j]) + i + j

    print(result)



