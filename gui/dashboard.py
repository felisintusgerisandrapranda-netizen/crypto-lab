"""
Dashboard
CRYPTO LAB
Aplikasi Kriptografi Klasik
"""

import tkinter as tk


class DashboardPage(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(
            parent,
            bg="#F4F7FB"
        )

        self.controller = controller

        self.create_header()
        self.create_welcome()
        self.create_algorithm_cards()
        self.create_bottom_cards()
        self.create_footer()

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
            padx=45,
            pady=(30, 10)
        )

        tk.Label(
            header,
            text="🔐 CRYPTO LAB",
            font=("Segoe UI", 28, "bold"),
            bg="#F4F7FB",
            fg="#0F172A"
        ).pack(anchor="w")

        tk.Label(
            header,
            text="KRIPTOGRAFI KLASIK",
            font=("Segoe UI", 11, "bold"),
            bg="#F4F7FB",
            fg="#2563EB"
        ).pack(
            anchor="w",
            pady=(2, 0)
        )

        tk.Label(
            header,
            text="Belajar • Mengenkripsi • Mendekripsi • Memahami Algoritma",
            font=("Segoe UI", 10),
            bg="#F4F7FB",
            fg="#64748B"
        ).pack(
            anchor="w",
            pady=(4, 0)
        )

    # ==================================================
    # WELCOME
    # ==================================================

    def create_welcome(self):

        card = tk.Frame(
            self,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        card.pack(
            fill="x",
            padx=45,
            pady=15
        )

        content = tk.Frame(
            card,
            bg="#FFFFFF"
        )

        content.pack(
            fill="x",
            padx=28,
            pady=22
        )

        tk.Label(
            content,
            text="👋",
            font=("Segoe UI Emoji", 28),
            bg="#FFFFFF"
        ).pack(
            side="left",
            padx=(0, 18)
        )

        text_frame = tk.Frame(
            content,
            bg="#FFFFFF"
        )

        text_frame.pack(
            side="left",
            fill="x",
            expand=True
        )

        tk.Label(
            text_frame,
            text="Selamat Datang di Crypto Lab",
            font=("Segoe UI", 17, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        ).pack(anchor="w")

        tk.Label(
            text_frame,
            text=(
                "Aplikasi pembelajaran kriptografi klasik untuk "
                "mempelajari proses enkripsi, dekripsi, dan "
                "langkah perhitungan algoritma."
            ),
            font=("Segoe UI", 10),
            bg="#FFFFFF",
            fg="#64748B",
            justify="left"
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

    # ==================================================
    # ALGORITHM CARDS
    # ==================================================

    def create_algorithm_cards(self):

        tk.Label(
            self,
            text="Algoritma Kriptografi",
            font=("Segoe UI", 17, "bold"),
            bg="#F4F7FB",
            fg="#0F172A"
        ).pack(
            anchor="w",
            padx=45,
            pady=(5, 0)
        )

        tk.Label(
            self,
            text="Pilih algoritma yang ingin dipelajari.",
            font=("Segoe UI", 10),
            bg="#F4F7FB",
            fg="#64748B"
        ).pack(
            anchor="w",
            padx=45,
            pady=(2, 8)
        )

        cards = tk.Frame(
            self,
            bg="#F4F7FB"
        )

        cards.pack(
            fill="x",
            padx=38
        )

        cards.grid_columnconfigure(0, weight=1)
        cards.grid_columnconfigure(1, weight=1)
        cards.grid_columnconfigure(2, weight=1)

        self.create_algorithm_card(
            cards,
            0,
            "🔢",
            "CAESAR CIPHER",
            "Substitusi Monoalfabetik",
            "Menggeser setiap huruf berdasarkan nilai kunci.",
            "C = (P + k) mod 26",
            "caesar"
        )

        self.create_algorithm_card(
            cards,
            1,
            "🔑",
            "VIGENÈRE CIPHER",
            "Substitusi Polialfabetik",
            "Menggunakan kata kunci untuk menghasilkan pergeseran.",
            "C = (P + K) mod 26",
            "vigenere"
        )

        self.create_algorithm_card(
            cards,
            2,
            "🔀",
            "COLUMNAR",
            "Transposisi Kolom",
            "Mengubah posisi karakter berdasarkan susunan kolom.",
            "Grid → Urutan → Ciphertext",
            "columnar"
        )

    # ==================================================
    # CARD
    # ==================================================

    def create_algorithm_card(
        self,
        parent,
        column,
        icon,
        title,
        subtitle,
        description,
        formula,
        page
    ):

        card = tk.Frame(
            parent,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=7
        )

        content = tk.Frame(
            card,
            bg="#FFFFFF"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=18
        )

        tk.Label(
            content,
            text=icon,
            font=("Segoe UI Emoji", 24),
            bg="#FFFFFF"
        ).pack(anchor="w")

        tk.Label(
            content,
            text=title,
            font=("Segoe UI", 13, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        ).pack(
            anchor="w",
            pady=(8, 0)
        )

        tk.Label(
            content,
            text=subtitle,
            font=("Segoe UI", 9, "bold"),
            bg="#FFFFFF",
            fg="#2563EB"
        ).pack(
            anchor="w"
        )

        tk.Label(
            content,
            text=description,
            font=("Segoe UI", 9),
            bg="#FFFFFF",
            fg="#64748B",
            justify="left",
            wraplength=280
        ).pack(
            anchor="w",
            pady=(10, 10)
        )

        formula_frame = tk.Frame(
            content,
            bg="#EFF6FF"
        )

        formula_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        tk.Label(
            formula_frame,
            text=formula,
            font=("Consolas", 9, "bold"),
            bg="#EFF6FF",
            fg="#1D4ED8"
        ).pack(
            pady=7
        )

        tk.Button(
            content,
            text="BUKA ALGORITMA  →",
            font=("Segoe UI", 9, "bold"),
            bg="#2563EB",
            fg="#FFFFFF",
            activebackground="#1D4ED8",
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda: self.controller.show_page(page)
        ).pack(
            fill="x"
        )

    # ==================================================
    # BOTTOM
    # ==================================================

    def create_bottom_cards(self):

        frame = tk.Frame(
            self,
            bg="#F4F7FB"
        )

        frame.pack(
            fill="x",
            padx=45,
            pady=(18, 8)
        )

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        self.create_bottom_card(
            frame,
            0,
            "📚",
            "Teori & Panduan",
            "Pelajari konsep dasar kriptografi klasik.",
            "PELAJARI",
            "theory"
        )

        self.create_bottom_card(
            frame,
            1,
            "ℹ️",
            "Tentang Aplikasi",
            "Informasi mengenai Crypto Lab dan project.",
            "LIHAT INFO",
            "about"
        )

    # ==================================================
    # BOTTOM CARD
    # ==================================================

    def create_bottom_card(
        self,
        parent,
        column,
        icon,
        title,
        description,
        button_text,
        page
    ):

        card = tk.Frame(
            parent,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=column,
            sticky="ew",
            padx=6
        )

        content = tk.Frame(
            card,
            bg="#FFFFFF"
        )

        content.pack(
            fill="x",
            padx=20,
            pady=13
        )

        tk.Label(
            content,
            text=icon,
            font=("Segoe UI Emoji", 21),
            bg="#FFFFFF"
        ).pack(
            side="left",
            padx=(0, 12)
        )

        text = tk.Frame(
            content,
            bg="#FFFFFF"
        )

        text.pack(
            side="left",
            fill="x",
            expand=True
        )

        tk.Label(
            text,
            text=title,
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        ).pack(anchor="w")

        tk.Label(
            text,
            text=description,
            font=("Segoe UI", 9),
            bg="#FFFFFF",
            fg="#64748B"
        ).pack(
            anchor="w",
            pady=(2, 5)
        )

        tk.Button(
            text,
            text=button_text,
            font=("Segoe UI", 9, "bold"),
            bg="#EFF6FF",
            fg="#1D4ED8",
            activebackground="#DBEAFE",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda: self.controller.show_page(page)
        ).pack(anchor="w")

    # ==================================================
    # FOOTER
    # ==================================================

    def create_footer(self):

        footer = tk.Frame(
            self,
            bg="#F4F7FB"
        )

        footer.pack(
            fill="x",
            padx=45,
            pady=(5, 12)
        )

        tk.Label(
            footer,
            text="CRYPTO LAB • Aplikasi Pembelajaran Kriptografi Klasik",
            font=("Segoe UI", 8),
            bg="#F4F7FB",
            fg="#94A3B8"
        ).pack(side="left")

        tk.Label(
            footer,
            text="Python • Tkinter",
            font=("Segoe UI", 8),
            bg="#F4F7FB",
            fg="#94A3B8"
        ).pack(side="right")

    def refresh_page(self):
        pass