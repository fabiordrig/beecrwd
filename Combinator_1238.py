qty = int(input())

for i in range(qty):
    t1, t2 = input().split()

    t_new = ""
    if len(t1) <= len(t2):
        for i in range(len(t1)):
            t_new += t1[i]
            t_new += t2[i]

        t_new += t2[len(t1) :]
    else:
        for i in range(len(t2)):
            t_new += t1[i]
            t_new += t2[i]
        t_new += t1[len(t2) :]
    print(t_new)
