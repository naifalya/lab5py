# Membuat dictionary daftar kontak
daftar_kontak = {
    'Ari': '08123456789',
    'Dina': '08765432100'
}

# Tampilkan kontak Ari
print("Kontak Ari:", daftar_kontak['Ari'])

# Tambah kontak baru Riko
daftar_kontak['Riko'] = '087654544'
print("Kontak Riko ditambahkan.")

# Ubah kontak Dina dengan nomor baru
daftar_kontak['Dina'] = '088999776'
print("Kontak Dina diubah.")

# Tampilkan semua Nama
print("Semua Nama:", list(daftar_kontak.keys()))

# Tampilkan semua Nomor
print("Semua Nomor:", list(daftar_kontak.values()))

# Tampilkan daftar Nama dan nomornya
print("Daftar Nama dan Nomor:")
for nama, nomor in daftar_kontak.items():
    print(f"- {nama}: {nomor}")

# Hapus kontak Dina
del daftar_kontak['Dina']
print("Kontak Dina dihapus.")