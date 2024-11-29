# PROGRAM PENCARIAN HARTA KARUN
Program ini adalah permainan sederhana yang dirancang untuk memberikan pengalaman interaktif bagi pemain dalam mencari harta karun tersembunyi. Pemain diberikan petunjuk dalam bentuk teka-teki atau deskripsi lokasi, dan mereka harus menebak tempat di mana harta karun tersebut tersembunyi. Program ini menggabungkan berbagai konsep pemrograman seperti RegEx, Object-Oriented Programming (OOP), string manipulation, dan looping untuk menciptakan pengalaman permainan yang seru dan menantang.

# Fitur Utama Program
1. Pemilihan Lokasi Harta Karun Secara Acak
Program akan memilih lokasi harta karun secara acak dari sejumlah pilihan yang ada. Lokasi-lokasi ini tersembunyi di berbagai tempat seperti pohon, patung, pantai, gua, atau peti tua di perpustakaan.

2. Petunjuk Untuk Mencari Harta Karun
Setiap kali permainan dimulai, pemain akan diberikan sebuah petunjuk yang menunjukkan lokasi umum harta karun, namun tidak secara langsung memberi tahu lokasi pastinya. Petunjuk ini akan diambil secara acak dari beberapa pilihan yang tersedia.

3. Tebakan Pemain dengan Validasi
Pemain diminta untuk menebak lokasi tempat harta karun tersembunyi. Program menggunakan RegEx untuk memvalidasi apakah tebakan pemain sesuai dengan lokasi yang benar. Pemain diberikan 3 kesempatan untuk menebak dengan benar.

4. Petunjuk Tambahan
Setelah beberapa tebakan, program juga memberikan petunjuk tambahan untuk membantu pemain dalam mencari harta karun, agar pengalaman permainan tetap menyenangkan meskipun beberapa tebakan salah.

5. Ringkasan Permainan
Setelah permainan berakhir, program akan memberikan ringkasan tentang lokasi harta karun yang tersembunyi, petunjuk yang diberikan, dan petunjuk tambahan yang membantu pemain selama permainan.

# Cara Menggunakan Program
1. Menjalankan Program
Program ini dapat dijalankan pada editor Python atau terminal yang mendukung Python 3. Setelah program dijalankan, pemain akan disambut dengan petunjuk permainan dan diminta untuk mulai menebak lokasi harta karun.

2. Mulai Permainan
Pemain diminta untuk menebak lokasi tempat harta karun tersembunyi berdasarkan petunjuk yang diberikan. Pemain dapat memberikan jawaban yang berupa lokasi (misalnya: "pantai", "gua utara", dll). Setiap tebakan yang salah akan mengurangi kesempatan pemain.

3. Validasi Jawaban
Program akan memeriksa jawaban pemain dengan menggunakan RegEx untuk memastikan apakah tebakan pemain cocok dengan lokasi yang benar. Jika benar, permainan berakhir dengan kemenangan. Jika salah, program memberikan kesempatan lagi hingga 3 kali.

4. Petunjuk Tambahan
Jika pemain kesulitan, mereka bisa mendapatkan petunjuk tambahan yang akan diberikan oleh program secara acak. Petunjuk ini membantu pemain untuk lebih dekat dengan lokasi yang benar.

5. Ringkasan Permainan
Setelah permainan selesai, baik menang atau kalah, pemain akan diberikan ringkasan permainan yang mencakup lokasi harta karun yang sebenarnya, petunjuk yang diberikan, dan petunjuk tambahan yang telah diberikan selama permainan.

# Keunggulan Program Ini
1. Permainan Interaktif dan Menantang
Program ini memberikan pengalaman yang menyenangkan bagi pemain dengan menggabungkan elemen teka-teki dan pencarian yang berbasis pada petunjuk dan lokasi.

2. Penggunaan RegEx untuk Validasi Jawaban
Penggunaan RegEx dalam validasi jawaban memberikan keuntungan dalam membandingkan lokasi yang dimasukkan oleh pemain dengan pola yang tepat, memastikan hanya tebakan yang benar yang diterima.

4. Struktur Berbasis OOP
Program ini menggunakan pendekatan Object-Oriented Programming (OOP) yang memudahkan pengelolaan kode dalam permainan. Semua logika permainan dikelola oleh kelas PermainanPencarianHarta, sehingga kode lebih terstruktur dan mudah dikembangkan.

5. Petunjuk dan Hint Tambahan
Pemain tidak dibiarkan kesulitan tanpa petunjuk. Program memberikan petunjuk tambahan secara acak yang membantu pemain lebih dekat pada jawaban yang benar.

6. Kesempatan Terbatas untuk Menebak
Pemain diberikan 3 kesempatan untuk menebak lokasi harta karun. Fitur ini membuat permainan menjadi menantang dan memastikan bahwa pemain tidak terus-menerus bermain tanpa batas.

