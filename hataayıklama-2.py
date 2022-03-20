while True:
    try:
        sayi1=int(input("Birinci sayi giriniz:"))
        sayi2=int(input("İkinci sayıları giriniz"))
        print("Sayılarınızın bölümü:" ,sayi1/sayi2)
        break
    except ZeroDivisionError:#Hata mesajını özelleştiriyorum
        print("Bir sayı 0'a bölünmez")
    except ValueError:
        print("Lütfen bir sayı giriniz.")
    except:
        print("Genel hata")