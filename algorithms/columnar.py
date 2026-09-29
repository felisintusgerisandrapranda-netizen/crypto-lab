"""
Columnar Transposition Cipher
Aplikasi Kriptografi Klasik - Crypto Lab
"""


def clean_key(key):
    """
    Membersihkan key.

    Hanya huruf A-Z yang digunakan.
    """
    if key is None:
        return ""

    return "".join(
        char.upper()
        for char in str(key)
        if char.upper() >= "A"
        and char.upper() <= "Z"
    )


def validate_key(key):
    """
    Memvalidasi key Columnar Transposition.

    Setiap huruf harus berbeda.
    """
    key = clean_key(key)

    if not key:
        raise ValueError(
            "Kata kunci harus berisi huruf A-Z."
        )

    if len(set(key)) != len(key):
        raise ValueError(
            "Setiap huruf pada kunci harus berbeda.\n"
            "Contoh yang valid: TOMBAK."
        )

    return key


def clean_text(text):
    """
    Membersihkan plaintext/ciphertext.

    Hanya huruf A-Z yang digunakan.
    """
    if text is None:
        return ""

    return "".join(
        char.upper()
        for char in str(text)
        if char.upper() >= "A"
        and char.upper() <= "Z"
    )


def get_column_order(key):
    """
    Mendapatkan urutan kolom berdasarkan alfabet.

    Contoh:

    TOMBAK

    T O M B A K
    6 5 4 2 1 3
    """

    key = validate_key(key)

    sorted_indexes = sorted(
        range(len(key)),
        key=lambda index: key[index]
    )

    order = [0] * len(key)

    for number, index in enumerate(
        sorted_indexes,
        start=1
    ):
        order[index] = number

    return order


def build_grid(text, key):
    """
    Membuat grid Columnar Transposition.

    Plaintext dimasukkan:
    kiri → kanan
    atas → bawah
    """

    key = validate_key(key)

    text = clean_text(text)

    if not text:
        raise ValueError(
            "Teks harus berisi huruf."
        )

    columns = len(key)

    rows = (
        len(text) + columns - 1
    ) // columns

    grid = []

    position = 0

    for _ in range(rows):

        row = []

        for _ in range(columns):

            if position < len(text):
                row.append(text[position])
                position += 1
            else:
                row.append("")

        grid.append(row)

    return grid


def encrypt_columnar(text, key):
    """
    Enkripsi Columnar Transposition.
    """

    key = validate_key(key)

    text = clean_text(text)

    if not text:
        raise ValueError(
            "Plaintext harus berisi huruf."
        )

    grid = build_grid(text, key)

    columns = len(key)

    # Urutan kolom berdasarkan alfabet key
    column_order = sorted(
        range(columns),
        key=lambda index: key[index]
    )

    result = []

    for column in column_order:

        for row in grid:

            if row[column]:
                result.append(
                    row[column]
                )

    return "".join(result)


def decrypt_columnar(ciphertext, key):
    """
    Dekripsi Columnar Transposition.
    """

    key = validate_key(key)

    ciphertext = clean_text(ciphertext)

    if not ciphertext:
        raise ValueError(
            "Ciphertext harus berisi huruf."
        )

    columns = len(key)

    rows = (
        len(ciphertext) + columns - 1
    ) // columns

    remainder = len(ciphertext) % columns

    # Menentukan panjang masing-masing kolom
    if remainder == 0:

        column_lengths = [
            rows
            for _ in range(columns)
        ]

    else:

        column_lengths = [
            rows if index < remainder
            else rows - 1
            for index in range(columns)
        ]

    column_order = sorted(
        range(columns),
        key=lambda index: key[index]
    )

    column_data = [
        ""
        for _ in range(columns)
    ]

    position = 0

    for column in column_order:

        length = column_lengths[column]

        column_data[column] = (
            ciphertext[
                position:
                position + length
            ]
        )

        position += length

    result = []

    for row in range(rows):

        for column in range(columns):

            if row < len(
                column_data[column]
            ):

                result.append(
                    column_data[column][row]
                )

    return "".join(result)


def columnar_steps(text, key, decrypt=False):
    """
    Menampilkan proses Columnar Transposition.
    """

    key = validate_key(key)

    operation = (
        "DEKRIPSI"
        if decrypt
        else "ENKRIPSI"
    )

    cleaned_text = clean_text(text)

    if not cleaned_text:
        raise ValueError(
            "Teks harus berisi huruf."
        )

    steps = []

    steps.append("=" * 70)
    steps.append(
        f"PROSES {operation} COLUMNAR TRANSPOSITION"
    )
    steps.append("=" * 70)

    steps.append(
        f"Kunci      : {key}"
    )

    steps.append(
        f"Input      : {cleaned_text}"
    )

    steps.append("")

    # Nomor urutan kolom
    order = get_column_order(key)

    steps.append(
        "STRUKTUR KUNCI"
    )

    steps.append("-" * 70)

    steps.append(
        "Huruf : "
        + "  ".join(
            f"{char:>3}"
            for char in key
        )
    )

    steps.append(
        "Urutan: "
        + "  ".join(
            f"{number:>3}"
            for number in order
        )
    )

    steps.append("-" * 70)

    if not decrypt:

        grid = build_grid(
            cleaned_text,
            key
        )

        steps.append("")
        steps.append(
            "1. PLAINTEXT DISUSUN KE DALAM GRID"
        )

        steps.append("")

        # Header key
        steps.append(
            " | ".join(
                f" {char} "
                for char in key
            )
        )

        steps.append(
            "-" * (
                len(key) * 4
                + len(key) * 3
            )
        )

        for row in grid:

            steps.append(
                " | ".join(
                    f" {cell or ' '} "
                    for cell in row
                )
            )

        steps.append("")
        steps.append(
            "2. KOLOM DIBACA BERDASARKAN URUTAN ALFABET"
        )

        steps.append("")

        column_order = sorted(
            range(len(key)),
            key=lambda index: key[index]
        )

        result = []

        for column in column_order:

            column_text = "".join(
                row[column]
                for row in grid
                if row[column]
            )

            result.append(
                column_text
            )

            steps.append(
                f"Kolom {key[column]} "
                f"(urutan {order[column]}) "
                f"→ {column_text}"
            )

        steps.append("")
        steps.append(
            "3. CIPHERTEXT"
        )

        steps.append(
            " + ".join(result)
        )

        steps.append("")
        steps.append(
            f"HASIL: {''.join(result)}"
        )

    else:

        steps.append("")
        steps.append(
            "1. CIPHERTEXT DIBAGI KE DALAM KOLOM"
        )

        result = decrypt_columnar(
            cleaned_text,
            key
        )

        steps.append("")
        steps.append(
            "2. KOLOM DISUSUN KEMBALI SESUAI KUNCI"
        )

        steps.append("")
        steps.append(
            "3. GRID DIBACA KIRI → KANAN"
        )

        steps.append("")
        steps.append(
            f"4. PLAINTEXT: {result}"
        )

        steps.append("")
        steps.append(
            f"HASIL: {result}"
        )

    steps.append("=" * 70)

    return "\n".join(steps)


def get_example():
    """
    Mengembalikan contoh Columnar.
    """

    text = "SISTEMINFORMASI"
    key = "TOMBAK"

    return {
        "text": text,
        "key": key,
        "result": encrypt_columnar(
            text,
            key
        )
    }