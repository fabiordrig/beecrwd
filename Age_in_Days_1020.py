age = int(input())


def age_in_days(age):
    years = age // 365
    months = (age % 365) // 30
    days = (age % 365) % 30
    print(f"{years} ano(s)\n{months} mes(es)\n{days} dia(s)")


age_in_days(age)
