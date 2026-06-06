# Energy Consumption Prediction

## 📌 Deskripsi

Proyek ini dirancang untuk memprediksi tingkat konsumsi energi berdasarkan beberapa parameter kondisi lingkungan dan operasional. Dengan menggunakan pemodelan berbasis machine learning, sistem ini memperkirakan besaran penggunaan daya dari data sampel yang dimasukkan. Hasil dari proyek ini digunakan untuk memahami pola penggunaan energi serta membantu pengelolaan konsumsi daya menjadi lebih efisien.

---

## 💾 Dataset

Dataset yang digunakan dalam proyek ini memuat informasi mengenai faktor lingkungan dan karakteristik operasional yang memengaruhi tingkat penggunaan daya listrik. Di dalamnya mencakup sampel data terstruktur yang berisi beberapa atribut seperti metrik suhu, tingkat hunian, serta status operasional sistem untuk mendukung proses analisis dan pemodelan konsumsi energi.

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
