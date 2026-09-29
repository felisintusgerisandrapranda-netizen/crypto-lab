"""
CRYPTO LAB
Aplikasi Kriptografi Klasik

Main Application
"""

import tkinter as tk
from tkinter import ttk, messagebox

from gui.dashboard import DashboardPage
from gui.caesar_page import CaesarPage
from gui.vigenere_page import VigenerePage
from gui.columnar_page import ColumnarPage
from gui.theory_page import TheoryPage
from gui.about_page import AboutPage


class CryptoLabApp(tk.Tk):

    def __init__(self):

        super().__init__()

        # ==================================================
        # WINDOW
        # ==================================================

        self.title(
            "🔐 CRYPTO LAB — Kriptografi Klasik"
        )

        self.geometry(
            "1200x760"
        )

        self.minsize(
            1000,
            650
        )

        self.configure(
            bg="#F4F7FB"
        )

        self.protocol(
            "WM_DELETE_WINDOW",
            self.close_application
        )

        # ==================================================
        # STYLE
        # ==================================================

        self.setup_styles()

        # ==================================================
        # CONTAINER
        # ==================================================

        self.container = tk.Frame(
            self,
            bg="#F4F7FB"
        )

        self.container.pack(
            fill="both",
            expand=True
        )

        self.container.grid_rowconfigure(
            0,
            weight=1
        )

        self.container.grid_columnconfigure(
            0,
            weight=1
        )

        # ==================================================
        # PAGES
        # ==================================================

        self.pages = {}

        self.create_pages()

        # ==================================================
        # DASHBOARD
        # ==================================================

        self.show_page(
            "dashboard"
        )

    # ==================================================
    # STYLES
    # ==================================================

    def setup_styles(self):

        style = ttk.Style(
            self
        )

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Modern.TEntry",
            padding=8,
            font=("Segoe UI", 11)
        )

        style.configure(
            "Primary.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(15, 9),
            foreground="#FFFFFF",
            background="#2563EB"
        )

        style.configure(
            "Secondary.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(15, 9),
            foreground="#0F172A",
            background="#E2E8F0"
        )

    # ==================================================
    # CREATE PAGES
    # ==================================================

    def create_pages(self):

        page_classes = {

            "dashboard": DashboardPage,

            "caesar": CaesarPage,

            "vigenere": VigenerePage,

            "columnar": ColumnarPage,

            "theory": TheoryPage,

            "about": AboutPage
        }

        for name, page_class in page_classes.items():

            page = page_class(
                self.container,
                self
            )

            self.pages[name] = page

            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

    # ==================================================
    # NAVIGATION
    # ==================================================

    def show_page(self, page_name):

        page = self.pages.get(
            page_name
        )

        if page is None:

            messagebox.showerror(
                "Error",
                f"Halaman '{page_name}' tidak ditemukan."
            )

            return

        page.tkraise()

        if hasattr(
            page,
            "refresh_page"
        ):

            page.refresh_page()

    # ==================================================
    # CLOSE
    # ==================================================

    def close_application(self):

        answer = messagebox.askyesno(
            "Keluar",
            "Apakah Anda yakin ingin keluar dari Crypto Lab?"
        )

        if answer:

            self.destroy()


# ======================================================
# START APPLICATION
# ======================================================

if __name__ == "__main__":

    app = CryptoLabApp()

    app.mainloop()