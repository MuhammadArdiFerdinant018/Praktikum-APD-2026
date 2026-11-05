import pwinput
from data import data_user, Role
from tampilan import (bersihkan_layar, tekan_enter, judul,
pesan_sukses, pesan_gagal)


def login():
    percobaan = 0
    while percobaan < 3:
        bersihkan_layar()
        judul("---LOGIN---")
        username = input("Username: ")
        password = pwinput.pwinput("Password: ", mask="*")
        try:
            if data_user[username]["password"] != password:
                raise ValueError
        except (KeyError, ValueError):
            percobaan += 1
            pesan_gagal(f"Username atau password salah wok Sisa percobaanmu: {3 - percobaan}")
            tekan_enter()
        else:
            return username, data_user[username]["role"]
    pesan_gagal("Terlalu banyak percobaan lu. sana kembali ke menu awal.")
    tekan_enter()
    return "", ""


def register():
    bersihkan_layar()
    judul("--- REGISTER AKUN BARU ---")
    username_baru = input("Username (minimal 3 karakter, jangan spasi): ")
    password_baru = pwinput.pwinput("Password (minimal 6 karakter): ", mask="*")
    try:
        if len(username_baru) < 3 or " " in username_baru:
            raise ValueError("Username minimal 3 karakter dan jangan spasi")
        if username_baru in data_user:
            raise ValueError("Username dah dipake wok, makanya nama jangan pasaran")
        if len(password_baru) < 6:
            raise ValueError("Password minimal 6 karakter yak")
    except ValueError as e:
        pesan_gagal(str(e))
    else:
        data_user[username_baru] = {"password": password_baru, "role": Role[1]}
        pesan_sukses("Gokss akun baru, login dah")
    finally:
        tekan_enter()