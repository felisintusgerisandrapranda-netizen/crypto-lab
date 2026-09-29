"""
Clipboard Utility
Crypto Lab
"""

import tkinter as tk


def copy_to_clipboard(text):
    """
    Menyalin teks ke clipboard Windows.
    """

    root = tk.Tk()
    root.withdraw()

    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

    root.destroy()


def copy_widget_content(widget):
    """
    Menyalin isi widget Text ke clipboard.
    """

    text = widget.get("1.0", tk.END).rstrip("\n")

    if not text:
        raise ValueError(
            "Tidak ada teks yang dapat disalin."
        )

    copy_to_clipboard(text)

    return text