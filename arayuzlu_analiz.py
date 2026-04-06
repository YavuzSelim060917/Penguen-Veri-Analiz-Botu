import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# VERİYİ DOĞRUDAN KÜTÜPHANEDEN YÜKLE (En Güvenli Yol)
df_global = sns.load_dataset('penguins')
aktif_sutun = None

def asistan_konus(mesaj):
    asistan_mesaj_kutusu.config(text=mesaj)
    pencere.update_idletasks()

def veriyi_temizle():
    global df_global
    once = len(df_global)
    df_global = df_global.dropna()
    asistan_konus(f"Veri temizleme işlemi tamamlandı. \n{once - len(df_global)} eksik satır ayıklandı.")

def analizi_baslat():
    global df_global, aktif_sutun
    secilen_parametre = combo_ozellik.get()
    
    # Parametre Eşleştirme (Sabit ve Hatasız)
    harita = {
        "Vücut Kütlesi (g)": "body_mass_g", 
        "Kanat Uzunluğu (mm)": "flipper_length_mm", 
        "Gaga Uzunluğu (mm)": "bill_length_mm"
    }
    aktif_sutun = harita[secilen_parametre]
    
    # Analiz Hazırlığı
    analiz_df = df_global.dropna(subset=[aktif_sutun])
    ortalama = analiz_df[aktif_sutun].mean()
    en_yuksek = analiz_df.nlargest(3, aktif_sutun)
    en_dusuk = analiz_df.nsmallest(3, aktif_sutun)
    
    # Rapor Metni Oluşturma
    rapor = f"--- {secilen_parametre.upper()} ANALİZİ ---\n\n"
    rapor += f"İncelenen Kayıt Sayısı: {len(analiz_df)}\n"
    rapor += f"Genel Ortalama: {ortalama:.2f}\n\n"
    
    rapor += "--- EN YÜKSEK 3 DEĞER ---\n"
    for _, row in en_yuksek.iterrows():
        rapor += f"• {row['species']} ({row['island']}): {row[aktif_sutun]}\n"
        
    rapor += "\n--- EN DÜŞÜK 3 DEĞER ---\n"
    for _, row in en_dusuk.iterrows():
        rapor += f"• {row['species']} ({row['island']}): {row[aktif_sutun]}\n"

    # Arayüzü Güncelle
    text_alanı.delete(1.0, tk.END)
    text_alanı.insert(tk.END, rapor)
    asistan_konus("İşte sonuçlar!\nİstersen grafiğe de bakalım.")
    buton_grafik.pack(pady=5)

def grafigi_goster():
    if aktif_sutun:
        plt.figure(figsize=(8, 5))
        sns.barplot(data=df_global, x='species', y=aktif_sutun, palette='viridis')
        plt.title(f"Türlere Göre {aktif_sutun} Dağılımı", pad=20)
        plt.xlabel("Penguen Türleri")
        plt.ylabel("Ortalama Değer")
        plt.tight_layout()
        plt.show()

def raporu_kaydet():
    rapor_metni = text_alanı.get(1.0, tk.END)
    if len(rapor_metni.strip()) < 10:
        asistan_konus("Kaydedilecek bir analiz sonucu bulunamadı.")
        return
    dosya = filedialog.asksaveasfilename(defaultextension=".txt", title="Raporu Kaydet")
    if dosya:
        with open(dosya, "w", encoding="utf-8") as f:
            f.write(rapor_metni)
        asistan_konus("Analiz raporu başarıyla sisteme kaydedildi.")

# --- ARAYÜZ TASARIMI ---
pencere = tk.Tk()
pencere.title("Profesör Penguen: Akıllı Veri Analizörü")
pencere.geometry("520x780")
pencere.configure(bg="#f8f9fa")

# Asistan Paneli
asistan_cerceve = tk.Frame(pencere, bg="white", bd=1, relief="solid")
asistan_cerceve.pack(pady=15, padx=20, fill="x")
tk.Label(asistan_cerceve, text="🎓🐧", font=("Arial", 35), bg="white").pack(side="left", padx=10)
asistan_mesaj_kutusu = tk.Label(asistan_cerceve, 
                               text="Hoş Geldiniz! Ben Profesör Penguen.\nAnaliz etmek istediğiniz parametreyi seçin.", 
                               bg="white", wraplength=350, justify="left", font=("Arial", 10))
asistan_mesaj_kutusu.pack(side="left", padx=10, pady=10)

# Butonlar ve Seçimler
tk.Button(pencere, text="🧹 Veriyi Temizle", command=veriyi_temizle, bg="#e53935", fg="white", font=("Arial", 9)).pack(pady=10)

combo_ozellik = ttk.Combobox(pencere, values=["Vücut Kütlesi (g)", "Kanat Uzunluğu (mm)", "Gaga Uzunluğu (mm)"], state="readonly", width=35)
combo_ozellik.current(0)
combo_ozellik.pack(pady=10)

tk.Button(pencere, text="🚀 Analizi Başlat", command=analizi_baslat, bg="#2e7d32", fg="white", font=("Arial", 11, "bold"), width=25, pady=10).pack(pady=20)

text_alanı = tk.Text(pencere, height=12, width=55, font=("Consolas", 10), bd=1, relief="solid")
text_alanı.pack(pady=10, padx=20)

buton_grafik = tk.Button(pencere, text="📊 Grafiği Görüntüle", command=grafigi_goster, bg="#1976d2", fg="white", font=("Arial", 10, "bold"), width=25)

tk.Button(pencere, text="💾 Raporu Dosya Olarak Kaydet", command=raporu_kaydet, bg="#7b1fa2", fg="white", font=("Arial", 9)).pack(pady=10)

pencere.mainloop()
