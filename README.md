# Face_Expression_Detection

Repositori ini berisi proyek segmentasi ekspresi wajah menggunakan teknik Deep Learning dan Computer Vision. Proyek ini bertujuan untuk menganalisis ekspresi wajah pengguna dan membantu meningkatkan pemahaman terhadap emosi manusia dalam interaksi antara manusia dan teknologi yang sesuai berdasarkan analisis tersebut. Repositori ini mencakup file Jupyter Notebook yang menjelaskan proses secara menyeluruh, mulai dari eksplorasi data hingga penerapan model deep learning.

## Daftar Isi 🗒️
1. [Link Terkait Project](#link-terkait-project-)
2. [Project Overview](#project-overview-)
3. [Latar Belakang Masalah](#latar-belakang-masalah-)
4. [Problem Statement](#problem-statement-)
5. [Metode yang Digunakan](#metode-yang-digunakan-)
6. [Hasil dan Rekomendasi](#hasil-dan-rekomendasi-)
7. [File yang Tersedia](#file-yang-tersedia-)
8. [Cara Menggunakan Project Ini](#cara-menggunakan-project-ini-)
9. [Dependencies](#dependencies-)
10. [Libraries](#libraries-)
11. [Author](#author-)

## Link Terkait Project ⛓️‍💥

- [Dataset](https://www.kaggle.com/datasets/ritesh1420/face-expression-data)
- [Deployment](https://huggingface.co/spaces/mseptianz/expression_detection)

## Project Overview 📝

Dalam proyek ini, saya menggunakan teknik Deep Learning untuk menganalisis ekspresi wajah pengguna. Beberapa langkah utama yang dicakup dalam proyek ini adalah:

1. **Import Libraries dan Eksplorasi Data**:
    - Memuat dataset dan melakukan eksplorasi awal untuk memahami struktur dan karakteristik data.

2. **Preprocessing Data**:
    - Melakukan pembersihan dan persiapan data, termasuk penanganan gambar dan normalisasi.

3. **Training Base Model**:
    - Membangun dan melatih model deep learning untuk mengidentifikasi bentuk wajah.

4. **Evaluasi Base Model**:
    - Menggunakan metrik evaluasi untuk menilai kinerja model.

5. **Tuning Model**:
    - Membangun dan melatih model deep learning dengan beberapa hyperparameter tuning untuk mengidentifikasi ekspresi wajah.

6. **Evaluasi Model yang Dituning**:
    - Menggunakan metrik evaluasi untuk menilai kinerja model.

7. **Menggunakan Model Transfer Learning**:
    - Membangun dan melatih model deep learning dengan transfer learning untuk mengidentifikasi bentuk wajah.

8. **Evaluasi Model Hasil Transfer Learning**:
    - Menggunakan metrik evaluasi untuk menilai kinerja model.

9. **Pengambilan Keputusan**:
    - Mengambil keputusan terhadap performa model.

## Latar Belakang Masalah 🧐

Ekspresi wajah adalah salah satu bentuk komunikasi non-verbal yang paling kuat dan mendalam dalam menggambarkan emosi manusia. Meskipun manusia dapat dengan mudah membaca ekspresi wajah orang lain, proses ini bagi mesin adalah tantangan besar. Deteksi dan klasifikasi ekspresi wajah membutuhkan pemahaman yang mendalam mengenai pola-pola visual yang terkait dengan emosi manusia, yang berbeda-beda antar individu dan budaya. Oleh karena itu, pengembangan model pendeteksi ekspresi wajah berbasis kecerdasan buatan (AI) menjadi penting untuk memungkinkan komputer memahami dan merespons ekspresi manusia secara otomatis.

## Problem Statement √

**Specific:** 
membuat sebuah model deep learning yang dapat mengidentifikasi ekspresi wajah ke dalam beberapa kategori emosi, seperti senang, sedih, marah, terkejut, takut, dan netral, secara otomatis.

**Measurable:**
Keberhasilan model akan diukur berdasarkan akurasi identifikasi ekspresi wajah yang mencapai minimal 80%, dengan menggunakan dataset yang tersedia dari berbagai usia, jenis kelamin, dan latar belakang budaya.

**Achievable:**
Model akan dibangun menggunakan teknologi deep learning, khususnya Convolutional Neural Networks (CNN), yang efektif dalam mengenali pola pada data citra wajah. 

**Relevant:**
Sistem ini akan memungkinkan analisis ekspresi wajah pengguna atau audiens secara real-time untuk memahami respons emosional mereka terhadap konten, produk, atau lingkungan tertentu, yang berguna untuk meningkatkan pengalaman pengguna, menyempurnakan strategi pemasaran, serta menyesuaikan konten berdasarkan reaksi audiens.

**Time-bound:**
Model ini diharapkan dapat dikembangkan dan diuji dalam waktu 2 bulan

**Problem Statement:**
Membangun model berbasis deep learning yang dapat mengidentifikasi ekspresi wajah ke dalam beberapa kategori. Dengan adanya sistem otomatis ini, organisasi dapat menganalisis ekspresi pengguna atau audiens secara real-time untuk memahami respons emosional mereka terhadap konten, produk, atau lingkungan tertentu. 

## Metode yang Digunakan 🛠️

- Deep Learning
- Computer Vision
- Klasifikasi Gambar
- Visualisasi Data

## Hasil dan Rekomendasi 💡

Berdasarkan beberapa model yang sudah diuji sebelumnya (base model, model improvement dan model dengan transfer learning), model yang akan dipilih adalah model dengan menggunakan transfer learning dari VGG16 dengan arsitektur sequential API. Walaupun kesalahan prediksi yang akan terjadi sebesar 30%, namun hal ini akan cukup membantu dalam pengembangan bisnis dan menyediakan fasilitas yang akan digunakan berdasarkan performa dari model ini.

**Rekomendasi:**
- Model menunjukkan kinerja yang sangat baik dalam mengklasifikasikan ekspresi "Ahegao", dengan nilai precision, recall, dan F1-score yang hampir mencapai 1. Hal ini menunjukkan akurasi yang tinggi dalam identifikasi ekspresi tersebut.
- Model memiliki performa yang cukup baik dalam mengklasifikasikan ekspresi "Happy", meskipun nilai precision sedikit lebih rendah dibandingkan dengan recall. Ini menandakan bahwa model mungkin cenderung salah mengklasifikasikan beberapa ekspresi lain sebagai "Happy".
- Model menghadapi kesulitan dalam membedakan ekspresi "Neutral" dan "Sad". Nilai precision, recall, dan F1-score untuk kedua kelas ini cenderung rendah jika dibandingkan dengan kelas lainnya, yang menunjukkan bahwa model sering salah mengklasifikasikan ekspresi "Neutral" sebagai "Sad" dan sebaliknya.
- Model menunjukkan kinerja yang cukup baik dalam mengklasifikasikan ekspresi "Surprise" dan "Angry", meskipun precision untuk kelas "Angry" sedikit lebih rendah dibandingkan recall.
- Meskipun performa model cukup baik pada beberapa kategori, tuning hyperparameter tambahan atau eksperimen dengan arsitektur yang berbeda bisa meningkatkan akurasi keseluruhan.
- Model bisa melakukan prediksi dengan baik, tetapi aspect ratio foto disarankan 1:1 agar tidak terjadi stretching pada foto saat melakukan resize image, dan angle foto menghadap kedepan sejajar dengan kamera.

## File yang Tersedia 📂

- `Face_Expression_Detection.ipynb`: Jupyter Notebook yang berisi langkah-langkah analisis data, pengembangan model deep learning, evaluasi model, dan wawasan yang diperoleh dari analisis.
- `Data_Inference.ipynb`: Jupyter Notebook yang berisi prediksi unseen data menggunakan model yang sudah dibuat sebelumnya
- `url.txt` : Source data & deployment
- `Deployment` : Folder berisikan file-file yang telah dideploy  
  
## Cara Menggunakan Project Ini 💻

1. Clone repositori ini ke dalam lokal Anda:
    ```bash
    https://github.com/mseptianz/Face_Expression_Detection.git
    ```

2. Jalankan Jupyter Notebook untuk mengikuti alur analisis data:
    ```bash
    jupyter notebook Face_Expression_Detection.ipynb
    ```

## Dependencies ⚙️

- ![Jupyter Notebook](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 3.8.20
- ![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)

## Libraries 📚
- TensorFlow
- Keras
- OS
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Author ✍️
**Muhammad Septian Zamzani**

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhammad-septian-zamzani-a9a8b5230/)
