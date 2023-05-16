qty = int(input())

for _ in range(qty):
    is_cheater = False

    diet = input().lower()
    meals = [input().lower() for _ in range(2)]

    diet_chars = list(diet)
    for meal in meals:
        for char in meal:
            if char in diet_chars:
                diet_chars.remove(char)
            else:
                is_cheater = True

    result = "".join(sorted(diet_chars)).upper()
    print("CHEATER" if is_cheater else result)
