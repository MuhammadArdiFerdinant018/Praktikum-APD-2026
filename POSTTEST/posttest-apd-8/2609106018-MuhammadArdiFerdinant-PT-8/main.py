from data import Role
from tampilan import (bersihkan_layar, tekan_enter, judul, pesan_info, pesan_gagal, pilih_menu)
from autentikasi import login, register
from CRUD import lihat_sepatu, tambah_sepatu, ubah_sepatu, hapus_sepatu


def menu_user(nama, role):
    sesi = True
    while sesi:
        bersihkan_layar()
        pesan_info(f"ciee bisa login: {nama} ({role})")

        if role == Role[0]:
            pilihan = [
                ("Lihat Data Sepatu    (Read)", "1"),
                ("Tambah Sepatu        (Create)", "2"),
                ("Ubah Data Sepatu     (Update)", "3"),
                ("Hapus Data Sepatu    (Delete)", "4"),
                ("Logout", "0"),
            ]
        else:
            pilihan = [
                ("Lihat Data Sepatu", "1"),
                ("Logout", "0"),
            ]

        pilih = pilih_menu("Pilih menu dulu", pilihan)

        if pilih == "1":
            lihat_sepatu()
        elif pilih == "2" and role == Role[0]:
            tambah_sepatu()
        elif pilih == "3" and role == Role[0]:
            ubah_sepatu()
        elif pilih == "4" and role == Role[0]:
            hapus_sepatu()
        elif pilih == "0" or pilih is None:
            sesi = False
        else:
            pesan_gagal("Isi yang bener kocak")
            tekan_enter()


def main():
    jalan = True
    while jalan:
        bersihkan_layar()
        judul("SISTEM PENCATAT STOK SEPATU RUNNING")
        print("=" * 50)
        menu_awal = pilih_menu("Pilih menu", [
            ("Login", "1"),
            ("Register", "2"),
            ("Keluar", "3"),
        ])

        if menu_awal == "1":
            user_aktif, role = login()
            if user_aktif != "":
                menu_user(user_aktif, role)
        elif menu_awal == "2":
            register()
        elif menu_awal == "3" or menu_awal is None:
            pesan_info("Makasih yak, selesai deh")
            jalan = False
            
main()