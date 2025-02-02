import random

nama_pertama = input("Masukkan nama kamu : ")
nama_kedua = input("Masukkan nama pasangan kamu : ")

love_score = random.randint(1, 100)

if love_score > 70:
    print(f"{nama_pertama} dan {nama_kedua} memiliki love score {love_score}%. Kalian sangat cocok!")
elif love_score > 40 and love_score <= 70:
    print(f"{nama_pertama} dan {nama_kedua} memiliki love score {love_score}%. Masih ada harapan semangat!")
else:
    print(f"{nama_pertama} dab {nama_kedua} memiliki love score {love_score}%. Kalian tidak cocok! bagaikan air dan minyak")