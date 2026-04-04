import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

df_global = None

def analizi_baslat():
    global df_global
    secilen_ozellik = combo_ozellik.get() # Kullanıcının neyi seçtiğini alıyoruz
    
    # Sözlük yapısıyla kullanıcı dostu isimleri kod isimlerine çevirelim
    ozellik_haritasi = {
        "Vücut Kütlesi (g)": "body_mass_g",
        "Kanat Uzunluğu (mm)": "flipper_length_mm",
        "Gaga Uzunluğu (mm)": "bill_length_mm"
    }
    
    sütun_adi = ozellik_haritasi[secilen_ozellik]

    try:
        # Görsel yükleme efekti
        buton_analiz.config(state="disabled", text="Veriler İşleniyor...")
        progress_bar.pack(pady=5)
        for i in range(1, 101, 20):
            progress_bar['value'] = i
            pencere.update_idletasks()
            time.sleep(0.1)

        df = sns.load_dataset('penguins').dropna()
        df_global = df

        # Dinamik Analiz: Kullanıcının seçtiği özelliğe göre en yüksek 3'ü bul
        en_yuksek = df.nlargest(3, sütun_adi)
        ortalama = df[sütun_adi].mean()

        rapor = f"--- {secilen_ozellik.upper()} ANALİZİ ---\n\n"
        rapor += f"İncelenen Toplam Penguen: {len(df)}\n"
        rapor += f"Genel Ortalama: {ortalama:.2f}\n\n"
        rapor += f"--- EN YÜKSEK 3 DEĞER ---\n"
        
        for i, row in en_yuksek.iterrows():
            rapor += f"{row['species']} ({row['island']}): {row[sütun_adi]}\n"

        text_alanı.delete(1.0, tk.END)
        text_alanı.insert(tk.END, rapor)
        
        buton_grafik.pack(pady=5)
        progress_bar.pack_forget()
        buton_analiz.config(state="normal", text="Farklı Bir Özellik Analiz Et")
        
    except Exception as e:
        messagebox.showerror("Hata", f"Veri yüklenemedi: {e}")
        buton_analiz.config(state="normal")

def grafigi_goster():
    if df_global is not None:
        secilen = combo_ozellik.get()
        ozellik_haritasi = {
            "Vücut Kütlesi (g)": "body_mass_g",
            "Kanat Uzunluğu (mm)": "flipper_length_mm",
            "Gaga Uzunluğu (mm)": "bill_length_mm"
        }
        sütun = ozellik_haritasi[secilen]
        
        plt.figure(figsize=(8, 5))
        # Türlere göre seçilen özelliğin ortalamasını grafik yapalım
        df_global.groupby('species')[sütun].mean().plot(kind='bar', color=['teal', 'orange', 'purple'])
        
        plt.title(f'Türlere Göre Ortalama {secilen}', fontsize=12, fontweight='bold')
        plt.ylabel('Değer')
        plt.xticks(rotation=0)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.show()

# --- ARAYÜZ ---
pencere = tk.Tk()
pencere.title("Yavuz - Dinamik Veri Analizörü v1.2")
pencere.geometry("500x650")
pencere.configure(bg="#f5f5f5")

tk.Label(pencere, text="Penguen Analiz Paneli", font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=15)

# KULLANICI SEÇİM ALANI
tk.Label(pencere, text="Analiz edilecek özelliği seçin:", bg="#f5f5f5", font=("Arial", 10)).pack()
combo_ozellik = ttk.Combobox(pencere, values=["Vücut Kütlesi (g)", "Kanat Uzunluğu (mm)", "Gaga Uzunluğu (mm)"], state="readonly", width=30)
combo_ozellik.current(0) # Varsayılan olarak ilkini seç
combo_ozellik.pack(pady=10)

buton_analiz = tk.Button(pencere, text="Analizi Başlat", command=analizi_baslat, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=25, pady=8)
buton_analiz.pack(pady=10)

progress_bar = ttk.Progressbar(pencere, orient="horizontal", length=300, mode="determinate")

buton_grafik = tk.Button(pencere, text="📊 Dinamik Grafiği Göster", command=grafigi_goster, bg="#2196F3", fg="white", font=("Arial", 11, "bold"), width=25, pady=8)

text_alanı = tk.Text(pencere, height=12, width=55, font=("Courier", 10), bd=2, relief="groove")
text_alanı.pack(pady=15, padx=20)

pencere.mainloop()
