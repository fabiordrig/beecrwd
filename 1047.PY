start_hour, start_minute, final_hour, final_minute = list(map(int, input().split()))

dif = ((final_hour * 60) + final_minute) - ((start_hour * 60) + start_minute)
if dif <= 0:
    dif += 24 * 60

time = dif // 60
minute = dif % 60
print(f"O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)")
