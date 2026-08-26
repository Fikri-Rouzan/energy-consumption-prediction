# PowerAnalytics

## 📌 Deskripsi

Proyek ini merupakan implementasi pemodelan machine learning yang digunakan untuk memprediksi besaran konsumsi energi dalam satuan kWh pada berbagai kategori bangunan. Pemodelan dibangun dengan menganalisis parameter masukan yang mencakup jenis bangunan, luas area, jumlah penghuni, jumlah peralatan aktif, suhu rata-rata wilayah, serta pengaruh hari dalam seminggu. Hasil akhir dari proyek ini ditujukan untuk membantu manajer gedung dalam memetakan pola penggunaan daya dan mengidentifikasi faktor yang memengaruhi konsumsi energi guna mendukung efisiensi operasional bangunan.

---

## 💾 Dataset

Dataset yang digunakan dalam proyek ini memuat data mengenai variabel operasional bangunan dan kondisi lingkungan yang memengaruhi tingkat penggunaan daya. Atribut yang tersedia di dalam data ini meliputi kategori jenis bangunan, luas bangunan, jumlah penghuni, jumlah peralatan yang digunakan, serta rata-rata suhu wilayah. Selain itu, terdapat informasi mengenai kategori hari serta nilai target berupa jumlah konsumsi energi dalam satuan kWh sebagai acuan untuk proses pemodelan prediktif.

---

## 🛠️ Tech Stack

| Kategori                    | Teknologi yang Digunakan                                                      |
| :-------------------------- | :---------------------------------------------------------------------------- |
| 🌐 **Programming Language** | `Python`                                                                      |
| 🌱 **Environment**          | `Jupyter Notebook`                                                            |
| 🧩 **Framework**            | `Streamlit`                                                                   |
| ⚛️ **Libraries**            | `NumPy`, `pandas`, `Matplotlib`, `seaborn`, `SciPy`, `scikit-learn`, `Joblib` |
| ⚡ **Tool**                 | `Google Colab`                                                                |
| 🚀 **Deployment**           | `Streamlit Community Cloud`                                                   |

---

## ⚙️ Petunjuk Pengaturan

1. **Prasyarat**
   - Python 3.11 atau lebih baru.
   - Git terinstal di komputer.

2. **Clone Repositori**

```bash
git clone https://github.com/Fikri-Rouzan/poweranalytics.git
cd poweranalytics
```

3. **Buat Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. **Install Dependensi**

```bash
pip install -r requirements.txt
```

5. **Menjalankan Dashboard Streamlit**

```bash
streamlit run dashboard/dashboard.py
```
