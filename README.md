# Deck of Cards Oyunu 🎴

Bu proje, Python kullanılarak geliştirilmiş bir **Deck of Cards** oyunudur. Oyunda, bir kart destesi oluşturulur ve oyuncular (kullanıcı ve bilgisayar) sırayla kart çeker. Her kartın bir puan değeri vardır ve oyun sonunda en yüksek puanı alan kazanır. Oyun, Tkinter ile geliştirilmiş bir grafik arayüz (GUI) üzerinden oynanır ve görsel bir arka plan ile desteklenir.

## 📋 Proje Özellikleri

- **Kart Destesi Yönetimi**: 52 kartlık bir deste oluşturulur, karıştırılır ve oyunculara dağıtılır.
- **Puanlama Sistemi**:
  - J, Q, K kartları: 10 puan
  - As (A): 11 puan
  - 2, 3, 4, 5, 6 kartları: -6 puan
  - Diğer kartlar: Kendi değerleri kadar puan (örneğin 7, 7 puan).
- **Oynanış**:
  - Oyuncu, her turda 1 ile 8 arasında kart çekebilir.
  - Bilgisayar da rastgele bir sayıda kart çeker.
  - Destedeki kartlar bittiğinde oyun sona erer ve puanlar karşılaştırılır.
- **Grafik Arayüz**: Tkinter ile geliştirilmiş kullanıcı dostu bir arayüz.
- **Ayarlar Menüsü**: Ses açma/kapama gibi ayarlar için bir menü (şimdilik temel bir örnek).

<img src="https://github.com/user-attachments/assets/487bcc0a-42b1-473c-81f5-171fa83703ac" alt="Oyun Ekran Görüntüsü" width="500">

## 📂 Dosya Yapısı
deck-of-cards-game/
│
├── src/                    # Kaynak kod dosyaları
│   ├── deck_of_cards.py    # Kart ve deste mantığı
│   └── card_game.py        # Tkinter GUI uygulaması
│
├── assets/                 # Statik dosyalar
│   └── wallpaper.jpg       # Arka plan resmi
│
├── README.md               # Proje açıklaması
├── requirements.txt        # Gerekli kütüphaneler
└── .gitignore              # Git'in yoksayacağı dosyalar



## 🚀 Kurulum ve Çalıştırma

### 1. Gereksinimler
Projenin çalışması için aşağıdaki kütüphanelere ihtiyacınız var:
- Python 3.x
- Tkinter (Python ile birlikte gelir)
- Pillow (resim işlemleri için)

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
git clone https://github.com/kullanici-adi/deck-of-cards-game.git
cd deck-of-cards-game
python src/card_game.py  
```

## 🎮 Oyun Kuralları

- Oyuna başladığınızda, 52 kartlık bir deste karıştırılır.  
- Her turda, "Kaç kart çekmek istersiniz?" sorusuna bir sayı (1-8) girin ve "Kart Çek" butonuna tıklayın.  
- Bilgisayar da otomatik olarak kart çeker.  
- Çekilen kartlar ve puanlar ekranda gösterilir.  
- Destedeki kartlar bittiğinde oyun sona erer ve kazanan ilan edilir.

- ## 🛠️ Geliştirme ve Katkı

Bu proje açık kaynaklıdır. Katkıda bulunmak isterseniz:

1. Bu depoyu forklayın.  
2. Yeni bir özellik veya hata düzeltmesi için bir dal oluşturun: `git checkout -b yeni-ozellik`.  
3. Değişikliklerinizi yapın ve commit edin: `git commit -m "Yeni özellik eklendi"`.  
4. Dalınızı ana depoya itin: `git push origin yeni-ozellik`.  
5. Bir Pull Request oluşturun.

## 📧 İletişim

Herhangi bir soru veya öneri için bana ulaşabilirsiniz:  
- **E-posta:** [alaaddinuysal9@gmail.com]  
