def p(x, y):
    a = 0
    for i in range(len(x)):
        if x[i] == "mie":
            a = a + 10000 * y[i]
        elif x[i] == "es":
            a = a + 5000 * y[i]
        elif x[i] == "nasi":
            a = a + 12000 * y[i]
        else:
            a = a + 0

    if a > 50000:
        a = a - (a * 0.1)

    print("Total:", a)


barang = ["mie", "es", "nasi"]
jumlah = [2, 3, 1]

p(barang, jumlah)