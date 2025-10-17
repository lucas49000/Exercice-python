# Ex4
for n in range(0, 21):  # 0 à 20 inclus
    if n % 2 == 0 and n <= 10:
        print(f"{n} -> pair <= 10")
    elif n % 2 != 0 and n > 10:
        print(f"{n} -> impair > 10")
