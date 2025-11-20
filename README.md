# Dictionary

Dictionary adalah tipe data yang memungkinkan penyimpanan dan pengelolaan data dalam bentuk pasangan kunci-nilai (key-value pairs). Setiap elemen dalam dictionary terdiri dari dua bagian utama: kunci (key) yang bersifat unik dan nilai (value) yang terkait dengan kunci tersebut.

### **Latihan Manipulasi Dictionary untuk Data Kontak**

Program ini memanfaatkan struktur data **dictionary** untuk menyimpan dan mengelola informasi kontak, di mana setiap **nama** berperan sebagai *key* dan **nomor telepon** sebagai *value*. Adapun fungsi utama dari setiap bagian kode dijelaskan sebagai berikut:

1. **Inisialisasi Dictionary**
   Program mendefinisikan dictionary bernama `daftar_kontak` yang berisi dua pasangan data awal, yaitu kontak **Ari** dan **Dina**.

2. **Menampilkan Kontak Berdasarkan Nama**
   Program mengakses nomor telepon milik Ari dengan memanggil `daftar_kontak['Ari']` dan menampilkannya ke layar.

3. **Menambahkan Kontak Baru**
   Kontak baru atas nama **Riko** ditambahkan ke dalam dictionary dengan menetapkan key `'Riko'` dan value berupa nomor telepon yang sesuai.

4. **Memperbarui Data Kontak**
   Program memperbarui nomor telepon milik **Dina** dengan cara mengganti value pada key `'Dina'`.

5. **Menampilkan Seluruh Nama Kontak**
   Fungsi `daftar_kontak.keys()` digunakan untuk mengambil seluruh key dalam dictionary, yang kemudian ditampilkan sebagai daftar nama.

6. **Menampilkan Seluruh Nomor Telepon**
   Fungsi `daftar_kontak.values()` dipanggil untuk menampilkan seluruh nomor telepon yang tersimpan.

7. **Menampilkan Seluruh Data Kontak**
   Program menggunakan perulangan `for` bersama `items()` untuk menampilkan setiap pasangan nama dan nomor telepon yang terdapat dalam dictionary.

8. **Menghapus Data Kontak**
   Data kontak milik **Dina** dihapus dari dictionary dengan menggunakan perintah `del daftar_kontak['Dina']`.

Secara keseluruhan, kode ini mendemonstrasikan operasi dasar pada dictionary yang meliputi akses data, penambahan, pembaruan, penampilan seluruh isi, dan penghapusan data.

### **Latihan Dictionary untuk Daftar Nilai Mahasiswa**

Program ini menggunakan **dictionary** sebagai tempat penyimpanan data mahasiswa dengan struktur `{NIM: {nama, tugas, uts, uas, akhir}}`. Program menyediakan menu untuk melihat, menambah, mengubah, menghapus, dan mencari data.

1. **Validasi Nama**
   Fungsi `valid_nama()` menggunakan *regular expression* untuk memastikan nama hanya berisi huruf dan spasi. Fungsi `input_nama()` memastikan pengguna menginput nama yang valid sebelum data disimpan.

2. **Menampilkan Data**
   Fungsi `lihat_data()` menampilkan data dalam format tabel. Jika tidak ada data, program menampilkan pesan “TIDAK ADA DATA”.

3. **Menambah Data**
   `tambah_data()` meminta input NIM, nama (dengan validasi), serta nilai tugas, UTS, dan UAS. Nilai akhir dihitung menggunakan rumus:
   `0.30 * tugas + 0.35 * uts + 0.35 * uas`.

4. **Mengubah Data**
   `ubah_data()` memperbarui data berdasarkan NIM. Nama baru tetap divalidasi, sementara nilai lain dapat diubah bila dimasukkan.

5. **Menghapus dan Mencari Data**
   `hapus_data()` menghapus data berdasarkan NIM, dan `cari_data()` menampilkan detail data mahasiswa tertentu.

6. **Menu Utama**
   Program berjalan dalam loop dan menerima perintah:
   **L** (lihat), **T** (tambah), **U** (ubah), **H** (hapus), **C** (cari), dan **K** (keluar).

Program ini menerapkan operasi CRUD secara lengkap dengan validasi input pada bagian nama dan tampilan tabel yang rapi.
