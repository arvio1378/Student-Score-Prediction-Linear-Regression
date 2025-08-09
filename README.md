# 📚 Prediksi Nilai Ujian Siswa Menggunakan Linear Regression

## 📋 Deskripsi
Projek ini adalah projek latihan saya untuk membuat aplikasi python sederhana untuk memprediksi skor dari jumlah jam belajar siswa menggunakan Linear Regression.
Projek ini juga mudah untuk pemula yang ingin memahami algoritma Machine Learning yang salah satunya adalah Linear Regression.

## 🚀 Fitur
- Input jumlah jam belajar dengan CLI
- Model Linear Regression dengan scikit-learn
- Dataset disimpan dalam format CSV
- Visualisasi hubungan antara jam belajar dan nilai
- Evaluasi model dengan R² Score, MAE, dan MSE
- Model disimpan ke file joblib untuk digunakan ulang
- Validasi input pada CLI untuk mencegah kesalahan

## 🧠 Tools & Library
- Python 3.X
- Pandas
- Seaborn
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit

## 📁 Struktur Folder
- Student Score Prediction (Linear Regression)/
  - data
      - student_scores.csv
  - notebooks
      - model.pkl
      - student.ipynb
  - src
      - main.py
  - requirements.txt
  - README.md

## 📊 Dataset

| Hours       | Scores      |
|-------------|-------------|
| 2.5         | 21          |
| 5.1         | 47          |
| 3.2         | 27          |
| 8.5         | 75          |
| ...         | ...         |

Dataset sederhana dengan 2 kolom, yaitu Hours dan Scores.

## 🖥️ Cara Menjalankan Program
1. Clone repositori
```bash
git clone https://github.com/arvio1378/Student-Score-Prediction-Linear-Regression.git
cd Student-Score-Prediction-Linear-Regression
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Jalankan program
```bash
python src/main.py
```

## 📈 Hasil & Evaluasi
Model memberikan hasil yang hampir akurat dengan nilai R² score yang hampir mendekat 1 sehingga cocok digunakan untuk demonstrasi Linear Regression dengan antar satu variabel.

## 🏗️ Kontribusi
Dapat melakukan kontribusi kepada siapa saja. Bisa bantu untuk :
- Menambahkan antaramuka di web/streamlit
- Menambahkan monitoring/logging untuk pencatatan prediksi
- Pengujian Model dengan data lain

## 🧑‍💻 Tentang Saya
Saya sedang belajar dan membangun karir di bidang AI/ML. Projek ini adalah latihan saya untuk membangun aplikasi python sederhana. Saya ingin lebih untuk mengembangkan skill saya di bidang ini melalui projek-projek yang ada.

📫 Terhubung dengan saya di:
- Linkedin : https://www.linkedin.com/in/arvio-abe-suhendar/
- Github : https://github.com/arvio1378
