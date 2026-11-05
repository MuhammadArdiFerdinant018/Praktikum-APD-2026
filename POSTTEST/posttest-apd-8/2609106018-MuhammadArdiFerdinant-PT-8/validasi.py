# validasi.py
# Modul untuk input yang divalidasi (merek, ukuran, harga, ID) dan cek duplikat.

from data import data_sepatu
from tampilan import pesan_gagal


def input_merek():
    while True:
        try:
            merek = input("Merek          : ").strip()
            if merek == "":
                raise ValueError("Merek jangan kosong cuy")
        except ValueError as e:
            pesan_gagal(str(e))
        else:
            return merek.lower()


def input_ukuran():
    while True:
        try:
            ukuran = int(input("Ukuran (30-50) : "))
            if ukuran < 30 or ukuran > 50:
                raise ValueError
        except ValueError:
            pesan_gagal("Ukurannya harus angka antara 30 sampai 50 yak")
        else:
            return ukuran


def input_harga():
    while True:
        try:
            harga = int(input("Harga (Rp)     : "))
            if harga <= 0:
                raise ValueError
        except ValueError:
            pesan_gagal("Harga harus angka lebih dari 0, kalo engga ya gratis dong..")
        else:
            return harga


def pilih_id():
    try:
        nomor = int(input("\nMasukkan ID sepatu: "))
        if nomor not in data_sepatu:
            raise KeyError
    except ValueError:
        pesan_gagal("ID harus berupa angka kocak")
        return None
    except KeyError:
        pesan_gagal("ID-nya ga valid wok")
        return None
    else:
        return nomor


def cari_duplikat(merek, ukuran, harga):
    for info in data_sepatu.values():
        if info["merek"] == merek and info["ukuran"] == ukuran and info["harga"] == harga:
            return True
    return False