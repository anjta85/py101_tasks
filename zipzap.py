for i in range(1, 100, 1):
    if i / 3 and i % 3 == 0:
        print(f"{i} делится на 3, результат (zip).")
    if i % 3 != 0:
        print(f"{i} не делится на 3")

    if i / 5 and i % 5 == 0:
        print(f"{i} делится на 5, результат (zap).")
    if i % 5 != 0:
        print(f"{i} не делится на 5")  
              
    if i / 15 and i % 15 == 0:
        print(f"{i} делится на 15, результат (zip-zap).")
    if i % 15 != 0:
        print(f"{i} не делится на 15")