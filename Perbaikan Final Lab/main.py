import re
import random
import time

def validasi_jawaban(jawaban, pola):
    return re.match(pola, jawaban, re.IGNORECASE)

def buat_petunjuk():
    petunjuk = [
        "Harta karun terletak di dekat pohon oak tua.",
        "Cari di bawah patung burung elang.",
        "Harta karun ada di bawah pasir di pantai.",
        "Cari di gua utara di balik air terjun.",
        "Harta karun tersembunyi di dalam peti tua di perpustakaan."
    ]
    return random.choice(petunjuk)

def lokasi_harta_karun():
    lokasi = ["pohon oak tua", "patung burung elang", "pantai", "gua utara", "peti tua di perpustakaan"]
    return random.choice(lokasi)

class PermainanPencarianHarta:
    def __init__(self):
        self.lokasi_harta = lokasi_harta_karun()
        self.petunjuk = buat_petunjuk()
        self.pola = re.escape(self.lokasi_harta)

    def mulai_permainan(self):
        print("Selamat datang di permainan Pencarian Harta Karun!")
        print("Petunjuk untuk menemukan harta karun:")
        print(self.petunjuk)
        print("\nCoba tebak di mana harta karun tersembunyi!")
        
        kesempatan = 3
        while kesempatan > 0:
            jawaban = input(f"\nTebakanmu (kesempatan tersisa {kesempatan}): ").strip().lower()
            if validasi_jawaban(jawaban, self.pola):
                print("Selamat! Kamu menemukan harta karun!")
                break
            else:
                kesempatan -= 1
                print("Tebakan salah. Coba lagi.")

            if kesempatan == 0:
                print(f"\nGame Over! Harta karun tersembunyi di {self.lokasi_harta}.")
    
    def beri_petunjuk_tambahan(self):
        petunjuk_tambahan = [
            "Cobalah tempat yang berhubungan dengan alam.",
            "Periksa di sekitar benda-benda besar.",
            "Cari tempat yang memiliki nilai sejarah."
        ]
        return random.choice(petunjuk_tambahan)

    def ringkasan_permainan(self):
        print("\nRingkasan permainan:")
        print(f"Lokasi harta karun: {self.lokasi_harta}")
        print(f"Petunjuk: {self.petunjuk}")
        print(f"Petunjuk tambahan: {self.beri_petunjuk_tambahan()}")

def main():
    permainan = PermainanPencarianHarta()
    permainan.mulai_permainan()
    permainan.ringkasan_permainan()

if __name__ == "__main__":
    main()