"""
Vigenère Cipher
Aplikasi Kriptografi Klasik - Crypto Lab
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_az(char):
    """Mengecek apakah karakter merupakan huruf A-Z."""
    return char.upper() in ALPHABET


def clean_key(key):
    """
    Membersihkan key Vigenère.

    Hanya huruf A-Z yang digunakan.
    """
    if key is None:
        return ""

    return "".join(
        char.upper()
        for char in str(key)
        if char.upper() in ALPHABET
    )


def validate_key(key):
    """
    Memvalidasi key Vigenère.
    """
    key = clean_key(key)

    if not key:
        raise ValueError(
            "Kunci Vigenère harus berisi huruf alfabet."
        )

    return key


def vigenere_encrypt(text, key):
    """
    Enkripsi Vigenère Cipher.

    Rumus:
    C = (P + K) mod 26
    """
    key = validate_key(key)

    result = []

    key_index = 0

    for char in text:

        if is_az(char):

            plaintext_value = (
                ord(char.upper()) - ord("A")
            )

            key_char = key[key_index % len(key)]

            key_value = (
                ord(key_char) - ord("A")
            )

            cipher_value = (
                plaintext_value + key_value
            ) % 26

            result.append(
                chr(cipher_value + ord("A"))
            )

            key_index += 1

        else:
            # Spasi dan tanda baca tidak diubah
            result.append(char)

    return "".join(result)


def vigenere_decrypt(text, key):
    """
    Dekripsi Vigenère Cipher.

    Rumus:
    P = (C - K) mod 26
    """
    key = validate_key(key)

    result = []

    key_index = 0

    for char in text:

        if is_az(char):

            cipher_value = (
                ord(char.upper()) - ord("A")
            )

            key_char = key[key_index % len(key)]

            key_value = (
                ord(key_char) - ord("A")
            )

            plaintext_value = (
                cipher_value - key_value
            ) % 26

            result.append(
                chr(plaintext_value + ord("A"))
            )

            key_index += 1

        else:
            result.append(char)

    return "".join(result)


def vigenere_steps(text, key, decrypt=False):
    """
    Menampilkan langkah perhitungan Vigenère Cipher.
    """

    key = validate_key(key)

    operation = "Dekripsi" if decrypt else "Enkripsi"

    steps = []

    steps.append("=" * 75)
    steps.append(
        f"PROSES {operation.upper()} VIGENÈRE CIPHER"
    )
    steps.append("=" * 75)

    steps.append(f"Input : {text}")
    steps.append(f"Kunci : {key}")
    steps.append("")

    if decrypt:
        steps.append("Rumus:")
        steps.append("P = (C - K) mod 26")
    else:
        steps.append("Rumus:")
        steps.append("C = (P + K) mod 26")

    steps.append("")
    steps.append("-" * 75)

    # Header tabel
    steps.append(
        f"{'NO':<4}"
        f"{'CHAR':<8}"
        f"{'KEY':<8}"
        f"{'P/C':<8}"
        f"{'K':<8}"
        f"{'HASIL':<8}"
    )

    steps.append("-" * 75)

    result = []

    key_index = 0
    number = 1

    for char in text:

        if is_az(char):

            char_value = (
                ord(char.upper()) - ord("A")
            )

            key_char = key[
                key_index % len(key)
            ]

            key_value = (
                ord(key_char) - ord("A")
            )

            if decrypt:

                result_value = (
                    char_value - key_value
                ) % 26

            else:

                result_value = (
                    char_value + key_value
                ) % 26

            result_char = chr(
                result_value + ord("A")
            )

            result.append(result_char)

            steps.append(
                f"{number:<4}"
                f"{char.upper():<8}"
                f"{key_char:<8}"
                f"{char_value:<8}"
                f"{key_value:<8}"
                f"{result_char:<8}"
            )

            key_index += 1
            number += 1

        else:

            result.append(char)

            if char == " ":
                steps.append(
                    f"{'-':<4}"
                    f"{'SPASI':<8}"
                    f"{'-':<8}"
                    f"{'-':<8}"
                    f"{'-':<8}"
                    f"{'TETAP':<8}"
                )
            else:
                steps.append(
                    f"{'-':<4}"
                    f"{char:<8}"
                    f"{'-':<8}"
                    f"{'-':<8}"
                    f"{'-':<8}"
                    f"{'TETAP':<8}"
                )

    steps.append("-" * 75)
    steps.append(
        f"HASIL: {''.join(result)}"
    )
    steps.append("=" * 75)

    return "\n".join(steps)


def get_example():
    """
    Mengembalikan contoh Vigenère Cipher.
    """
    return {
        "text": "KRIPTOGRAFI",
        "key": "LAMPION",
        "result": vigenere_encrypt(
            "KRIPTOGRAFI",
            "LAMPION"
        )
    }