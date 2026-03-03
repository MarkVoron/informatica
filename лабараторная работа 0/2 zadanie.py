disketa = 1.44
disketa_bites = disketa * 1024 * 1024
pages = 100
stroki = 50
symbols = 25
letter = 4
book = pages * stroki * symbols * letter
amount = disketa_bites // book
amount = int(amount)
print("Количество книг, помещающихся на дискету:", amount)


