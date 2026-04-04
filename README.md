# 🐧 Penguen Veri Analiz Paneli (Interactive Data Analyzer)

Bu proje, popüler **Palmer Penguins** veri setini kullanarak kullanıcıya interaktif bir veri keşfi deneyimi sunan masaüstü tabanlı bir analiz aracıdır. Kullanıcıların farklı biyometrik ölçümleri seçerek penguen türleri arasındaki dağılımları ve istatistiksel özetleri görmesini sağlar.

---

### 🚀 Öne Çıkan Özellikler
* **Dinamik Analiz:** Kullanıcı; Vücut Kütlesi, Kanat Uzunluğu veya Gaga Boyutu gibi farklı parametreler arasında geçiş yapabilir.
* **Yapay Bekleme (UX):** Kullanıcı deneyimini güçlendirmek için işlem sürecini hissettiren görsel yükleme barları (Progress Bar).
* **Veri Görselleştirme:** Matplotlib altyapısı ile otomatik güncellenen istatistiksel grafikler.
* **Hata Yönetimi:** Eksik verilerin (`NaN`) otomatik temizlenmesi ve çalışma zamanı hatalarının `try-except` blokları ile yönetilmesi.

---

### 🛠️ Kullanılan Teknolojiler
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Veri%20Görselleştirme-orange?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)

---

### 📦 Kurulum ve Çalıştırma

1. **Depoyu klonlayın:**
   ```bash
   https://github.com/YavuzSelim060917/Penguen-Veri-Analiz-Botu.git

2. **Gerekli kütüphaneleri yükleyin:**
   pip install pandas seaborn matplotlib

3. **Uygulamayı başlatın:**
   python arayuzlu_analiz.py

---

### 🧠 Yazılım Mimarisi Hakkında
Bu projede Hata Yönetimi (Error Handling) ve Veri Temizleme (Data Cleaning) süreçlerine odaklanılmıştır. Seaborn     kütüphanesinden çekilen ham veri, analiz öncesinde dropna() yöntemiyle stabilize edilmiştir. Arayüz tarafında ise    Python'un standart kütüphanesi olan Tkinter kullanılarak hafif ve hızlı bir yapı kurulmuştur.
