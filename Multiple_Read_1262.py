while True:
    try:
        processes = input()
        process_list = list(processes)
        qty = int(input())

        result = 0
        aux = []

        for i in process_list:
            if i.upper() == "W":
                result += 1
                aux = []
            else:
                if len(aux) == 0:
                    aux.append(i)
                    result += 1
                    continue

                if len(aux) == qty:
                    result += 1
                    aux = []
                    aux.append(i)
                    continue

                if aux.count(i) > 0:
                    aux.append(i)
                    continue
        print(result)
    except EOFError:
        break
