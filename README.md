#Text-to-Speech Uygulaması (gTTS + Streamlit)

Bu proje, Python ile geliştirilen basit bir **yazıyı sese dönüştürme uygulamasıdır**. Google Text-to-Speech (gTTS) kütüphanesini kullanarak girilen metni `.mp3` formatında sese çevirir. Kullanıcı arayüzü Streamlit ile hazırlanmıştır.

##  Özellikler

-  Kullanıcıdan metin alır
-  gTTS ile sesi üretir
-  `.mp3` dosyası olarak kaydeder
-  (Opsiyonel) Web sayfasında sesi oynatır

  
##  Proje Yapısı

text_to_speech/
  |--app.py # Streamlit arayüzü
  |--gtts_makinesi.py # TTS fonksiyonu (gTTS işlemi burada)
  |--mp3/ # Oluşan ses dosyalarının bulunduğu klasör
  |--requirements.txt # Gerekli kütüphaneler
  |--README.md # Bu dosya

## Kurulum ve Çalıştırma

### 1. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt

2. Uygulamayı başlatın:
streamlit run app.py

3. Web arayüzü açılacak:
Tarayıcınızda http://localhost:8501 adresine giderek uygulamayı kullanabilirsiniz.

Kullanılan Teknolojiler
 Python 3.x

gTTS (Google Text to Speech)

Streamlit



