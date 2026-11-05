from data import data_sepatu, counter
from tampilan import (bersihkan_layar, tekan_enter, tampilkan_data, judul,
                    pesan_sukses, pesan_gagal, pesan_info, pilih_menu)
from validasi import (input_merek, input_ukuran, input_harga,
                    pilih_id, cari_duplikat)


def hitung_total(daftar_id, i):
    if i == len(daftar_id):
        return 0
    return data_sepatu[daftar_id[i]]["harga"] + hitung_total(daftar_id, i + 1)


def lihat_sepatu():
    bersihkan_layar()
    judul("--- DAFTAR SEPATU RUNNING ---")
    if len(data_sepatu) == 0:
        pesan_info("Belum ada data sepatu weh")
    else:
        tampilkan_data(data_sepatu)
        total = hitung_total(list(data_sepatu.keys()), 0)
        pesan_info(f"Total harga semua sepatu: Rp {total:,}")
    tekan_enter()


def tambah_sepatu():
    bersihkan_layar()
    judul("--- TAMBAH DATA SEPATU ---")
    merek = input_merek()
    ukuran = input_ukuran()
    harga = input_harga()

    if cari_duplikat(merek, ukuran, harga):
        pesan_gagal("Gagal! Data sepatu sudah ada bos.")
    else:
        counter["id_terakhir"] += 1
        data_sepatu[counter["id_terakhir"]] = {
            "merek": merek, "ukuran": ukuran, "harga": harga
        }
        pesan_sukses("Gokill data sepatu berhasil nambah tuh")
    tekan_enter()


def ubah_sepatu():
    bersihkan_layar()
    judul("--- UBAH DATA SEPATU ---")
    if len(data_sepatu) == 0:
        pesan_info("gaada sepatu yang mau diubah wok")
    else:
        tampilkan_data(data_sepatu)
        kunci = pilih_id()
        if kunci is not None:
            bagian = pilih_menu("Apa yang mau diubah bos", [
                ("Ubah Merek", "1"),
                ("Ubah Ukuran", "2"),
                ("Ubah Harga", "3"),
                ("Ubah Ukuran & Harganya sekalian lahh", "4"),
            ])

            if bagian == "1":
                data_sepatu[kunci]["merek"] = input_merek()
                pesan_sukses("Gokill merek diubah nichh")
            elif bagian == "2":
                data_sepatu[kunci]["ukuran"] = input_ukuran()
                pesan_sukses("Gokill ukuran diubah nichh")
            elif bagian == "3":
                data_sepatu[kunci]["harga"] = input_harga()
                pesan_sukses("gokss harganya diubah tuh")
            elif bagian == "4":
                ukuran_baru = input_ukuran()
                harga_baru = input_harga()
                data_sepatu[kunci].update({"ukuran": ukuran_baru, "harga": harga_baru})
                pesan_sukses("gokss ukuran sama harganya udah diubah nih")
            else:
                pesan_gagal("Perubahan dibatalkan")
    tekan_enter()


def hapus_sepatu():
    bersihkan_layar()
    judul("--- HAPUS DATA SEPATU ---")
    if len(data_sepatu) == 0:
        pesan_info("Belum ada datanya, apa yang mau dihapus kocak")
    else:
        tampilkan_data(data_sepatu)
        kunci = pilih_id()
        if kunci is not None:
            yakin = pilih_menu(
                f"Yakin mau dihapus {data_sepatu[kunci]['merek']} "
                f"ukuran {data_sepatu[kunci]['ukuran']}?",
                [("Ya, hapus", "y"), ("Tidak, batal", "n")],
            )
            if yakin == "y":
                dihapus = data_sepatu.pop(kunci)
                pesan_sukses(f"{dihapus['merek']} ukuran {dihapus['ukuran']} berhasil dihapus wok")
            else:
                pesan_info("Penghapusan batal yak")
    tekan_enter()