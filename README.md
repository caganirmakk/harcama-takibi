# 💸 Harcama Takibi Uygulaması

Bu proje, Python kullanılarak geliştirilmiş menü tabanlı bir kişisel harcama takip uygulamasıdır.  
Harcamalar JSON dosyasında saklanır ve program her açıldığında kaldığı yerden devam eder.

## 🚀 Özellikler

- Harcama ekleme
- Harcamaları listeleme
- Toplam harcama tutarını hesaplama
- Kategori bazlı harcama özeti
- Verilerin JSON dosyasında kalıcı olarak saklanması

## 🧠 Kullanılan Teknolojiler

- Python 3
- JSON (veri saklama)
- Dosya okuma / yazma (`json`, `os` modülleri)

## 📂 Proje Yapısı

harcama-takibi/
│
├── main.py
├── harcamalar.json
└── README.md


- `main.py` → Uygulamanın ana dosyası
- `harcamalar.json` → Harcamaların kaydedildiği dosya
- `README.md` → Proje açıklaması

## ▶️ Nasıl Çalıştırılır?

1. Repoyu klonla:
   ```bash
   git clone https://github.com/caganirmakk/harcama-takibi.git
Proje klasörüne gir:

cd harcama-takibi
Programı çalıştır:

python main.py
📋 Menü Seçenekleri
1 → Harcama Ekle

2 → Harcamaları Listele

3 → Toplam Harcama

4 → Kategori Özeti

0 → Çıkış

🗂 Veri Yapısı
Her harcama aşağıdaki alanları içerir:

id → Benzersiz harcama numarası

tutar → Harcama miktarı

kategori → Harcama kategorisi

aciklama → Açıklama

tarih → Gün/Ay/Yıl formatında tarih

🎯 Amaç
Bu proje eğitim ve öğrenme amaçlı geliştirilmiştir.
