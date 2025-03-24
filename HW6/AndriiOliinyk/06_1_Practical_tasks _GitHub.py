def rozdil_chisel(start, end):
    """
    Розділяє числа в заданому діапазоні на три категорії:
    - парні, які діляться на 2,
    - непарні, які діляться на 3,
    - числа, які не діляться ні на 2, ні на 3.
    """

    parni_na_2 = []
    neparni_na_3 = []
    inshi_chisla = []

    for chislo in range(start, end + 1):
        if chislo % 2 == 0:
            parni_na_2.append(chislo)
        elif chislo % 3 == 0:
            neparni_na_3.append(chislo)
        else:
            inshi_chisla.append(chislo)

    print(f"Парні числа, які діляться на 2: {parni_na_2}")
    print(f"Непарні числа, які діляться на 3: {neparni_na_3}")
    print(f"Числа, які не діляться ні на 2, ні на 3: {inshi_chisla}")
# Викликаємо функцію для діапазону від 1 до 10
rozdil_chisel(1, 10)