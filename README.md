CQ-FW (Code Query Firewall) adalah open source python project untuk mengunci nama file pada folder khususnya project dan mendeteksi bila ada file baru, file hilang dan file yang dimodifikasi.

#KEBUTUHAN TEKNOLOGI
Install Python Versi 3 atau lebih

#CARA INSTALL
1. Extract fq-fw pada disk (saya sarankan diletakkan diluar project/folder yang akan dilakukan scan)
2. Buka file config.json
3. Tuliskan folder target. contoh: /var/www/project_name
4. Untuk membatasi folder tertentu dari proses scan, anda bisa menambahkan folder yang akan dilewati. contoh : /var/www/project_name/files,/var/www/project_name/images
5. Berikan ijin tulis untuk folder log
6. Jalankan file lock.py
7. Hasil lock file bisa dilihat pada file lock_files.json didalam folder log
8. Lakukan proses scan secara berkala. Untuk melakukan proses scan, jalankan file scan.py
9. Hasil scan akan bisa dilihat pada file lose_files.log (daftar file yang hilang), modified_files.log (daftar file yang dimodifikasi), new_files.log (daftar file baru) didalam folder log

#CATATAN
1. Jalankan file lock.py setiap kali anda melakukan perubahan pada project (Update)
2. Jalankan file scan.py setiap hari
