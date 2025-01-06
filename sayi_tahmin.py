import random

# Rastgele bir sayı seç (1-100 arası)
secret_number = random.randint(1, 100)
print("1 ile 100 arasında bir sayı tuttum. Hadi tahmin etmeye çalış!")

while True:
    try:
        # Kullanıcıdan tahmin alma
        guess = int(input("Tahmininiz: "))

        # Tahmini kontrol et
        if guess < secret_number:
            print("Daha büyük bir sayı söyle!")
        elif guess > secret_number:
            print("Daha küçük bir sayı söyle!")
        else:
            print(f"Tebrikler! Doğru tahmin ettiniz. Sayı: {secret_number}")
            break  # Doğru tahmin, oyunu bitir
    except ValueError:
        print("Lütfen bir sayı girin!")
