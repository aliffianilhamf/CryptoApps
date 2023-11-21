def enkripsi_caesar(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Periksa apakah karakter adalah huruf
            if char.isupper():
                # Enkripsi huruf besar
                ciphertext += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                # Enkripsi huruf kecil
                ciphertext += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            # Tambahkan karakter non-huruf tanpa mengenkripsi
            ciphertext += char
    return ciphertext

# Contoh penggunaan
plaintext = "alip"
shift_amount = 3
ciphertext = enkripsi_caesar(plaintext, shift_amount)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
def dekripsi_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Periksa apakah karakter adalah huruf
            if char.isupper():
                # Dekripsi huruf besar
                plaintext += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                # Dekripsi huruf kecil
                plaintext += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            # Tambahkan karakter non-huruf tanpa mendekripsi
            plaintext += char
    return plaintext

# Contoh penggunaan
ciphertext = "dols"
shift_amount = 3
plaintext = dekripsi_caesar(ciphertext, shift_amount)

print("Ciphertext:", ciphertext)
print("Plaintext:", plaintext)
