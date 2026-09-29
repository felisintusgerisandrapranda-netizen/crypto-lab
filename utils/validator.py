"""
Validation Utility
Crypto Lab
"""


def validate_text(text, field_name="Teks"):
    """
    Memastikan input teks tidak kosong.
    """

    if text is None:
        raise ValueError(
            f"{field_name} tidak boleh kosong."
        )

    if not text.strip():
        raise ValueError(
            f"{field_name} tidak boleh kosong."
        )

    return text


def validate_caesar_key(key):
    """
    Validasi kunci Caesar.
    """

    if key is None or str(key).strip() == "":
        raise ValueError(
            "Kunci Caesar harus diisi."
        )

    try:
        key = int(key)
    except ValueError:
        raise ValueError(
            "Kunci Caesar harus berupa angka."
        )

    if not 0 <= key <= 25:
        raise ValueError(
            "Kunci Caesar harus berada pada angka 0 sampai 25."
        )

    return key


def validate_vigenere_key(key):
    """
    Validasi kunci Vigenère.
    """

    if key is None:
        raise ValueError(
            "Kunci Vigenère harus diisi."
        )

    key = str(key).strip()

    if not key:
        raise ValueError(
            "Kunci Vigenère harus diisi."
        )

    cleaned = "".join(
        char.upper()
        for char in key
        if "A" <= char.upper() <= "Z"
    )

    if not cleaned:
        raise ValueError(
            "Kunci Vigenère harus mengandung huruf A-Z."
        )

    return cleaned


def validate_columnar_key(key):
    """
    Validasi kunci Columnar.
    """

    if key is None:
        raise ValueError(
            "Kata kunci harus diisi."
        )

    key = str(key).strip()

    cleaned = "".join(
        char.upper()
        for char in key
        if "A" <= char.upper() <= "Z"
    )

    if not cleaned:
        raise ValueError(
            "Kata kunci harus mengandung huruf A-Z."
        )

    if len(set(cleaned)) != len(cleaned):
        raise ValueError(
            "Setiap huruf pada kunci Columnar "
            "harus berbeda.\n\n"
            "Contoh valid: TOMBAK"
        )

    return cleaned