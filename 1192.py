qty = int(input())


for i in range(qty):
    char = input()

    char_list = list(char)

    if int(char_list[0]) == int(char_list[2]):
        sum = int(char_list[0]) * int(char_list[2])
        print(sum)
    elif char_list[1].isupper():
        sum = int(char_list[2]) - int(char_list[0])
        print(sum)
    else:
        sum = int(char_list[0]) + int(char_list[2])
        print(sum)
