from kütüphane import *
print(""""
***************************
kütüphane programına hoşgeldiniz

işlemler:

1.Kitapları göster

2.kitap sorgula

3.kitap ekle

4.kitap sil

5.baskı yükselt

çıkmak için 'q' ya basın

*****************************"""   )
kütüphane=Kütüphane()
while True:
    işlem=input("yapacağınız işlem seçin (1,2,3,4):")

    if işlem=="q":
        print("program sonlandırılıyor.....")
        time.sleep(1)
        print("yeniden bekleriz :)")
        break
    elif işlem=="1":

        kütüphane.kitapları_göster()
    elif işlem=="2":
        isim=input("hangi kitabı istiyorsun")
        print("kitap sorgulanıyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif işlem=="3":
        isim=input("isim:")
        yazar=input("yazar:")
        yayınevi=input("yayınevi:")
        tür=input("tür:")
        baskı=int(input("baskı:"))
        yeni_kitap=Kitap(isim,yazar,yayınevi,tür,baskı)
        print("kitap ekleniyor....")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("kitap eklendi.....")
    elif işlem=="4":
        isim=input("hangi kitabı silmek istiyorsun:")
        cevap=input("emin misiniz:(E/H)")
        if cevap=="E":
            print("kitap siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("kitap silindi....")
    elif işlem=="5":
        isim=input("hangi kitabın baskısını yükseltmek istiyorsun:")
        print("baskı yükseltiyoruz...")
        time.sleep(2)
        kütüphane.baskı_yükseltme(isim)
        print("baskı yükseltildi...")
    else:
        print("....geçersiz işlem....")





























