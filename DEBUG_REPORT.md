# DEBUG REPORT – Bug PPN pada DiskonCalculator

## 1. Deskripsi Bug

Ditemukan bug logika pada fungsi `hitung_diskon`, di mana PPN 10% **ikut ditambahkan secara tidak sengaja** ke dalam perhitungan harga akhir. Fungsi yang seharusnya hanya menghitung diskon justru juga menambahkan pajak, sehingga hasil perhitungan menjadi lebih besar dari yang diharapkan.

## 2. Gejala Bug

* Input harga awal: 1000
* Diskon: 10%
* Output yang diharapkan: 900.0
* Output aktual: 990 (atau 990.0000000000001)

Nilai output lebih besar karena adanya tambahan PPN 10% setelah diskon.

## 3. Analisis Penyebab

Setelah dilakukan penelusuran kode, ditemukan bahwa setelah harga dikurangi diskon, nilai tersebut kembali dikalikan dengan faktor `1.10`. Faktor ini merepresentasikan penambahan PPN 10% yang tidak diminta dalam requirement awal fungsi `hitung_diskon`.

## 4. Proses Debugging

* Mengamati perbedaan antara expected output (900) dan actual output (990)
* Menggunakan `print` atau `pdb.set_trace()` untuk menelusuri alur perhitungan
* Menemukan bahwa PPN 10% ditambahkan pada harga setelah diskon

## 5. Solusi

Menghapus perhitungan PPN dari fungsi `hitung_diskon` agar fungsi hanya bertanggung jawab menghitung diskon sesuai dengan namanya dan kebutuhan sistem.

## 6. Hasil Setelah Perbaikan

* Fungsi `hitung_diskon` hanya menghitung diskon tanpa PPN
* Output perhitungan kembali sesuai dengan nilai yang diharapkan