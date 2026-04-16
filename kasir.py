def hitung_total(harga_barang, daftar_belanja):
    total = 0

    for item, jumlah in daftar_belanja.items():
        if item in harga_barang:
            total += harga_barang[item] * jumlah

    return total


def hitung_diskon(total):
    if total > 50000:
        return total * 0.1
    return 0


def tampilkan_total(total):
    print(f"Total yang harus dibayar: {total}")


def main():
    harga_barang = {
        "mie": 10000,
        "es": 5000,
        "nasi": 12000
    }

    daftar_belanja = {
        "mie": 2,
        "es": 3,
        "nasi": 1
    }

    total = hitung_total(harga_barang, daftar_belanja)
    diskon = hitung_diskon(total)
    total_akhir = total - diskon

    tampilkan_total(total_akhir)


if __name__ == "__main__":
    main()
