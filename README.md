# Implementasi Algoritma Backtracking: Sudoku Solver

Tugas individu untuk mata kuliah Algoritma dan Pemrograman. Project ini mengimplementasikan algoritma **Backtracking** untuk menyelesaikan permainan Sudoku menggunakan bahasa pemrograman Python.

## 📌 Deskripsi Tugas
Algoritma Backtracking adalah teknik pencarian solusi secara incremental (satu per satu) dengan mengeliminasi solusi yang tidak sesuai dengan batasan (constraint) yang ditentukan. 

Dalam kasus Sudoku, batasan yang harus dipenuhi adalah:
1. Satu kuadran $3 \times 3$ tidak boleh memiliki angka yang sama.
2. Satu baris tidak boleh memiliki angka yang sama.
3. Satu kolom tidak boleh memiliki angka yang sama.

## 🚀 Fitur Utama
* **Visualisasi CLI:** Menampilkan langkah-langkah penyelesaian masalah secara real-time di terminal.
* **Mekanisme Backtracking:** Jika program menemui jalan buntu (unsolved), program akan mengosongkan cell dan kembali ke percabangan sebelumnya untuk mencoba angka lain.

## 🛠️ Cara Menjalankan
1. Pastikan Anda sudah menginstal Python di perangkat Anda.
2. Clone repository ini:
   ```bash
   git clone [https://github.com/revansyahfaris/TugasAlpro_AlgoritmaBacktracking.git](https://github.com/revansyahfaris/TugasAlpro_AlgoritmaBacktracking.git)
