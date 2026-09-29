"""
About Page
CRYPTO LAB
"""

import tkinter as tk


class AboutPage(tk.Frame):

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
            text="ℹ️ TENTANG CRYPTO LAB",
            font=("Segoe UI", 23, "bold"),
            bg="#F4F7FB",
            fg="#0F172A"
        ).pack(anchor="w")

        tk.Label(
            title,
            text="Informasi Aplikasi",
            font=("Segoe UI", 10),
            bg="#F4F7FB",
            fg="#2563EB"
        ).pack(anchor="w")

    # ==================================================
    # CONTENT
    # ==================================================

    def create_content(self):

        main = tk.Frame(
            self,
            bg="#F4F7FB"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=5
        )

        # ==================================================
        # HERO
        # ==================================================

        hero = tk.Frame(
            main,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        hero.pack(
            fill="x",
            pady=(0, 12)
        )

        tk.Label(
            hero,
            text="🔐",
            font=("Segoe UI Emoji", 45),
            bg="#FFFFFF"
        ).pack(
            pady=(25, 5)
        )

        tk.Label(
            hero,
            text="CRYPTO LAB",
            font=("Segoe UI", 24, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        ).pack()

        tk.Label(
            hero,
            text="APLIKASI PEMBELAJARAN KRIPTOGRAFI KLASIK",
            font=("Segoe UI", 10, "bold"),
            bg="#FFFFFF",
            fg="#2563EB"
        ).pack(
            pady=(2, 5)
        )

        tk.Label(
            hero,
            text=(
                "Aplikasi desktop berbasis Python dan Tkinter "
                "untuk mempelajari algoritma kriptografi klasik."
            ),
            font=("Segoe UI", 10),
            bg="#FFFFFF",
            fg="#64748B"
        ).pack(
            pady=(0, 25)
        )

        # ==================================================
        # INFORMATION
        # ==================================================

        cards = tk.Frame(
            main,
            bg="#F4F7FB"
        )

        cards.pack(
            fill="both",
            expand=True
        )

        cards.grid_columnconfigure(0, weight=1)
        cards.grid_columnconfigure(1, weight=1)
        cards.grid_rowconfigure(0, weight=1)

        self.create_info_card(
            cards,
            0,
            "🎯 Tujuan",
            (
                "Membantu mahasiswa memahami konsep dasar "
                "kriptografi klasik melalui implementasi "
                "yang interaktif dan mudah digunakan."
            )
        )

        self.create_info_card(
            cards,
            1,
            "🧩 Algoritma",
            (
                "Crypto Lab menyediakan tiga algoritma: "
                "Caesar Cipher, Vigenère Cipher, dan "
                "Columnar Transposition."
            )
        )

        self.create_info_card(
            cards,
            2,
            "💻 Teknologi",
            (
                "Aplikasi dibuat menggunakan Python 3 "
                "dan Tkinter tanpa membutuhkan library "
                "eksternal tambahan."
            ),
            row=1
        )

        self.create_info_card(
            cards,
            3,
            "📖 Fitur Pembelajaran",
            (
                "Selain menghasilkan ciphertext, aplikasi "
                "menampilkan langkah perhitungan sehingga "
                "proses algoritma dapat dipelajari."
            ),
            row=1
        )

        # ==================================================
        # FOOTER
        # ==================================================

        tk.Label(
            main,
            text=(
                "CRYPTO LAB • Kriptografi Klasik • "
                "Python + Tkinter"
            ),
            font=("Segoe UI", 9),
            bg="#F4F7FB",
            fg="#94A3B8"
        ).pack(
            pady=12
        )

    # ==================================================
    # INFO CARD
    # ==================================================

    def create_info_card(
        self,
        parent,
        column,
        title,
        description,
        row=0
    ):

        card = tk.Frame(
            parent,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=6,
            pady=6
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        ).pack(
            anchor="w",
            padx=18,
            pady=(18, 8)
        )

        tk.Label(
            card,
            text=description,
            font=("Segoe UI", 9),
            bg="#FFFFFF",
            fg="#64748B",
            wraplength=380,
            justify="left"
        ).pack(
            anchor="w",
            padx=18,
            pady=(0, 18)
        )

    def refresh_page(self):
        pass