import os

bersih = "cls" if os.name == "nt" else "clear"

Role = ("atmin", "yahaha user")

data_user = {
    "atminperdi": {"password": "atmin123", "role": Role[0]},
    "budi": {"password": "budikuy", "role": Role[1]},
}

data_sepatu = {
    1: {"merek": "adidas", "ukuran": 40, "harga": 2000000},
    2: {"merek": "ortus", "ukuran": 42, "harga": 3000000},
    3: {"merek": "asics", "ukuran": 41, "harga": 1500000},
}
id_terakhir = 3

jalan = True
while jalan:
    os.system(bersih)
    print("SISTEM PENCATAT STOK SEPATU RUNNING")
    print("=" * 50)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu (1-3): ")

    if menu_awal == "1":
        percobaan = 0
        user_aktif = None
        while percobaan < 3 and user_aktif is None:
            os.system(bersih)
            print("---LOGIN---")
            username = input("Username: ")
            password = input("Password: ")
            if username in data_user and data_user[username]["password"] == password:
                user_aktif = username
            else:
                percobaan += 1
                print(f"Username atau password salah wok Sisa percobaanmu: {3 - percobaan}")
                input("Tekan enter kalo mau lanjut wok")

        if user_aktif is None:
            print("Terlalu banyak percobaan lu. sana kembali ke menu awal.")
            input("pencet enter kalo mau lanjut wok")
        else:
            nama = user_aktif
            role = data_user[user_aktif]["role"]
            sesi = True

            while sesi:
                os.system(bersih)
                print(f"ciee bisa login: {nama} ({role})")
                print("=" * 50)
                if role == Role[0]:
                    print("1. Lihat Data Sepatu    (Read)")
                    print("2. Tambah Sepatu        (Create)")
                    print("3. Ubah Data Sepatu     (Update)")
                    print("4. Hapus Data Sepatu    (Delete)")
                    print("0. Logout")
                else:
                    print("1. Lihat Data Sepatu")
                    print("0. Logout")
                pilih = input("Pilih menu dulu: ")

                if pilih == "1":
                    os.system(bersih)
                    print("--- DAFTAR SEPATU RUNNING ---")
                    if len(data_sepatu) == 0:
                        print("Belum ada data sepatu weh")
                    else:
                        print(f"{'ID':<4}{'merek':<16}{'ukuran':<10}{'harga':>14}")
                        print("-" * 44)
                        for id_sepatu, info in data_sepatu.items():
                            print(f"{id_sepatu:<4}{info['merek']:<16}{info['ukuran']:<10}{info['harga']:>14,}")
                    input("\nPencet enter kalo mau kembali yak")

                elif pilih == "2" and role == Role[0]:
                    os.system(bersih)
                    print("--- TAMBAH DATA SEPATU ---")
                    while True:
                        merek = input("Merek          : ")
                        if merek != "":
                            break
                        print("Merek jangan kosong cuy")
                    while True:
                        ukuran = input("Ukuran (30-50) : ")
                        if ukuran.isdigit() and 30 <= int(ukuran) <= 50:
                            ukuran = int(ukuran)
                            break
                        print("Ukurannya harus antara 30 sampai 50 yak")
                    while True:
                        harga = input("Harga (Rp)     : ")
                        if harga.isdigit() and int(harga) > 0:
                            harga = int(harga)
                            break
                        print("Harga harus lebih dari 0, kalo engga ya gratis dong..")

                    duplikat = False
                    for info in data_sepatu.values():
                        if info["merek"] == merek and info["ukuran"] == ukuran and info["harga"] == harga:
                            duplikat = True
                    if duplikat:
                        print("Gagal! Data sepatu sudah ada bos.")
                    else:
                        id_terakhir += 1
                        data_sepatu[id_terakhir] = {"merek": merek, "ukuran": ukuran, "harga": harga}
                        print("Gokill data sepatu berhasil nambah tuh")
                    input("Pencet enter kalo mau kembali yak")

                elif pilih == "3" and role == Role[0]:
                    os.system(bersih)
                    print("--- UBAH DATA SEPATU ---")
                    if len(data_sepatu) == 0:
                        print("gaada sepatu yang mau diubah wok")
                    else:
                        print(f"{'ID':<4}{'merek':<16}{'ukuran':<10}{'harga':>14}")
                        print("-" * 44)
                        for id_sepatu, info in data_sepatu.items():
                            print(f"{id_sepatu:<4}{info['merek']:<16}{info['ukuran']:<10}{info['harga']:>14,}")

                        nomor = input("\nID sepatu yang diubah: ")
                        if nomor.isdigit() and int(nomor) in data_sepatu:
                            kunci = int(nomor)
                            print("1. Ubah Merek")
                            print("2. Ubah Ukuran")
                            print("3. Ubah Harga")
                            print("4. Ubah Ukuran & Harganya sekalian lahh")
                            bagian = input("Apa yang mau diubah bos: ")

                            if bagian == "1":
                                while True:
                                    merek = input("Merek apa bos : ")
                                    if merek != "":
                                        break
                                    print("Merek jangan kosong woii")
                                data_sepatu[kunci]["merek"] = merek
                                print("Gokill merek diubah nichh")
                            elif bagian == "2":
                                while True:
                                    ukuran = input("Mau ukuran berape lu (30-50): ")
                                    if ukuran.isdigit() and 30 <= int(ukuran) <= 50:
                                        ukuran = int(ukuran)
                                        break
                                    print("Ukuran harus 30-50 yak")
                                data_sepatu[kunci]["ukuran"] = ukuran
                                print("Gokill ukuran diubah nichh")
                            elif bagian == "3":
                                while True:
                                    harga = input("Harganya mau berapa bos (Rp): ")
                                    if harga.isdigit() and int(harga) > 0:
                                        harga = int(harga)
                                        break
                                    print("Harga harus lebih dari 0, kalo engga ya gratis dong..")
                                data_sepatu[kunci]["harga"] = harga
                                print("gokss harganya diubah tuh")
                            elif bagian == "4":
                                while True:
                                    ukuran = input("Mau ukuran berape lu (30-50): ")
                                    if ukuran.isdigit() and 30 <= int(ukuran) <= 50:
                                        ukuran = int(ukuran)
                                        break
                                    print("Ukuran harus 30-50 yak")
                                while True:
                                    harga = input("Harganya mau berapa bos (Rp): ")
                                    if harga.isdigit() and int(harga) > 0:
                                        harga = int(harga)
                                        break
                                    print("Harga harus lebih dari 0, kalo engga ya gratis dong..")
                                data_sepatu[kunci].update({"ukuran": ukuran, "harga": harga})
                                print("gokss ukuran sama harganya udah diubah nih")
                            else:
                                print("ngawur, masukkin yang bener kocak")
                        else:
                            print("ID-nya ga valid wok")
                    input("Pencet enter kalo mau kembali yak")

                elif pilih == "4" and role == Role[0]:
                    os.system(bersih)
                    print("--- HAPUS DATA SEPATU ---")
                    if len(data_sepatu) == 0:
                        print("Belum ada datanya, apa yang mau dihapus kocak")
                    else:
                        print(f"{'ID':<4}{'merek':<16}{'ukuran':<10}{'harga':>14}")
                        print("-" * 44)
                        for id_sepatu, info in data_sepatu.items():
                            print(f"{id_sepatu:<4}{info['merek']:<16}{info['ukuran']:<10}{info['harga']:>14,}")

                        nomor = input("\nMau sepatu apa yang dihapus cuy (ID): ")
                        if nomor.isdigit() and int(nomor) in data_sepatu:
                            kunci = int(nomor)
                            yakin = input(
                                f"Yakin mau dihapus {data_sepatu[kunci]['merek']} "
                                f"ukuran {data_sepatu[kunci]['ukuran']}? (y/n): "
                            )
                            if yakin == "y":
                                dihapus = data_sepatu.pop(kunci)
                                print(f"{dihapus['merek']} ukuran {dihapus['ukuran']} berhasil dihapus wok")
                            elif yakin == "n":
                                print("Penghapusan batal yak")
                            else:
                                print("Isi yang bener wehh, penghapusan batal yak.")
                        else:
                            print("isi yang bener kocak")
                    input("Pencet enter kalo mau kembali yak")

                elif pilih == "0":
                    sesi = False

                else:
                    print("Isi yang bener kocak")
                    input("pencet enter kalo mau lanjut wok")

    elif menu_awal == "2":
        os.system(bersih)
        print("--- REGISTER AKUN BARU ---")
        username = input("Username (minimal 3 karakter, jangan spasi): ")
        password = input("Password (minimal 6 karakter): ")

        if len(username) < 3 or " " in username:
            print("Username minimal 3 karakter dan jangan spasi")
        elif username in data_user:
            print("Username dah dipake wok, makanya nama jangan pasaran")
        elif len(password) < 6:
            print("Password minimal 6 karakter yak")
        else:
            data_user[username] = {"password": password, "role": Role[1]}
            print("Gokss akun baru, login dah")
        input("pencet enter kalo mau lanjut wok")

    elif menu_awal == "3":
        print("Makasih yak, selesai deh")
        jalan = False

    else:
        print("Isi yang bener wok")
        input("pencet enter kalo mau lanjut wok")
        