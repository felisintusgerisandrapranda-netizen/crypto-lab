"""
File Handler Utility
Crypto Lab
"""

import os
from tkinter import filedialog


def save_text_file(text, title="Simpan Hasil"):
    """
    Menyimpan teks ke file TXT.
    """

    if not text.strip():
        raise ValueError(
            "Tidak ada hasil yang dapat disimpan."
        )

    file_path = filedialog.asksaveasfilename(
        title=title,
        defaultextension=".txt",
        filetypes=[
            (
                "Text File",
                "*.txt"
            ),
            (
                "All Files",
                "*.*"
            )
        ]
    )

    if not file_path:
        return None

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)

    return file_path


def save_result(
    input_text,
    key,
    result,
    algorithm,
    operation
):
    """
    Menyimpan hasil lengkap ke TXT.

    Isi file:

    Algoritma
    Operasi
    Input
    Kunci
    Hasil
    """

    content = f"""
========================================
CRYPTO LAB
HASIL KRIPTOGRAFI
========================================

Algoritma : {algorithm}
Operasi   : {operation}

----------------------------------------
INPUT
----------------------------------------

{input_text}

----------------------------------------
KUNCI
----------------------------------------

{key}

----------------------------------------
HASIL
----------------------------------------

{result}

========================================
""".strip()

    return save_text_file(
        content,
        title=f"Simpan Hasil {algorithm}"
    )