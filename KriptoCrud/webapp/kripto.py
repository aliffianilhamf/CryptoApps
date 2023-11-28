import math  # Import module math untuk fungsi ceil() dan floor()


# def tampilkan_menu():  # Fungsi untuk menampilkan menu
#     print(
#         "PROGRAM ENKRIPSI-DEKRIPSI ORTHOGONAL TRANSPOSITION"
#     )  # Menampilkan judul program
#     print("\n[MENU]")  # Menampilkan menu
#     print(" [1] Enkripsi")
#     print(" [2] Dekripsi")
#     print(" [3] Keluar")


def orthogonal_encrypt(pltx, step_size):  # Fungsi untuk enkripsi
    plain_text = pltx.replace(" ", "-")
    matrix_representation = (
        []
    )  # Matriks kosong untuk menyimpan representasi matriks dari teks
    encrypted_text = ""  # Teks terenkripsi

    for i in range(step_size):  # Mengisi matriks dengan karakter dari teks
        matrix_row = []  # Baris matriks
        # Loop ini akan mengulangi sebanyak kolom yang diperlukan dalam matriks, dan jumlah kolom dihitung dengan
        # membagi panjang teks (len(plain_text)) dengan step_size, dan menggunakan math.ceil()
        # untuk memastikan hasil pembagian dibulatkan ke atas agar semua karakter teks dapat masuk.
        for j in range(math.ceil(len(plain_text) / step_size)):
            index = (
                j * step_size
                + i  # j = indeks kolom saat ini, step_size = jumlah baris, i = indeks baris saat ini
            )  # Indeks karakter yang akan dimasukkan ke dalam baris matriks
            if index < len(
                plain_text
            ):  # Jika masih ada karakter yang tersisa, masukkan karakter ke dalam baris matriks
                matrix_row.append(
                    plain_text[index]
                )  # Masukkan karakter ke dalam baris matriks
            else:  # Jika tidak ada karakter yang tersisa, masukkan karakter '@' ke dalam baris matriks
                matrix_row.append("@")  # Masukkan karakter '@' ke dalam baris matriks
        matrix_representation.append(
            matrix_row
        )  # Masukkan baris matriks ke dalam matriks representasi

    print("Matrix:\n")  # Tampilkan matriks representasi
    for row in matrix_representation:  # Untuk setiap baris dalam matriks representasi
        print(row)  # Tampilkan baris

    # proses enkripsi
    matrix_height = step_size  # Tinggi matriks
    matrix_width = math.ceil(len(plain_text) / matrix_height)  # Lebar matriks

    #PENENTUAN BARIS AWAL
    #for i in range(matrix_height - 1, -1,-1):  # Mulai dari baris terakhir
    for i in range(matrix_height):  # Mulai dari baris pertama
        if matrix_height % 2 == 0:  # Jika height matriks genap
            # MENENTUKAN ARAH
            for j in range(matrix_width - 1, -1, -1):  # Bergerak mengular dari kanan ke kiri
            #for j in range(matrix_width ):  # Bergerak mengular dari  kiri ke kanan
                if matrix_representation[i][j] != "@":  # Jika bukan karakter '@'
                    encrypted_text += matrix_representation[i][j]  # Tambahkan karakter ke dalam teks terenkripsi
                else:  # Jika karakter '@'
                    encrypted_text += (
                        "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                    )
        else:  # Jika height matriks ganjil
            for j in range(matrix_width):  # Bergerak mengular dari kanan ke kiri
                #for j in range(matrix_width):  # Bergerak mengular dari  kiri ke kanan
                if matrix_representation[i][j] != "@":  # Jika bukan karakter '@'
                    encrypted_text += matrix_representation[i][j]  # Tambahkan karakter ke dalam teks terenkripsi
                else:  # Jika karakter '@'
                    encrypted_text += (
                        "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                    )
    return encrypted_text

def orthogonal_decrypt(cipher_text, step_size):  # Fungsi untuk dekripsi
    matrix_height = step_size  # Tinggi matriks
    matrix_width = math.ceil(len(cipher_text) / matrix_height)  # Lebar matriks

    plain_text_matrix = (
        [  # Matriks kosong untuk menyimpan representasi matriks dari teks
            [" " for _ in range(matrix_width)] for _ in range(matrix_height)
        ]
    )

    idx = 0  # Indeks untuk mengakses karakter dalam teks terenkripsi

    #PENENTUAN BARIS
    #for i in range(matrix_height - 1, -1, -1):  # Mulai dari baris terakhir 
    for i in range(matrix_height ):  # Mulai dari baris pERTAMA
        if matrix_height % 2 == 0:  # Jika tinggi matriks genap
            for j in range(matrix_width - 1, -1, -1):  # Bergerak mengular dari kanan ke kiri
                #for j in range(matrix_width ):  # Bergerak mengular dari kiri ke kanan
                plain_text_matrix[i][j] = cipher_text[
                    idx
                ]  # Masukkan karakter ke dalam matriks
                idx += 1  # Tambahkan indeks
        else:
            for j in range(matrix_width):  # Bergerak mengular dari kiri ke kanan
                #for j in range(matrix_width ):  # Bergerak mengular dari kiri ke kanan
                plain_text_matrix[i][j] = cipher_text[
                    idx
                ]  # Masukkan karakter ke dalam matriks
                idx += 1  # Tambahkan indeks

    print("Matrix:\n")  # Tampilkan matriks representasi
    for row in plain_text_matrix:  # Untuk setiap baris dalam matriks representasi
        print(row)  # Tampilkan baris

    plain_text = ""  # Teks terdekripsi
    
    for j in range(matrix_width):  # Untuk setiap kolom dalam matriks representasi
        for i in range(matrix_height):  # Untuk setiap baris dalam matriks representasi
            #ASELI
            if plain_text_matrix[i][j] != "@":  # Jika bukan karakter '@'
                plain_text += plain_text_matrix[i][j]
            # Tambahkan karakter ke dalam teks terdekripsi
            #plain_text += plain_text_matrix[i][j]
           
    return plain_text.replace("-", " ")  # Kembalikan - menjadi spasi
    #return plain_text  # jangan di replace