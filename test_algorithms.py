from algorithms.caesar import (
    caesar_encrypt,
    caesar_decrypt,
    caesar_steps
)

from algorithms.vigenere import (
    vigenere_encrypt,
    vigenere_decrypt,
    vigenere_steps
)

from algorithms.columnar import (
    encrypt_columnar,
    decrypt_columnar,
    columnar_steps
)


print("=" * 60)
print("TEST CAESAR CIPHER")
print("=" * 60)

plaintext = "HALO DUNIA"
key = 3

ciphertext = caesar_encrypt(
    plaintext,
    key
)

print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)

print()

print(
    caesar_steps(
        plaintext,
        key
    )
)

print()

decrypted = caesar_decrypt(
    ciphertext,
    key
)

print("Dekripsi  :", decrypted)


print("\n")
print("=" * 60)
print("TEST VIGENÈRE CIPHER")
print("=" * 60)

plaintext = "KRIPTOGRAFI"
key = "LAMPION"

ciphertext = vigenere_encrypt(
    plaintext,
    key
)

print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)

print()

print(
    vigenere_steps(
        plaintext,
        key
    )
)

print()

decrypted = vigenere_decrypt(
    ciphertext,
    key
)

print("Dekripsi  :", decrypted)


print("\n")
print("=" * 60)
print("TEST COLUMNAR TRANSPOSITION")
print("=" * 60)

plaintext = "SISTEMINFORMASI"
key = "TOMBAK"

ciphertext = encrypt_columnar(
    plaintext,
    key
)

print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)

print()

print(
    columnar_steps(
        plaintext,
        key
    )
)

print()

decrypted = decrypt_columnar(
    ciphertext,
    key
)

print("Dekripsi  :", decrypted)


print("\n")
print("=" * 60)
print("SEMUA TEST SELESAI")
print("=" * 60)