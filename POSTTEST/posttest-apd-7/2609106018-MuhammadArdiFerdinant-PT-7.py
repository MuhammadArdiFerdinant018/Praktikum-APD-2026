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

def tekan_enter():
    input("Pencet enter kalo mau lanjut wok")


def bersihkan_layar():
    os.system(bersih)

def tampilkan_data(daftar):
    print(f"{'ID':<4}{'merek':<16}{'ukuran':<10}{'harga':>14}")
    print("-" * 44)
    for id_sepatu in daftar:
        info = daftar[id_sepatu]
        print(f"{id_sepatu:<4}{info['merek']:<16}{info['ukuran']:<10}{info['harga']:>14,}")


def tampilkan_menu(role):
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


def input_merek():
    while True:
        try:
            merek = input("Merek          : ")
            if merek == "":
                raise ValueError("Merek jangan kosong cuy")
        except ValueError as e:
            print(e)
        else:
            return merek


def input_ukuran():
    while True:
        try:
            ukuran = int(input("Ukuran (30-50) : "))
            if ukuran < 30 or ukuran > 50:
                raise ValueError
        except ValueError:
            print("Ukurannya harus angka antara 30 sampai 50 yak")
        else:
            return ukuran


def input_harga():
    while True:
        try:
            harga = int(input("Harga (Rp)     : "))
            if harga <= 0:
                raise ValueError
        except ValueError:
            print("Harga harus angka lebih dari 0, kalo engga ya gratis dong..")
        else:
            return harga


def login():
    percobaan = 0
    while percobaan < 3:
        os.system('cls')
        print("---LOGIN---")
        username = input("Username: ")
        password = input("Password: ")
        try:
            if data_user[username]["password"] != password:
                raise ValueError
        except (KeyError, ValueError):
            percobaan += 1
            print(f"Username atau password salah wok Sisa percobaanmu: {3 - percobaan}")
            tekan_enter()
        else:
            return username, data_user[username]["role"]
    print("Terlalu banyak percobaan lu. sana kembali ke menu awal.")
    tekan_enter()
    return "", ""


def pilih_id():
    try:
        nomor = int(input("\nMasukkan ID sepatu: "))
        if nomor not in data_sepatu:
            raise KeyError
    except ValueError:
        print("ID harus berupa angka kocak")
        return None
    except KeyError:
        print("ID-nya ga valid wok")
        return None
    else:
        return nomor

def cari_duplikat(merek, ukuran, harga):
    for info in data_sepatu.values():
        if info["merek"] == merek and info["ukuran"] == ukuran and info["harga"] == harga:
            return True
    return False

def hitung_total(daftar_id, i):
    if i == len(daftar_id):  
        return 0
    return data_sepatu[daftar_id[i]]["harga"] + hitung_total(daftar_id, i + 1) 

def lihat_sepatu():
    os.system('cls')
    print("--- DAFTAR SEPATU RUNNING ---")
    if len(data_sepatu) == 0:
        print("Belum ada data sepatu weh")
    else:
        tampilkan_data(data_sepatu)
        total = hitung_total(list(data_sepatu.keys()), 0)
        print(f"Total harga semua sepatu: Rp {total:,}")
    tekan_enter()

def tambah_sepatu():
    global id_terakhir
    os.system('cls')
    print("--- TAMBAH DATA SEPATU ---")
    merek = input_merek()
    ukuran = input_ukuran()
    harga = input_harga()

    if cari_duplikat(merek, ukuran, harga):
        print("Gagal! Data sepatu sudah ada bos.")
    else:
        id_terakhir += 1
        data_sepatu[id_terakhir] = {"merek": merek, "ukuran": ukuran, "harga": harga}
        print("Gokill data sepatu berhasil nambah tuh")
    tekan_enter()


def ubah_sepatu():
    os.system('cls')
    print("--- UBAH DATA SEPATU ---")
    if len(data_sepatu) == 0:
        print("gaada sepatu yang mau diubah wok")
    else:
        tampilkan_data(data_sepatu)
        kunci = pilih_id()
        if kunci is not None:
            print("1. Ubah Merek")
            print("2. Ubah Ukuran")
            print("3. Ubah Harga")
            print("4. Ubah Ukuran & Harganya sekalian lahh")
            bagian = input("Apa yang mau diubah bos: ")

            if bagian == "1":
                data_sepatu[kunci]["merek"] = input_merek()
                print("Gokill merek diubah nichh")
            elif bagian == "2":
                data_sepatu[kunci]["ukuran"] = input_ukuran()
                print("Gokill ukuran diubah nichh")
            elif bagian == "3":
                data_sepatu[kunci]["harga"] = input_harga()
                print("gokss harganya diubah tuh")
            elif bagian == "4":
                ukuran_baru = input_ukuran()
                harga_baru = input_harga()
                data_sepatu[kunci].update({"ukuran": ukuran_baru, "harga": harga_baru})
                print("gokss ukuran sama harganya udah diubah nih")
            else:
                print("ngawur, masukkin yang bener kocak")
    tekan_enter()


def hapus_sepatu():
    os.system('cls')
    print("--- HAPUS DATA SEPATU ---")
    if len(data_sepatu) == 0:
        print("Belum ada datanya, apa yang mau dihapus kocak")
    else:
        tampilkan_data(data_sepatu)
        kunci = pilih_id()
        if kunci is not None:
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
    tekan_enter()

def register():
    os.system('cls')
    print("--- REGISTER AKUN BARU ---")
    username_baru = input("Username (minimal 3 karakter, jangan spasi): ")
    password_baru = input("Password (minimal 6 karakter): ")
    try:
        if len(username_baru) < 3 or " " in username_baru:
            raise ValueError("Username minimal 3 karakter dan jangan spasi")
        if username_baru in data_user:
            raise ValueError("Username dah dipake wok, makanya nama jangan pasaran")
        if len(password_baru) < 6:
            raise ValueError("Password minimal 6 karakter yak")
    except ValueError as e:
        print(e)
    else:
        data_user[username_baru] = {"password": password_baru, "role": Role[1]}
        print("Gokss akun baru, login dah")
    finally:
        tekan_enter()

def menu_user(nama, role):
    sesi = True
    while sesi:
        os.system('cls')
        print(f"ciee bisa login: {nama} ({role})")
        tampilkan_menu(role)
        pilih = input("Pilih menu dulu: ")

        if pilih == "1":
            lihat_sepatu()
        elif pilih == "2" and role == Role[0]:
            tambah_sepatu()
        elif pilih == "3" and role == Role[0]:
            ubah_sepatu()
        elif pilih == "4" and role == Role[0]:
            hapus_sepatu()
        elif pilih == "0":
            sesi = False
        else:
            print("Isi yang bener kocak")
            tekan_enter()


def main():
    jalan = True
    while jalan:
        os.system('cls')
        print("SISTEM PENCATAT STOK SEPATU RUNNING")
        print("=" * 50)
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        menu_awal = input("Pilih menu (1-3): ")

        if menu_awal == "1":
            user_aktif, role = login()
            if user_aktif != "":
                menu_user(user_aktif, role)
        elif menu_awal == "2":
            register()
        elif menu_awal == "3":
            print("Makasih yak, selesai deh")
            jalan = False
        else:
            print("Isi yang bener wok")
            tekan_enter()

main()