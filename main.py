import json
import os

print("=" * 50)
print("Harcama Takibi Uygulamasına Hoşgeldiniz")

dosya_adi = "harcamalar.json"

# Verileri yükle
if os.path.exists(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as f:
        harcamalar = json.load(f)

    # En büyük id'yi bul
    id = 0
    for key in harcamalar.keys():
        if int(key) > id:
            id = int(key)
else:
    harcamalar = {}
    id = 0


while True:
    print("""
    1 - Harcama Ekle
    2 - Harcamaları Listele
    3 - Toplam Harcama
    4 - Kategori Özeti
    0 - Çıkış
    """)

    try:
        choice = int(input("Seçiminizi giriniz: "))
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
        continue

    # ÇIKIŞ
    if choice == 0:
        print("Çıkış yapılıyor...")
        break

    # HARCAMA EKLE
    elif choice == 1:
        id += 1

        try:
            tutar = float(input("Harcamanın tutarını giriniz: "))
        except ValueError:
            print("Tutar sayı olmalıdır!")
            continue

        kategori = input("Harcamanın kategorisini giriniz: ")
        aciklama = input("Harcamanın açıklamasını giriniz: ")

        try:
            gun = int(input("Gün: "))
            ay = int(input("Ay: "))
            yil = int(input("Yıl: "))
        except ValueError:
            print("Tarih alanları sayı olmalıdır!")
            continue

        tarih = f"{gun}/{ay}/{yil}"

        harcamalar[str(id)] = {
            "id": id,
            "tutar": tutar,
            "kategori": kategori,
            "aciklama": aciklama,
            "tarih": tarih
        }

        with open(dosya_adi, "w", encoding="utf-8") as f:
            json.dump(harcamalar, f, ensure_ascii=False, indent=4)

        print("Harcama eklendi.")

    # HARCAMALARI LİSTELE
    elif choice == 2:
        if not harcamalar:
            print("Henüz harcama yok.")
        else:
            for harcama in harcamalar.values():
                print(harcama)

    # TOPLAM HARCAMA
    elif choice == 3:
        toplam = 0
        for harcama in harcamalar.values():
            toplam += harcama["tutar"]

        print(f"Toplam harcama: {toplam}")

    # KATEGORİ ÖZETİ
    elif choice == 4:
        kategori_ozet = {}

        for harcama in harcamalar.values():
            kategori = harcama["kategori"]
            tutar = harcama["tutar"]

            if kategori in kategori_ozet:
                kategori_ozet[kategori] += tutar
            else:
                kategori_ozet[kategori] = tutar

        for k, v in kategori_ozet.items():
            print(f"{k}: {v}")

    else:
        print("Hatalı seçim yaptınız!")