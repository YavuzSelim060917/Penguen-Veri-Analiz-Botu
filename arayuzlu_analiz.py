import tkinter as tk
from tkinter import messagebox
import pandas as pd
import seaborn as sns

def analizi_baslat():
    try:
        df = sns.load_dataset('penguins')
        df = df.dropna()
        

        en_agir = df.nlargest(3, 'body_mass_g')
        ortalama = df['body_mass_g'].mean()
        

        rapor = f"--- ANALİZ TAMAMLANDI ---\n\n"
        rapor += f"Toplam Temiz Veri: {len(df)} adet\n"
        rapor += f"Genel Kilo Ortalaması: {ortalama:.2f} g\n\n"
        rapor += "--- EN AĞIR 3 PENGUEN ---\n"
        
        for i, row in en_agir.iterrows():
            rapor += f"{row['species']} ({row['island']}): {row['body_mass_g']}g\n"
            

        text_alanı.delete(1.0, tk.END)
        text_alanı.insert(tk.END, rapor)
        
    except Exception as e:
        messagebox.showerror("Hata", f"Bir sorun oluştu: {e}")

pencere = tk.Tk()
pencere.title("Yavuz - Veri Analiz Botu v1.0")
pencere.geometry("400x450")

label_baslik = tk.Label(pencere, text="Penguen Veri Analiz Sistemi", font=("Arial", 14, "bold"))
label_baslik.pack(pady=10)

buton_analiz = tk.Button(pencere, text="Analizi Çalıştır ve Raporla", command=analizi_baslat, 
                         bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
buton_analiz.pack(pady=10)

text_alanı = tk.Text(pencere, height=15, width=45)
text_alanı.pack(pady=10, padx=10)

pencere.mainloop()