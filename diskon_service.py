import pdb

class DiskonCalculator:
    """Menghitung harga akhir adalah diskon"""

    def hitung_diskon(self, harga_awal: float, presentase_diskon: int) -> float:

        # pdb.set_trace() <-- Untuk debugging tempatkan disini

        # --- BUG LOGIKA DISINI ---
        # Presentase tidak dibagi 100, sehingga diskon 10% dhitung sebagai 1000%
        # jumlah_diskon = harga_awal * presentase_diskon
        
        # Code perbaikan
        jumlah_diskon = harga_awal * presentase_diskon / 100

        harga_akhir = harga_awal - jumlah_diskon

        return harga_akhir
    
# UJI COBA (Ini adalah test case yang akan GAGAL) ---
if __name__ == '__main__':
    calc = DiskonCalculator()
    # input: 1000 - 10%. Hasil yang diharapkan: 900.0
    hasil = calc.hitung_diskon(1000, 10)
    print(f"Hasil: {hasil}")
    # Output: Hasil: 9000.0 (SALAH)