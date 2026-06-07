# Energy Consumption Prediction

## 📌 Deskripsi

Proyek ini dirancang untuk memprediksi tingkat konsumsi energi pada berbagai jenis bangunan berdasarkan karakteristik fisik dan faktor lingkungan. Dengan memanfaatkan pemodelan machine learning, sistem ini menganalisis variabel seperti jenis bangunan, luas bangunan, jumlah penghuni, peralatan yang digunakan, suhu rata-rata, dan hari dalam seminggu untuk memperkirakan penggunaan daya dalam satuan kWh. Hasil akhir dari proyek ini ditujukan untuk membantu manajer gedung dalam memahami pola penggunaan daya serta menentukan faktor yang memengaruhi konsumsi energi guna mengoptimalkan efisiensi operasional.

---

## 💾 Dataset

Dataset yang digunakan dalam proyek ini memuat gambaran mengenai faktor karakteristik bangunan dan kondisi lingkungan yang memengaruhi tingkat penggunaan daya. Di dalamnya terdapat data terstruktur yang mencakup beberapa atribut spesifik seperti jenis bangunan, luas area bangunan, jumlah penghuni, jumlah peralatan yang digunakan, serta suhu rata-rata harian. Selain itu, dataset ini juga memuat informasi hari dalam seminggu serta nilai target variabel berupa konsumsi energi dalam satuan kWh untuk mendukung proses pemodelan prediktif.

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
git clone https://github.com/Fikri-Rouzan/energy-consumption-prediction.git
cd energy-consumption-prediction
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
