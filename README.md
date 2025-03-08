# Menentukan Arah Kiblat & Waktu Sholat dengan Python  

## Deskripsi Proyek
Proyek ini bertujuan untuk menghitung **arah kiblat** berdasarkan koordinat geografis dan menentukan **waktu sholat** sesuai kriteria **Kementerian Agama Indonesia (MABIMS)**.  

Perhitungan **arah kiblat** dilakukan menggunakan **metode trigonometri bola**, yang menghitung sudut antara lokasi pengguna dan Ka'bah di Mekah. Sementara itu, perhitungan **waktu sholat** menggunakan metode astronomi dengan sudut matahari yang telah ditetapkan oleh MABIMS.  

Proyek ini dikembangkan dengan **Python**, menggunakan pustaka seperti **NumPy, Pandas, Matplotlib, Folium**, dan **prayer-times-calculator** untuk mempermudah perhitungan dan visualisasi data.  

---  

## **Metode Perhitungan**  

### **1. Menentukan Arah Kiblat**  
Arah kiblat dihitung menggunakan **metode trigonometri bola**, dengan rumus:  

\[
\theta = \arctan \left( \frac{\sin(\Delta\lambda)}{\cos(\phi_1) \tan(\phi_2) - \sin(\phi_1) \cos(\Delta\lambda)} \right)
\]

Di mana:  
- \( \theta \) = arah kiblat dalam derajat  
- \( \phi_1 \) = latitude lokasi pengguna  
- \( \phi_2 \) = latitude Ka'bah (21.4225°)  
- \( \lambda_1 \) = longitude lokasi pengguna  
- \( \lambda_2 \) = longitude Ka'bah (39.8262°)  
- \( \Delta\lambda \) = \( \lambda_2 - \lambda_1 \)  

Hasil perhitungan ini menunjukkan **azimuth** atau sudut arah kiblat dari utara searah jarum jam. Hasil kemudian divisualisasikan menggunakan **Folium** dalam bentuk peta interaktif.  

---

### **2. Perhitungan Waktu Sholat**  
Waktu sholat dihitung berdasarkan **kriteria MABIMS** yang digunakan di Indonesia dan negara-negara Asia Tenggara.  

**Kriteria perhitungan waktu sholat (MABIMS):**  

| Waktu Sholat  | Kriteria Perhitungan |
|--------------|-------------------|
| **Imsak**   | 10 menit sebelum Subuh |
| **Subuh**   | Matahari berada **-20°** di bawah ufuk |
| **Dhuha**   | Matahari **4.5°** di atas ufuk |
| **Zuhur**   | Setelah matahari melewati meridian (Zawal) |
| **Ashar**   | Bayangan benda sama dengan panjang benda (Fiqh Syafi'i) |
| **Maghrib** | Matahari terbenam |
| **Isya**    | Matahari berada **-18°** di bawah ufuk |

**Catatan:**  
- Waktu sholat dikoreksi dengan **ikhtiyat ±2 menit** sebagai pengaman agar berlaku untuk seluruh wilayah kota.  
- Perhitungan dilakukan dengan pendekatan astronomi dan dapat disesuaikan dengan zona waktu pengguna.  

---

## **Fitur Utama**  
✅ **Menentukan arah kiblat** berdasarkan koordinat lokasi dengan metode trigonometri bola  
✅ **Menghitung waktu sholat** sesuai standar **MABIMS** dan Kementerian Agama RI  
✅ **Menggunakan metode astronomi** untuk perhitungan waktu sholat  
✅ **Koreksi waktu sholat** dengan **ikhtiyat ±2 menit**  
