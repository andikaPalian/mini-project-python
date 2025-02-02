# Notes : Binary Search adalah algoritma pencarian yang efisien untuk mencari elemen dalam array yang sudah diurutkan.
# Algoritma ini bekerja dengan membagi array menjadi dua bagian dan kemudian mencari elemen target dalam salah satu bagian tersebut.
# Algoritma ini memiliki kompleksitas waktu O(log n), yang berarti bahwa waktu yang dibutuhkan untuk mencari elemen dalam array yang besar akan bertambah secara logaritmik dengan ukuran array.
# Algoritma ini sangat efisien untuk mencari elemen dalam array yang besar dan digunakan dalam banyak aplikasi, seperti pencarian dalam database dan pencarian dalam array yang besar.
# Contoh penggunaan algoritma binary search adalah pencarian nama dalam daftar kontak, pencarian nomor telepon dalam daftar telepon, dan pencarian ID dalam database.


def binary_search(arr, target):
    # Awal dan akhir jangkauan pencarian
    left, right = 0, len(arr) -1
    # Loop sampai jangkauan pencarian tidak kosong
    while left <= right:
        # Temukan indeks tengah array
        mid = (left + right) // 2
        # Jika element target ditemukan di mid, kembalikan indeksnya
        if arr[mid] == target:
            return mid
        # Jika element target lebih besar dari element mid, pindah ke bagian kanan dari array
        elif arr[mid] < target:
            left = mid + 1
        # Jika element target lebih kecil dari element mid, pindah ke bagian kiri dari array
        else:
            right = mid - 1
    # Jika element target tidak ditemukan, kembalikan -1
    return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 18
result = binary_search(arr, target)
print(result) # Output: 8