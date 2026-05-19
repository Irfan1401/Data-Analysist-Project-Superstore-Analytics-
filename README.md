Superstore Analytics Dashboard
Proyek ini adalah aplikasi dasbor interaktif berbasis Streamlit untuk menganalisis performa penjualan dan melakukan segmentasi pelanggan (RFM Analysis) dari sebuah superstore. Proyek ini dilengkapi dengan skrip pembuat data tiruan (dummy data) untuk simulasi.

🚀 Fitur Utama
Data Generator (generate_data.py): Menghasilkan data transaksi penjualan secara otomatis yang mencakup berbagai produk, kota, metode pembayaran, dan riwayat belanja pelanggan selama setahun terakhir.

Interactive Dashboard (dashboard.py):

Filter Dinamis: Memfilter data berdasarkan Kota dan Metode Pembayaran.

KPI Metrics: Menampilkan Total Pendapatan, Total Pesanan, dan Rata-rata Nilai Pesanan.

Visualisasi Data: Menampilkan tren penjualan bulanan (Line Chart) dan produk terlaris (Bar Chart) menggunakan Plotly.

RFM Analysis: Mengelompokkan pelanggan ke dalam segmen (VIP/Loyal, Regular, Low Spender, At Risk) berdasarkan Recency, Frequency, dan Monetary.

🛠️ Prasyarat (Requirements)
Pastikan Python sudah terinstal di sistem Anda. Anda memerlukan pustaka berikut untuk menjalankan proyek ini:

pandas

streamlit

plotly

Anda dapat menginstalnya menggunakan pip:

Bash
pip install pandas streamlit plotly
⚙️ Cara Menjalankan Aplikasi
Langkah 1: Hasilkan Data Penjualan
Sebelum menjalankan dasbor, Anda harus membuat dataset (berupa file CSV) terlebih dahulu dengan menjalankan skrip berikut:

Bash
python generate_data.py
Skrip ini akan membuat folder data dan menyimpan file sales_data.csv di dalamnya.

Langkah 2: Jalankan Dasbor Streamlit
Setelah data berhasil dibuat, jalankan aplikasi web Streamlit menggunakan perintah berikut:
http://localhost:8501).
Bash
streamlit run dashboard.py
Aplikasi akan otomatis terbuka di browser default Anda (biasanya di http://localhost:8501).
