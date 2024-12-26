#### Kode-MK: IF3024 - Pengolahan Sinyal Digital 
#### Prodi : Teknik Informatika
#### Dosen Pengampu : Martin C.T. Manullang


## Analisis Sinyal Respirasi dan rPPG dari Video Webcam
Proyek ini bertujuan untuk memproses sinyal fisiologis, yaitu sinyal respirasi dan photoplethysmography berbasis video (remote photoplethysmography atau rPPG), dari rekaman video menggunakan webcam. Data sinyal diekstraksi langsung dari frame video dengan teknik pemrosesan sederhana, seperti analisis intensitas piksel. Proses ini membantu dalam pengukuran kondisi fisiologis seseorang secara non-invasif.

## 📋 Deskripsi Proyek
Aplikasi ini mengambil input video dari webcam, memproses setiap frame, dan mengekstraksi sinyal respirasi serta rPPG.  
- **Sinyal Respirasi:** Menggunakan rata-rata intensitas piksel.  
- **Sinyal rPPG:** Menggunakan standar deviasi intensitas piksel.  
- Data ditampilkan secara real-time dalam bentuk grafik untuk memantau perubahan sinyal.  

## ⚙️ Teknologi yang Digunakan
1. **Python** - Bahasa pemrograman utama.  
2. **OpenCV** - Untuk menangkap dan memproses frame video.  
3. **NumPy** - Untuk perhitungan numerik.  
4. **Matplotlib** - Untuk visualisasi sinyal secara real-time.  
5. **SciPy** - Untuk filtering sinyal menggunakan bandpass Butterworth.  

## 🛠️ Instruksi Instalasi dan Penggunaan Program

### **Persyaratan Sistem**
Sebelum menjalankan program, pastikan sistem Anda memenuhi persyaratan berikut:
- **Python:** Versi 3.7 atau lebih baru.
- **Webcam:** Dibutuhkan untuk menangkap input video secara real-time.
- **Library Python:** Pastikan library berikut sudah terpasang:
  - `opencv-python`
  - `numpy`
  - `matplotlib`
  - `scipy`

---

## Contributors
| Full Name                       | NIM       | GitHub Username                       |
| ------------------------------- | --------- | ---------------                       |
| Maleakhi Pratama Tobing         | 121140225 | Male27                                |
| Yanto Pernando Halomoan Hutapea | 121140127 | yanto1988                             |
| Louis Paskalis Ginting          | 121140066 | LouisPaskalisGinting_121140066        |

## Logbook
| Date & Time                   | Project Progress and Updates                                           |
| ------------------------------| -----------------------------------------------------------------------|
| 18 Desember 2024, pukul 09.00	| Pengaturan awal proyek dan pembuatan repository di GitHub.             |
| 18 Desember 2024, pukul 14.00	|Mengimplementasikan pengambilan video webcam menggunakan OpenCV.        |
| 19 Desember 2024, pukul 10.30	|Menambahkan pemrosesan frame untuk ekstraksi sinyal respirasi dan rPPG. |
| 20 Desember 2024, pukul 11.00	|Mengimplementasikan filter bandpass Butterworth menggunakan SciPy.      |
| 21 Desember 2024, pukul 15.00	|Mengembangkan visualisasi sinyal real-time menggunakan Matplotlib.      |
| 22 Desember 2024, pukul 17.00	|Memperbaiki masalah sinkronisasi frame rate dan mengoptimalkan performa.|
| 23 Desember 2024, pukul 13.00	|Finalisasi kode dan persiapan dokumentasi untuk GitHub.                 |
| 24 Desember 2024, pukul 16.30	|Penyelesaian README dan laporan proyek.                                 |          

### **Langkah-Langkah Instalasi**
1. **Clone Repository:**
   Clone repository ini ke direktori lokal Anda dengan perintah berikut:
   ```bash
   git clone https://github.com/yourusername/RealTimeRespiratory-rPPG.git
   cd RealTimeRespiratory-rPPG

Alur Kerja Sistem
Menginisialisasi Webcam: Kamera membaca frame secara real-time.
Pemrosesan Frame:
Setiap frame dikonversi ke skala abu-abu.
Rata-rata intensitas dan standar deviasi dihitung untuk menghasilkan sinyal respirasi dan rPPG.
Visualisasi Data: Sinyal ditampilkan sebagai grafik real-time menggunakan Matplotlib.
