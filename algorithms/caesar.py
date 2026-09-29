"""
Caesar Cipher
Aplikasi Kriptografi Klasik - Crypto Lab
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_az(char):
    """Mengecek apakah karakter merupakan huruf A-Z."""
    return char.upper() in ALPHABET


def validate_key(key):
    """
    Memvalidasi kunci Caesar.
    Kunci harus berupa angka 0-25.
    """
    try:
        key = int(key)
    except (ValueError, TypeError):
        raise ValueError("Kunci Caesar harus berupa angka.")

    if not 0 <= key <= 25:
        raise ValueError("Kunci Caesar harus berada pada angka 0 sampai 25.")

    return key


def caesar_encrypt(text, key):
    """
    Melakukan enkripsi Caesar Cipher.

    Rumus:
    C = (P + k) mod 26
    """
    key = validate_key(key)

    result = []

    for char in text:
        if is_az(char):
            upper_char = char.upper()

            position = ord(upper_char) - ord("A")
            new_position = (position + key) % 26

            result.append(chr(new_position + ord("A")))
        else:
            # Spasi dan tanda baca tetap dipertahankan
            result.append(char)

    return "".join(result)


def caesar_decrypt(text, key):
    """
    Melakukan dekripsi Caesar Cipher.

    Rumus:
    P = (C - k) mod 26
    """
    key = validate_key(key)

    result = []

    for char in text:
        if is_az(char):
            upper_char = char.upper()

            position = ord(upper_char) - ord("A")
            new_position = (position - key) % 26

            result.append(chr(new_position + ord("A")))
        else:
            result.append(char)

    return "".join(result)


def caesar_steps(text, key, decrypt=False):
    """
    Menghasilkan langkah perhitungan Caesar Cipher.

    Digunakan untuk menampilkan proses algoritma
    pada halaman GUI.
    """
    key = validate_key(key)

    steps = []

    operation = "Dekripsi" if decrypt else "Enkripsi"

    steps.append("=" * 60)
    steps.append(f"PROSES {operation.upper()} CAESAR CIPHER")
    steps.append("=" * 60)
    steps.append(f"Input : {text}")
    steps.append(f"Kunci : {key}")
    steps.append("")

    if decrypt:
        steps.append("Rumus:")
        steps.append("P = (C - k) mod 26")
    else:
        steps.append("Rumus:")
        steps.append("C = (P + k) mod 26")

    steps.append("")
    steps.append("-" * 60)

    result = []

    for char in text:

        if is_az(char):

            upper_char = char.upper()

            position = ord(upper_char) - ord("A")

            if decrypt:
                new_position = (position - key) % 26
                result_char = chr(new_position + ord("A"))

                steps.append(
                    f"{upper_char} = {position} → "
                    f"({position} - {key}) mod 26 = "
                    f"{new_position} → {result_char}"
                )

            else:
                new_position = (position + key) % 26
                result_char = chr(new_position + ord("A"))

                steps.append(
                    f"{upper_char} = {position} → "
                    f"({position} + {key}) mod 26 = "
                    f"{new_position} → {result_char}"
                )

            result.append(result_char)

        else:
            result.append(char)

            if char == " ":
                steps.append("SPASI → tetap")
            else:
                steps.append(f"{char} → tetap")

    steps.append("-" * 60)
    steps.append(f"HASIL: {''.join(result)}")
    steps.append("=" * 60)

    return "\n".join(steps)


def get_example():
    """
    Mengembalikan contoh Caesar Cipher.
    """
    return {
        "text": "HALO DUNIA",
        "key": "3",
        "result": "KDOR GXQLD"
    }