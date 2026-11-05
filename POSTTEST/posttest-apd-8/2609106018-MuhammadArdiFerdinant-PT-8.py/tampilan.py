import os
import inquirer
from colorama import Fore, Style, init
from prettytable import PrettyTable

init(autoreset=True)

bersih = "cls" if os.name == "nt" else "clear"


def bersihkan_layar():
    os.system(bersih)


def tekan_enter():
    input("Pencet enter kalo mau lanjut wok")


def pesan_sukses(teks):
    print(Fore.GREEN + Style.BRIGHT + teks)


def pesan_gagal(teks):
    print(Fore.RED + Style.BRIGHT + teks)


def pesan_info(teks):
    print(Fore.CYAN + teks)


def judul(teks):
    print(Fore.YELLOW + Style.BRIGHT + teks)


def tampilkan_data(daftar):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Merek", "Ukuran", "Harga (Rp)"]
    for id_sepatu in daftar:
        info = daftar[id_sepatu]
        tabel.add_row([id_sepatu, info["merek"], info["ukuran"], f"{info['harga']:,}"])
    tabel.align["Merek"] = "l"
    tabel.align["Harga (Rp)"] = "r"
    print(tabel)


def pilih_menu(pesan, pilihan):
    """Menampilkan menu panah (inquirer). pilihan = list of (label, nilai).
    Mengembalikan nilai yang dipilih, atau None kalau dibatalkan (Ctrl+C)."""
    pertanyaan = [
        inquirer.List("menu", message=pesan, choices=pilihan),
    ]
    jawaban = inquirer.prompt(pertanyaan)
    if jawaban is None:
        return None
    return jawaban["menu"]