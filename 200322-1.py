import random
while True:
    seviye = input("Bir seviye seçiniz (kolay/orta/zor)").lower() #lower yazıyı küçüğe çevirir. #upper yazıyı büyüğe çevirir.


    if seviye=="kolay":
        uret=random.randint(1,10)# 1 ile 10 arası rastgele sayı verir.
        print(uret)
        break

    elif seviye=="orta":
        uret=random.randint(1,50)
        break

    elif seviye=="zor":
        uret=random.randint(1,100)
        break

    else:
        print("Lütfen tekrar deneyiniz.")


while True:
    tahmin=int(input("Tahmin:"))

    if tahmin==uret:
        print("tebrikler")
        break

    elif tahmin<uret:
        print("Üzgünüm, sayınızı büyütünüz")

    else:
        print("Üzgünüm, sayınızı küçültün")

