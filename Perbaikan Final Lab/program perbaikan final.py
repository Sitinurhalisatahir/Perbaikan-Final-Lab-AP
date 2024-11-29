# Program untuk mengelola daftar aktivitas ramah lingkungan
def tambah_aktivitas(daftar, aktivitas):
    """Menambahkan aktivitas ke dalam daftar"""
    if aktivitas not in daftar:
        daftar.append(aktivitas)
        print(f"\nAktivitas '{aktivitas}' berhasil ditambahkan!")
    else:
        print(f"\nAktivitas '{aktivitas}' sudah ada dalam daftar.")

def hapus_aktivitas(daftar, aktivitas):
    """Menghapus aktivitas dari daftar"""
    if aktivitas in daftar:
        daftar.remove(aktivitas)
        print(f"\nAktivitas '{aktivitas}' berhasil dihapus!")
    else:
        print(f"\nAktivitas '{aktivitas}' tidak ditemukan dalam daftar.")

def tampilkan_aktivitas(daftar):
    """Menampilkan semua aktivitas dalam daftar"""
    if daftar:
        print("\nDaftar Aktivitas Ramah Lingkungan:")
        for idx, aktivitas in enumerate(daftar, start=1):
            print(f"{idx}. {aktivitas.capitalize()}")
    else:
        print("\nBelum ada aktivitas dalam daftar.")

def cari_aktivitas(daftar, kata_kunci):
    """Mencari aktivitas berdasarkan kata kunci"""
    hasil = [a for a in daftar if kata_kunci.lower() in a.lower()]
    if hasil:
        print("\nHasil pencarian:")
        for aktivitas in hasil:
            print(f"- {aktivitas.capitalize()}")
    else:
        print(f"\nTidak ditemukan aktivitas dengan kata kunci '{kata_kunci}'.")


daftar_aktivitas = []

while True:
    print("\n========== MENU ==========")
    print("1. Tambah Aktivitas")
    print("2. Hapus Aktivitas")
    print("3. Tampilkan Aktivitas")
    print("4. Cari Aktivitas")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        aktivitas_baru = input("Masukkan aktivitas ramah lingkungan: ")
        tambah_aktivitas(daftar_aktivitas, aktivitas_baru)
    elif pilihan == "2":
        aktivitas_hapus = input("Masukkan aktivitas yang ingin dihapus: ")
        hapus_aktivitas(daftar_aktivitas, aktivitas_hapus)
    elif pilihan == "3":
        tampilkan_aktivitas(daftar_aktivitas)
    elif pilihan == "4":
        kata_kunci = input("Masukkan kata kunci pencarian: ")
        cari_aktivitas(daftar_aktivitas, kata_kunci)
    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")