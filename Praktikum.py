import re

data = {}

def garis():
    print("======================================================================")

def valid_nama(nama):
    # Nama hanya boleh berisi huruf dan spasi
    return bool(re.match(r'^[A-Za-z ]+$', nama))

def input_nama():
    while True:
        nama = input("Nama\t: ")
        if valid_nama(nama):
            return nama
        else:
            print("ERROR: Nama hanya boleh berisi huruf! Coba lagi.\n")

def lihat_data():
    print("\nDaftar Nilai")
    garis()
    print("| NO |  NIM   |   NAMA   | TUGAS | UTS | UAS | AKHIR |")
    garis()

    if not data:
        print("|                           TIDAK ADA DATA                           |")
        garis()
        return

    for i, (nim, mhs) in enumerate(data.items(), start=1):
        print(f"| {i:<2} | {nim:<6} | {mhs['nama']:<8} | {mhs['tugas']:<5} | "
              f"{mhs['uts']:<3} | {mhs['uas']:<3} | {mhs['akhir']:<5} |")
    garis()

def tambah_data():
    print("\nTambah Data")
    nim = input("NIM\t: ")
    nama = input_nama()  # ← Validasi nama

    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    tugas = int(input("Nilai Tugas\t: "))

    akhir = round((tugas * 0.30) + (uts * 0.35) + (uas * 0.35), 2)

    data[nim] = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }

def ubah_data():
    print("\nUbah Data")
    nim = input("Masukkan NIM: ")

    if nim not in data:
        print("Data dengan NIM tersebut tidak ditemukan.")
        return

    print("Isi data baru (kosongkan jika tidak ingin mengubah):")
    nama_baru = input("Nama baru\t: ")

    if nama_baru.strip() != "":
        while not valid_nama(nama_baru):
            print("ERROR: Nama hanya boleh berisi huruf! Coba lagi.")
            nama_baru = input("Nama baru\t: ")
        data[nim]["nama"] = nama_baru

    uts = input("Nilai UTS baru\t: ")
    uas = input("Nilai UAS baru\t: ")
    tugas = input("Nilai Tugas baru\t: ")

    if uts.isdigit():
        data[nim]["uts"] = int(uts)
    if uas.isdigit():
        data[nim]["uas"] = int(uas)
    if tugas.isdigit():
        data[nim]["tugas"] = int(tugas)

    # Hitung ulang nilai akhir
    info = data[nim]
    info["akhir"] = round(
        info["tugas"] * 0.30
        + info["uts"] * 0.35
        + info["uas"] * 0.35, 2
    )

def hapus_data():
    print("\nHapus Data")
    nim = input("Masukkan NIM: ")

    if nim in data:
        del data[nim]
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")

def cari_data():
    print("\nCari Data")
    nim = input("Masukkan NIM: ")

    if nim in data:
        mhs = data[nim]
        print("\nData ditemukan:")
        print(f"NIM\t: {nim}")
        print(f"Nama\t: {mhs['nama']}")
        print(f"Tugas\t: {mhs['tugas']}")
        print(f"UTS\t: {mhs['uts']}")
        print(f"UAS\t: {mhs['uas']}")
        print(f"Akhir\t: {mhs['akhir']}")
    else:
        print("Data tidak ditemukan.")

# Program Utama
print("Program Input Nilai")
print("===================")

while True:
    print("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar]:", end="")
    pilih = input().lower()

    if pilih == "l":
        lihat_data()
    elif pilih == "t":
        tambah_data()
    elif pilih == "u":
        ubah_data()
    elif pilih == "h":
        hapus_data()
    elif pilih == "c":
        cari_data()
    elif pilih == "k":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.")