# Ringkasan Permainan
Setelah permainan selesai, program menyediakan ringkasan yang memberikan informasi lebih lanjut tentang lokasi harta karun, petunjuk yang diberikan, dan hint tambahan yang bisa jadi berguna untuk permainan selanjutnya.

Langkah-langkah Menjalankan Program
1. Mulai Program
Setelah menjalankan program, pemain akan melihat petunjuk yang diberikan oleh sistem tentang lokasi harta karun yang tersembunyi.

2. Menebak Lokasi Harta Karun
Pemain diminta untuk menebak lokasi harta karun berdasarkan petunjuk yang diberikan. Pemain memiliki 3 kesempatan untuk memberikan tebakan yang benar.

3. Cek Jawaban
Setelah setiap tebakan, program akan memberi tahu apakah tebakan pemain benar atau salah. Jika salah, program akan mengurangi kesempatan dan memberi kesempatan untuk menebak lagi.

4. Petunjuk Tambahan
Jika tebakan pemain salah, program akan memberikan petunjuk tambahan yang lebih spesifik untuk membantu pemain menemukan lokasi harta karun.

5. Selesai
Setelah pemain menebak lokasi yang benar atau kehabisan kesempatan, permainan berakhir dan program memberikan ringkasan permainan.

# Fleksibilitas dan Pengembangan Program
- Ekstensi Petunjuk: Program ini dapat dikembangkan lebih lanjut dengan menambahkan lebih banyak jenis petunjuk atau variasi dalam teka-teki untuk membuat permainan lebih menarik.

- Penyimpanan Data: Data permainan (seperti lokasi harta karun dan jawaban pemain) dapat disimpan dalam file eksternal untuk analisis lebih lanjut atau untuk digunakan dalam permainan berikutnya.

- Tingkat Kesulitan: Program ini dapat diperluas dengan menambahkan tingkat kesulitan, seperti meningkatkan jumlah petunjuk yang diberikan atau mengurangi jumlah kesempatan untuk menebak.

- Fitur Multiplayer: Program ini dapat dikembangkan lebih lanjut menjadi game multiplayer, di mana pemain bersaing untuk menemukan harta karun dengan lebih banyak pemain.

# Materi Pemrograman yang Diterapkan dalam Kode Pencarian Harta Karun
Program Pencarian Harta Karun ini melibatkan berbagai konsep dasar dalam pemrograman. Di bawah ini adalah penjelasan tentang materi-materi yang diterapkan dalam kode tersebut:

1. Conditional Statements (Pernyataan Kondisional)
- Materi yang Diterapkan:
Program menggunakan conditional statements untuk memeriksa kondisi tertentu dan mengambil keputusan berdasarkan hasil pemeriksaan tersebut. Kondisional yang paling sering digunakan dalam kode ini adalah if dan else.

- Implementasi dalam Kode:
Di dalam metode mulai_permainan(), kondisional digunakan untuk mengecek apakah tebakan pemain sesuai dengan lokasi harta karun atau tidak.

if validasi_jawaban(jawaban, self.pola):
    print("Selamat! Kamu menemukan harta karun!")
    break
else:
    kesempatan -= 1
    print("Tebakan salah. Coba lagi.")
   
Kondisional ini memeriksa apakah jawaban pemain sesuai dengan pola yang ditentukan (lokasi harta karun). Jika benar, permainan berakhir dengan kemenangan, jika tidak, pemain diberikan kesempatan untuk menebak lagi.

2. Looping (Perulangan)
- Materi yang Diterapkan:
Program menggunakan looping untuk memberikan pemain kesempatan untuk menebak beberapa kali (maksimal 3 kali). Jika tebakan salah, pemain masih memiliki kesempatan untuk mencoba lagi.

- Implementasi dalam Kode:
Dalam fungsi mulai_permainan(), digunakan while loop untuk memeriksa apakah pemain masih memiliki kesempatan untuk menebak. Loop ini akan berhenti ketika pemain berhasil menebak dengan benar atau kehabisan kesempatan.

while kesempatan > 0:
    jawaban = input(f"\nTebakanmu (kesempatan tersisa {kesempatan}): ").strip().lower()
    if validasi_jawaban(jawaban, self.pola):
        print("Selamat! Kamu menemukan harta karun!")
        break
    else:
        kesempatan -= 1
        print("Tebakan salah. Coba lagi.")
   
3. Functions (Fungsi)
- Materi yang Diterapkan:
Fungsi adalah konsep dasar dalam pemrograman untuk mengelompokkan kode yang memiliki tujuan tertentu. Dalam kode ini, berbagai fungsi dibuat untuk mengelola logika permainan.

