"""
Theory & Guide
CRYPTO LAB
"""

import tkinter as tk


class TheoryPage(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(
            parent,
            bg="#F4F7FB"
        )

        self.controller = controller

        self.create_header()
        self.create_content()

    # ==================================================
    # HEADER
    # ==================================================

    def create_header(self):

        header = tk.Frame(
            self,
            bg="#F4F7FB"
        )

        header.pack(
            fill="x",
            padx=35,
            pady=(22, 10)
        )

        tk.Button(
            header,
            text="← Dashboard",
            font=("Segoe UI", 9, "bold"),
            bg="#E2E8F0",
            fg="#334155",
            activebackground="#CBD5E1",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda: self.controller.show_page("dashboard")
        ).pack(side="left")

        title = tk.Frame(
            header,
            bg="#F4F7FB"
        )

        title.pack(
            side="left",
            padx=20
        )

        tk.Label(
            title,
            text="📚 TEORI & PANDUAN",
            font=("Segoe UI", 23, "bold"),
            bg="#F4F7FB",
            fg="#0F172A"
        ).pack(anchor="w")

        tk.Label(
            title,
            text="Materi Dasar Kriptografi Klasik",
            font=("Segoe UI", 10),
            bg="#F4F7FB",
            fg="#2563EB"
        ).pack(anchor="w")

    # ==================================================
    # CONTENT
    # ==================================================

    def create_content(self):

        outer = tk.Frame(
            self,
            bg="#F4F7FB"
        )

        outer.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=5
        )

        self.text = tk.Text(
            outer,
            font=("Segoe UI", 10),
            bg="#FFFFFF",
            fg="#334155",
            relief="solid",
            bd=1,
            wrap="word",
            padx=25,
            pady=20
        )

        self.text.pack(
            fill="both",
            expand=True
        )

        self.insert_theory()

        self.text.config(
            state="disabled"
        )

    # ==================================================
    # THEORY
    # ==================================================

    def insert_theory(self):

        content = """
CRYPTO LAB
TEORI & PANDUAN KRIPTOGRAFI KLASIK

============================================================

1. PENGERTIAN KRIPTOGRAFI
============================================================

Kriptografi adalah ilmu dan teknik untuk mengamankan
informasi dengan mengubah plaintext menjadi bentuk yang
tidak mudah dipahami oleh pihak yang tidak berwenang.

Beberapa istilah penting:

• Plaintext
  Pesan asli sebelum dilakukan enkripsi.

• Ciphertext
  Pesan yang sudah melalui proses enkripsi.

• Enkripsi
  Proses mengubah plaintext menjadi ciphertext.

• Dekripsi
  Proses mengembalikan ciphertext menjadi plaintext.

• Key / Kunci
  Nilai yang digunakan dalam proses enkripsi dan dekripsi.


============================================================

2. CAESAR CIPHER
============================================================

Caesar Cipher merupakan algoritma substitusi sederhana.

Setiap huruf digeser berdasarkan nilai kunci.

Contoh:

Plaintext : HALO
Kunci     : 3

H → K
A → D
L → O
O → R

Hasil:

KDOR

Rumus:

C = (P + k) mod 26

Dekripsi:

P = (C - k) mod 26


Keterangan:

P = nilai plaintext
C = nilai ciphertext
k = nilai kunci


============================================================

3. VIGENÈRE CIPHER
============================================================

Vigenère Cipher merupakan algoritma substitusi
polialfabetik.

Algoritma ini menggunakan kata kunci.

Contoh:

Plaintext : KRIPTOGRAFI
Key       : LAMPION

Kunci akan diulang apabila lebih pendek dari plaintext.

Rumus enkripsi:

C = (P + K) mod 26

Rumus dekripsi:

P = (C - K) mod 26


Kelebihan utama dibandingkan Caesar adalah setiap huruf
dapat menggunakan pergeseran yang berbeda berdasarkan
huruf kunci.


============================================================

4. COLUMNAR TRANSPOSITION
============================================================

Columnar Transposition merupakan teknik transposisi.

Berbeda dengan Caesar dan Vigenère yang mengubah nilai
huruf, Columnar Transposition mengubah posisi huruf.

Contoh key:

TOMBAK

Urutan alfabet:

T O M B A K
6 5 4 2 1 3

Plaintext:

SISTEMINFORMASI

Disusun ke dalam grid:

T | O | M | B | A | K
S | I | S | T | E | M
I | N | F | O | R | M
A | S | I |   |   |

Kemudian kolom dibaca berdasarkan urutan:

1 → A
2 → B
3 → K
4 → M
5 → O
6 → T


============================================================

5. PERBEDAAN ALGORITMA
============================================================

CAESAR

Jenis:
Substitusi monoalfabetik

Kunci:
Angka 0–25

Konsep:
Menggeser huruf.


VIGENÈRE

Jenis:
Substitusi polialfabetik

Kunci:
Kata / huruf

Konsep:
Pergeseran berdasarkan kata kunci.


COLUMNAR

Jenis:
Transposisi

Kunci:
Kata dengan huruf berbeda

Konsep:
Mengubah posisi karakter.


============================================================

6. ALUR UMUM ENKRIPSI
============================================================

Plaintext
     ↓
Input Kunci
     ↓
Algoritma Kriptografi
     ↓
Ciphertext
     ↓
Hasil


============================================================

7. ALUR UMUM DEKRIPSI
============================================================

Ciphertext
     ↓
Input Kunci
     ↓
Algoritma Dekripsi
     ↓
Plaintext
     ↓
Pesan Asli


============================================================

8. CATATAN PENTING
============================================================

Aplikasi Crypto Lab dibuat untuk tujuan pembelajaran.

Algoritma klasik seperti Caesar, Vigenère, dan Columnar
merupakan materi dasar kriptografi dan tidak dimaksudkan
sebagai pengganti algoritma kriptografi modern untuk
keamanan sistem nyata.


============================================================

CRYPTO LAB
Belajar • Mengenkripsi • Memahami Algoritma
============================================================
"""

        self.text.insert(
            tk.END,
            content
        )

    def refresh_page(self):
        pass