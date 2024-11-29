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

# Kesimpulan
Program Pencarian Harta Karun ini adalah contoh permainan interaktif yang menggunakan berbagai konsep pemrograman seperti RegEx, OOP, dan looping. Dengan mekanisme permainan yang menantang dan fitur-fitur seperti petunjuk tambahan dan validasi jawaban, program ini memberikan pengalaman yang menyenangkan dan mendidik. Pemain bisa belajar sambil bermain, sekaligus mengasah keterampilan pemrograman seperti penggunaan ekspresi reguler dan pemrograman berorientasi objek.
