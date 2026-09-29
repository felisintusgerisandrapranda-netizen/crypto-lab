# 🔐 Crypto Lab

## Aplikasi Kriptografi Klasik Berbasis Python

Crypto Lab adalah aplikasi desktop untuk mempelajari dan melakukan proses enkripsi serta dekripsi menggunakan algoritma kriptografi klasik.

Aplikasi ini dibuat menggunakan Python dan Tkinter dengan antarmuka desktop yang sederhana dan mudah digunakan.

---

## 📌 Fitur

Crypto Lab menyediakan tiga algoritma kriptografi klasik:

### 1. Caesar Cipher
Algoritma substitusi sederhana yang melakukan pergeseran posisi huruf berdasarkan nilai kunci.

Rumus enkripsi:

C = (P + k) mod 26

Rumus dekripsi:

P = (C - k) mod 26

---

### 2. Vigenère Cipher

Vigenère Cipher menggunakan sebuah kata kunci untuk melakukan substitusi terhadap plaintext.

Rumus enkripsi:

C = (P + K) mod 26

Rumus dekripsi:

P = (C - K) mod 26

---

### 3. Columnar Transposition Cipher

Columnar Transposition Cipher melakukan perubahan posisi karakter berdasarkan urutan alfabet dari kata kunci.

Contoh kunci:

TOMBAK

Urutan kolom:

6 5 4 2 1 3

---

## 🎯 Tujuan

Project ini dibuat sebagai media pembelajaran untuk memahami konsep:

- Kriptografi klasik
- Enkripsi
- Dekripsi
- Plaintext
- Ciphertext
- Kunci
- Substitusi
- Transposisi
- Proses perhitungan algoritma

---

## 🖥️ Teknologi

Project ini menggunakan:

- Python
- Tkinter
- Object-Oriented Programming
- Modular Programming
- Git
- GitHub

---

## 📂 Struktur Project

```text
crypto-lab/
│
├── main.py
├── test_algorithms.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── algorithms/
│   ├── __init__.py
│   ├── caesar.py
│   ├── vigenere.py
│   └── columnar.py
│
├── gui/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── caesar_page.py
│   ├── vigenere_page.py
│   ├── columnar_page.py
│   ├── theory_page.py
│   └── about_page.py
│
├── utils/
│   ├── __init__.py
│   ├── clipboard.py
│   ├── file_handler.py
│   └── validator.py
│
└── hasil/
