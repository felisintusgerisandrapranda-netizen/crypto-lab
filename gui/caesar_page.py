"""
Caesar Cipher GUI
CRYPTO LAB
"""

import tkinter as tk
from tkinter import messagebox

from algorithms.caesar import (
    caesar_encrypt,
    caesar_decrypt,
    caesar_steps
)

from utils.validator import (
    validate_text,
    validate_caesar_key
)

from utils.clipboard import (
    copy_widget_content
)

from utils.file_handler import (
    save_result
)


class CaesarPage(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(
            parent,
            bg="#F4F7FB"
        )

        self.controller = controller

        self.create_header()
        self.create_main_content()

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
            pady=(22, 8)
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
        ).pack(
            side="left"
        )

        title_frame = tk.Frame(
            header,
            bg="#F4F7FB"
        )

        title_frame.pack(
            side="left",
            padx=20
        )

        tk.Label(
            title_frame,
            text="🔢 CAESAR CIPHER",
            font=("Segoe UI", 23, "bold"),
            bg="#F4F7FB",
            fg="#0F172A"
        ).pack(anchor="w")

        tk.Label(
            title_frame,
            text="Substitusi Monoalfabetik",
            font=("Segoe UI", 10),
            bg="#F4F7FB",
            fg="#2563EB"
        ).pack(anchor="w")

    # ==================================================
    # MAIN
    # ==================================================

    def create_main_content(self):

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

        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(1, weight=1)

        # ------------------------------------------
        # INPUT CARD
        # ------------------------------------------

        input_card = tk.Frame(
            main,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        input_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 7),
            pady=5
        )

        tk.Label(
            input_card,
            text="INPUT & KUNCI",
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 5)
        )

        tk.Label(
            input_card,
            text="Pesan / Ciphertext",
            font=("Segoe UI", 9, "bold"),
            bg="#FFFFFF",
            fg="#475569"
        ).pack(
            anchor="w",
            padx=18
        )

        self.input_text = tk.Text(
            input_card,
            height=7,
            font=("Consolas", 11),
            bg="#F8FAFC",
            fg="#0F172A",
            relief="solid",
            bd=1,
            wrap="word"
        )

        self.input_text.pack(
            fill="x",
            padx=18,
            pady=(5, 12)
        )

        key_frame = tk.Frame(
            input_card,
            bg="#FFFFFF"
        )

        key_frame.pack(
            fill="x",
            padx=18
        )

        tk.Label(
            key_frame,
            text="Kunci (0–25)",
            font=("Segoe UI", 9, "bold"),
            bg="#FFFFFF",
            fg="#475569"
        ).pack(
            side="left"
        )

        self.key_entry = tk.Entry(
            key_frame,
            width=10,
            font=("Consolas", 11),
            relief="solid",
            bd=1
        )

        self.key_entry.pack(
            side="left",
            padx=10
        )

        tk.Label(
            key_frame,
            text="Contoh: 3",
            font=("Segoe UI", 8),
            bg="#FFFFFF",
            fg="#94A3B8"
        ).pack(
            side="left"
        )

        # BUTTONS

        button_frame = tk.Frame(
            input_card,
            bg="#FFFFFF"
        )

        button_frame.pack(
            fill="x",
            padx=18,
            pady=15
        )

        tk.Button(
            button_frame,
            text="🔒 ENKRIPSI",
            font=("Segoe UI", 9, "bold"),
            bg="#2563EB",
            fg="#FFFFFF",
            activebackground="#1D4ED8",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.encrypt_action
        ).pack(
            side="left",
            padx=(0, 6)
        )

        tk.Button(
            button_frame,
            text="🔓 DEKRIPSI",
            font=("Segoe UI", 9, "bold"),
            bg="#16A34A",
            fg="#FFFFFF",
            activebackground="#15803D",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.decrypt_action
        ).pack(
            side="left",
            padx=6
        )

        tk.Button(
            button_frame,
            text="🧹 BERSIHKAN",
            font=("Segoe UI", 9, "bold"),
            bg="#E2E8F0",
            fg="#334155",
            activebackground="#CBD5E1",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.clear_action
        ).pack(
            side="left",
            padx=6
        )

        # ------------------------------------------
        # INFO CARD
        # ------------------------------------------

        info = tk.Frame(
            input_card,
            bg="#EFF6FF"
        )

        info.pack(
            fill="x",
            padx=18,
            pady=(0, 15)
        )

        tk.Label(
            info,
            text="Rumus Enkripsi",
            font=("Segoe UI", 9, "bold"),
            bg="#EFF6FF",
            fg="#1D4ED8"
        ).pack(
            anchor="w",
            padx=12,
            pady=(8, 0)
        )

        tk.Label(
            info,
            text="C = (P + k) mod 26",
            font=("Consolas", 11, "bold"),
            bg="#EFF6FF",
            fg="#0F172A"
        ).pack(
            anchor="w",
            padx=12,
            pady=(2, 8)
        )

        # ------------------------------------------
        # RESULT CARD
        # ------------------------------------------

        result_card = tk.Frame(
            main,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        result_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(7, 0),
            pady=5
        )

        tk.Label(
            result_card,
            text="HASIL",
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 5)
        )

        self.result_text = tk.Text(
            result_card,
            height=8,
            font=("Consolas", 12, "bold"),
            bg="#F8FAFC",
            fg="#0F172A",
            relief="solid",
            bd=1,
            wrap="word"
        )

        self.result_text.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=(0, 10)
        )

        result_buttons = tk.Frame(
            result_card,
            bg="#FFFFFF"
        )

        result_buttons.pack(
            fill="x",
            padx=18,
            pady=(0, 15)
        )

        tk.Button(
            result_buttons,
            text="📋 COPY",
            font=("Segoe UI", 9, "bold"),
            bg="#E0F2FE",
            fg="#0369A1",
            activebackground="#BAE6FD",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.copy_result
        ).pack(
            side="left",
            padx=(0, 6)
        )

        tk.Button(
            result_buttons,
            text="💾 SIMPAN TXT",
            font=("Segoe UI", 9, "bold"),
            bg="#DCFCE7",
            fg="#166534",
            activebackground="#BBF7D0",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.save_result_file
        ).pack(
            side="left",
            padx=6
        )

        # ------------------------------------------
        # PROCESS
        # ------------------------------------------

        process_card = tk.Frame(
            main,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        process_card.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew",
            pady=(10, 0)
        )

        process_header = tk.Frame(
            process_card,
            bg="#FFFFFF"
        )

        process_header.pack(
            fill="x"
        )

        tk.Label(
            process_header,
            text="🧮 LANGKAH PERHITUNGAN",
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        ).pack(
            side="left",
            padx=18,
            pady=12
        )

        self.status_label = tk.Label(
            process_header,
            text="Siap digunakan",
            font=("Segoe UI", 9),
            bg="#FFFFFF",
            fg="#16A34A"
        )

        self.status_label.pack(
            side="right",
            padx=18
        )

        self.process_text = tk.Text(
            process_card,
            font=("Consolas", 9),
            bg="#0F172A",
            fg="#E2E8F0",
            insertbackground="#FFFFFF",
            relief="flat",
            bd=0,
            wrap="none"
        )

        self.process_text.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 12)
        )

        self.show_initial_process()

    # ==================================================
    # ACTION
    # ==================================================

    def get_input_and_key(self):

        text = self.input_text.get(
            "1.0",
            tk.END
        ).rstrip("\n")

        key = self.key_entry.get()

        text = validate_text(
            text,
            "Pesan"
        )

        key = validate_caesar_key(
            key
        )

        return text, key

    def encrypt_action(self):

        try:

            text, key = self.get_input_and_key()

            result = caesar_encrypt(
                text,
                key
            )

            steps = caesar_steps(
                text,
                key,
                decrypt=False
            )

            self.set_result(
                result,
                steps
            )

            self.status_label.config(
                text="✓ Enkripsi berhasil",
                fg="#16A34A"
            )

        except ValueError as error:

            messagebox.showerror(
                "Input Tidak Valid",
                str(error)
            )

    def decrypt_action(self):

        try:

            text, key = self.get_input_and_key()

            result = caesar_decrypt(
                text,
                key
            )

            steps = caesar_steps(
                text,
                key,
                decrypt=True
            )

            self.set_result(
                result,
                steps
            )

            self.status_label.config(
                text="✓ Dekripsi berhasil",
                fg="#16A34A"
            )

        except ValueError as error:

            messagebox.showerror(
                "Input Tidak Valid",
                str(error)
            )

    # ==================================================
    # RESULT
    # ==================================================

    def set_result(
        self,
        result,
        steps
    ):

        self.result_text.delete(
            "1.0",
            tk.END
        )

        self.result_text.insert(
            tk.END,
            result
        )

        self.process_text.delete(
            "1.0",
            tk.END
        )

        self.process_text.insert(
            tk.END,
            steps
        )

    # ==================================================
    # COPY
    # ==================================================

    def copy_result(self):

        try:

            copy_widget_content(
                self.result_text
            )

            messagebox.showinfo(
                "Berhasil",
                "Hasil berhasil disalin ke clipboard."
            )

        except ValueError as error:

            messagebox.showwarning(
                "Tidak Ada Hasil",
                str(error)
            )

    # ==================================================
    # SAVE
    # ==================================================

    def save_result_file(self):

        result = self.result_text.get(
            "1.0",
            tk.END
        ).strip()

        text = self.input_text.get(
            "1.0",
            tk.END
        ).strip()

        key = self.key_entry.get().strip()

        if not result:

            messagebox.showwarning(
                "Tidak Ada Hasil",
                "Lakukan enkripsi atau dekripsi terlebih dahulu."
            )

            return

        try:

            path = save_result(
                text,
                key,
                result,
                "Caesar Cipher",
                "Enkripsi / Dekripsi"
            )

            if path:

                messagebox.showinfo(
                    "Berhasil",
                    f"Hasil berhasil disimpan:\n\n{path}"
                )

        except ValueError as error:

            messagebox.showerror(
                "Gagal Menyimpan",
                str(error)
            )

    # ==================================================
    # CLEAR
    # ==================================================

    def clear_action(self):

        self.input_text.delete(
            "1.0",
            tk.END
        )

        self.key_entry.delete(
            0,
            tk.END
        )

        self.result_text.delete(
            "1.0",
            tk.END
        )

        self.process_text.delete(
            "1.0",
            tk.END
        )

        self.show_initial_process()

        self.status_label.config(
            text="Siap digunakan",
            fg="#16A34A"
        )

    # ==================================================
    # INITIAL PROCESS
    # ==================================================

    def show_initial_process(self):

        text = """
============================================================
              CAESAR CIPHER
============================================================

Rumus Enkripsi:
C = (P + k) mod 26

Rumus Dekripsi:
P = (C - k) mod 26

Keterangan:
P = Plaintext
C = Ciphertext
k = Kunci / nilai pergeseran

Contoh:

Plaintext : HALO DUNIA
Kunci     : 3

H → 7  → (7 + 3) mod 26 → K
A → 0  → (0 + 3) mod 26 → D
L → 11 → (11 + 3) mod 26 → O
O → 14 → (14 + 3) mod 26 → R

Hasil:
KDOR GXQLD

Silakan masukkan teks dan kunci.
============================================================
"""

        self.process_text.insert(
            tk.END,
            text
        )

    def refresh_page(self):
        pass