- Implementasi dalam Kode:
Fungsi-fungsi seperti buat_petunjuk(), lokasi_harta_karun(), dan beri_petunjuk_tambahan() masing-masing memiliki tujuan spesifik. Misalnya, buat_petunjuk() menghasilkan petunjuk secara acak, dan lokasi_harta_karun() menentukan lokasi harta karun.

def buat_petunjuk():
    petunjuk = [
        "Harta karun terletak di dekat pohon oak tua.",
        "Cari di bawah patung burung elang.",
        "Harta karun ada di bawah pasir di pantai.",
        "Cari di gua utara di balik air terjun.",
        "Harta karun tersembunyi di dalam peti tua di perpustakaan."
    ]
    return random.choice(petunjuk)

4. String Manipulation (Manipulasi String)
- Materi yang Diterapkan:
Manipulasi string adalah proses memodifikasi atau memanipulasi data berbentuk string. Dalam program ini, manipulasi string dilakukan untuk memastikan jawaban pemain tidak terpengaruh oleh spasi atau kapitalisasi huruf.

- Implementasi dalam Kode:
Program menggunakan strip() untuk menghapus spasi ekstra pada input pemain dan lower() untuk mengubah input menjadi huruf kecil, yang memastikan validasi jawaban dapat dilakukan dengan konsisten.

jawaban = input(f"\nTebakanmu (kesempatan tersisa {kesempatan}): ").strip().lower()

5. Regular Expressions (RegEx)
- Materi yang Diterapkan:
RegEx (Regular Expressions) digunakan untuk mencocokkan pola tertentu dalam string. Pada kode ini, RegEx digunakan untuk memeriksa apakah jawaban pemain sesuai dengan pola yang tepat (lokasi harta karun).

- Implementasi dalam Kode:
Fungsi validasi_jawaban() menggunakan re.match() untuk mencocokkan input pemain dengan pola yang sudah ditentukan untuk lokasi harta karun.

def validasi_jawaban(jawaban, pola):
    return re.match(pola, jawaban, re.IGNORECASE)
   
6. Object-Oriented Programming (OOP)
-Materi yang Diterapkan:
Object-Oriented Programming (OOP) adalah paradigma pemrograman yang mengorganisir kode dalam objek dan kelas. Dalam program ini, kelas PermainanPencarianHarta mengelola logika permainan, termasuk lokasi harta karun, petunjuk, dan proses permainan.
Implementasi dalam Kode:

- Program ini mengimplementasikan OOP dengan mendefinisikan kelas PermainanPencarianHarta yang memiliki atribut dan metode terkait permainan. Misalnya, self.lokasi_harta adalah atribut untuk menyimpan lokasi harta karun yang dipilih, dan self.mulai_permainan() adalah metode untuk memulai permainan.

class PermainanPencarianHarta:
    def __init__(self):
        self.lokasi_harta = lokasi_harta_karun()
        self.petunjuk = buat_petunjuk()
        self.pola = re.escape(self.lokasi_harta)
        
7. Data Types (Tipe Data)
- Materi yang Diterapkan:
Tipe data merujuk pada jenis data yang digunakan dalam program, seperti string, integer, dan list. Di dalam kode ini, berbagai tipe data digunakan untuk menyimpan informasi seperti lokasi harta karun, petunjuk, dan kesempatan tebakan.
Implementasi dalam Kode:

- List digunakan untuk menyimpan berbagai lokasi dan petunjuk yang dipilih secara acak.
String digunakan untuk menyimpan input dari pemain dan petunjuk yang ditampilkan.
Integer digunakan untuk menyimpan jumlah kesempatan yang tersisa bagi pemain.

lokasi = ["pohon oak tua", "patung burung elang", "pantai", "gua utara", "peti tua di perpustakaan"]
kesempatan = 3

# Kesimpulan
Program Pencarian Harta Karun ini menggabungkan berbagai konsep dasar pemrograman seperti Object-Oriented Programming (OOP), RegEx, looping, conditional statements, string manipulation, dan data types untuk menciptakan permainan yang interaktif dan menyenangkan. Dengan menggunakan OOP, program ini mengorganisir logika permainan dalam kelas, membuat kode lebih terstruktur dan mudah dikembangkan. Pemain diberikan kesempatan untuk menebak lokasi harta karun berdasarkan petunjuk yang diberikan, dan program memanfaatkan RegEx untuk memvalidasi jawaban pemain, memastikan input yang dimasukkan sesuai dengan format yang benar. Program ini juga menerapkan looping untuk memberikan beberapa kesempatan tebakan, dan conditional statements untuk mengontrol alur permainan, misalnya menentukan apakah tebakan benar atau salah. Fungsi-fungsi dalam program ini membantu modularisasi kode, membuatnya lebih mudah dipahami dan dikembangkan. Secara keseluruhan, permainan ini tidak hanya menghibur tetapi juga memperlihatkan penerapan praktis dari teknik-teknik pemrograman dasar yang penting.
