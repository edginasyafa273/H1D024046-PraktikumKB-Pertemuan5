**README - Sistem Pakar Diagnosa Penyakit THT (GUI Python)**
**1. Deskripsi**

Aplikasi ini merupakan implementasi sistem pakar berbasis aturan (rule-based expert system) untuk melakukan diagnosa awal penyakit THT (Telinga, Hidung, Tenggorokan) berdasarkan gejala yang diinput oleh pengguna.

Aplikasi dibangun menggunakan:

Bahasa: Python
GUI: Tkinter
Metode Inferensi: Forward Chaining

**2. Tujuan**

Mengimplementasikan konsep sistem pakar dalam studi kasus medis
Memahami cara kerja rule-based system
Mengembangkan aplikasi GUI sederhana untuk diagnosa

**3. Konsep Sistem Pakar**

Metode Inferensi: Forward Chaining

Proses kerja sistem:

User memilih gejala
Sistem mengumpulkan fakta (gejala yang dipilih)
Sistem mencocokkan dengan rule pada knowledge base
Sistem menghasilkan diagnosa penyakit

**4. Struktur Data**

**4.1 Knowledge Base (Database Penyakit dan Solusi)**
knowledge_base = {
    "Tonsilitis": {
        "gejala": ["G37","G12","G5","G27","G6","G21"],
        "solusi": "Istirahat dan minum hangat"
    }
}

Penjelasan:

Key = nama penyakit
Value = dictionary yang berisi:
gejala → daftar kode gejala
solusi → penanganan awal

Sistem menggunakan metode pencocokan jumlah gejala (scoring), bukan harus semua gejala terpenuhi.

**4.2 Data Gejala**
gejala_list = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak"
}

Penjelasan:

Key = kode gejala
Value = deskripsi gejala

Digunakan untuk menampilkan pertanyaan kepada pengguna.

**5. Penjelasan Program**
**5.1 Inisialisasi Class**
class SistemPakar:
    def __init__(self, root):

Fungsi:

Membuat tampilan GUI
Menyimpan state aplikasi

**5.2 Variabel Penting**
self.gejala_user = []
self.index = 0

Penjelasan:

gejala_user → menyimpan gejala yang dijawab "YA"
index → penunjuk pertanyaan saat ini

**5.3 Tombol Mulai**
self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai)

Fungsi:

Memulai proses diagnosa
Menghubungkan tombol dengan fungsi mulai()

**5.4 Fungsi mulai()**
def mulai(self):
    self.gejala_user = []
    self.index = 0

Fungsi:

Mereset data sebelumnya
Memulai sesi diagnosa baru

**5.5 Fungsi tanya()**
def tanya(self):
    kode = self.kode_gejala[self.index]
    self.label.config(text=gejala_list[kode])

Fungsi:

Menampilkan gejala berdasarkan urutan
Mengupdate tampilan pertanyaan

**5.6 Fungsi jawab()**
def jawab(self, jwb):
    if jwb == "y":
        self.gejala_user.append(self.kode_gejala[self.index])

Penjelasan:

Jika jawaban YA → gejala disimpan
Jika TIDAK → dilewati

**5.7 Proses Diagnosa**
for penyakit, data in knowledge_base.items():
    skor = sum(1 for g in data["gejala"] if g in self.gejala_user)

Penjelasan:

Sistem mengecek semua penyakit
Menghitung jumlah gejala yang cocok
Penyakit dengan skor tertinggi dipilih

**5.8 Perhitungan Persentase**
persen = (skor_max / total) * 100

Rumus:
Persentase = (jumlah gejala cocok / total gejala penyakit) × 100%

**5.9 Menampilkan Hasil**
messagebox.showinfo("Hasil Diagnosa", hasil)

Fungsi:

Menampilkan hasil diagnosa dalam bentuk pop-up
Berisi penyakit, persentase, dan solusi

**6. Cara Menjalankan Program**
Simpan file dengan nama:
sistem_pakar.py
Jalankan program:
python sistem_pakar.py
Langkah penggunaan:
Klik "Mulai Diagnosa"
Jawab pertanyaan
Lihat hasil diagnosa

**7. Contoh Output**
Penyakit: Tonsilitis
Kecocokan: 67%

Solusi:
Istirahat dan minum hangat

**8. Kelebihan dan Keterbatasan**
Kelebihan
Mudah digunakan
Tampilan sederhana
Proses cepat
Keterbatasan
Hanya berdasarkan gejala yang tersedia
Tidak menggantikan diagnosis dokter
Tidak menggunakan metode lanjutan seperti fuzzy logic

**9. Kesimpulan**
Program ini merupakan implementasi sederhana dari sistem pakar berbasis rule dengan metode forward chaining. Sistem mampu melakukan diagnosa awal berdasarkan kecocokan gejala, namun masih memiliki keterbatasan dalam menangani kompleksitas dan ketidakpastian dalam dunia medis.
