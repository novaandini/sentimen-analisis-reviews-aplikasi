from google_play_scraper import reviews, Sort
import pandas as pd

# Ambil 100 ulasan dari aplikasi "Tokopedia"
result, _ = reviews(
    'com.tokopedia.tkpd',  
    lang='id',             
    country='id',
    count=5000,
    sort=Sort.NEWEST
)

# Konversi hasil ke DataFrame pandas
df = pd.DataFrame(result, columns=["userName", "score", "at", "content"])

# Filter review dengan panjang minimal 20 karakter
df_filtered = df[df["content"].str.len() >= 20]

# Simpan ke CSV
csv_filename = "reviews.csv"
df_filtered.to_csv(csv_filename, index=False, encoding="utf-8")

print(f"Scraping selesai! Data disimpan di {csv_filename}")