time = int(input())
speed = int(input())


def gas(time, speed):
    distance = time * speed
    liters = distance / 12

    print(f"{liters:.3f}")


gas(time, speed)
