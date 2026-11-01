def baca_nilai(nama_file):
    file = open(nama_file, "r")
    data = file.read()
    file.close()

    nilai = data.split(",")
    total = 0

    for x in nilai:
        total += int(x)

    return total / len(nilai)


print("Rata-rata nilai:", baca_nilai("data/nilai.txt"))