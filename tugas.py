import tkinter as tk
from tkinter import messagebox

# ================= KNOWLEDGE BASE =================
knowledge_base = {
    "Tonsilitis": {
        "gejala": ["G37","G12","G5","G27","G6","G21"],
        "solusi": "Istirahat dan minum hangat"
    },
    "Sinusitis Maksilaris": {
        "gejala": ["G37","G12","G27","G17","G33","G36","G29"],
        "solusi": "Dekongestan dan uap hangat"
    },
    "Sinusitis Frontalis": {
        "gejala": ["G37","G12","G27","G17","G33","G36","G21","G26"],
        "solusi": "Kompres hangat"
    },
    "Sinusitis Edmoidalis": {
        "gejala": ["G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"],
        "solusi": "Periksa ke dokter"
    },
    "Sinusitis Sfenoidalis": {
        "gejala": ["G37","G12","G27","G17","G33","G36","G29","G7"],
        "solusi": "Segera ke dokter"
    },
    "Abses Peritonsiler": {
        "gejala": ["G37","G12","G6","G15","G2","G29","G10"],
        "solusi": "Penanganan medis segera"
    },
    "Faringitis": {
        "gejala": ["G37","G5","G6","G7","G15"],
        "solusi": "Istirahat"
    },
    "Kanker Laring": {
        "gejala": ["G5","G27","G6","G15","G2","G19","G1"],
        "solusi": "Segera periksa dokter"
    },
    "Deviasi Septum": {
        "gejala": ["G37","G17","G20","G8","G18","G25"],
        "solusi": "Operasi jika perlu"
    },
    "Laringitis": {
        "gejala": ["G37","G5","G15","G16","G32"],
        "solusi": "Istirahat suara"
    },
    "Kanker Leher & Kepala": {
        "gejala": ["G5","G22","G8","G28","G3","G11"],
        "solusi": "Periksa dokter"
    },
    "Otitis Media Akut": {
        "gejala": ["G37","G20","G35","G31"],
        "solusi": "Obat nyeri"
    },
    "Contact Ulcers": {
        "gejala": ["G5","G2"],
        "solusi": "Istirahat bicara"
    },
    "Abses Parafaringeal": {
        "gejala": ["G5","G16"],
        "solusi": "Penanganan medis"
    },
    "Barotitis Media": {
        "gejala": ["G12","G20"],
        "solusi": "Hindari tekanan"
    },
    "Kanker Nafasoring": {
        "gejala": ["G17","G8"],
        "solusi": "Periksa dokter"
    },
    "Kanker Tonsil": {
        "gejala": ["G6","G29"],
        "solusi": "Penanganan medis"
    },
    "Neuronitis Vestibularis": {
        "gejala": ["G35","G24"],
        "solusi": "Obat vertigo"
    },
    "Meniere": {
        "gejala": ["G20","G35","G14","G4"],
        "solusi": "Kurangi garam"
    },
    "Tumor Syaraf Pendengaran": {
        "gejala": ["G12","G34","G23"],
        "solusi": "Pemeriksaan lanjut"
    },
    "Kanker Leher Metastatik": {
        "gejala": ["G29"],
        "solusi": "Segera ke dokter"
    },
    "Osteosklerosis": {
        "gejala": ["G34","G9"],
        "solusi": "Alat bantu dengar"
    },
    "Vertigo Postural": {
        "gejala": ["G24"],
        "solusi": "Terapi posisi"
    }
}

# ================= DATA GEJALA =================
gejala_list = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Air liur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri hidung",
    "G14": "Vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tidak seimbang",
    "G24": "Bola mata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Benjolan di mulut",
    "G29": "Benjolan leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Lemas",
    "G37": "Demam"
}

# ================= APP =================
class SistemPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa THT")
        self.root.geometry("500x330")

        self.index = 0
        self.gejala_user = []
        self.kode_gejala = list(gejala_list.keys())

        self.label = tk.Label(root, text="Sistem Pakar Diagnosa THT", font=("Arial", 12))
        self.label.pack(pady=15)

        self.label_nomor = tk.Label(root, text="")
        self.label_nomor.pack()

        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai)
        self.btn_mulai.pack(pady=10)

        self.frame = tk.Frame(root)

        self.btn_ya = tk.Button(self.frame, text="YA", width=10, command=lambda: self.jawab("y"))
        self.btn_tidak = tk.Button(self.frame, text="TIDAK", width=10, command=lambda: self.jawab("t"))

        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai(self):
        self.index = 0
        self.gejala_user = []

        self.btn_mulai.pack_forget()
        self.frame.pack(pady=20)
        self.tanya()

    def tanya(self):
        total = len(self.kode_gejala)

        if self.index < total:
            kode = self.kode_gejala[self.index]

            self.label.config(text=f"Apakah Anda mengalami:\n{gejala_list[kode]}?")
            self.label_nomor.config(text=f"Pertanyaan {self.index+1} dari {total}")

        else:
            self.proses()

    def jawab(self, jwb):
        if jwb == "y":
            self.gejala_user.append(self.kode_gejala[self.index])

        self.index += 1
        self.tanya()

    def proses(self):
        # CEK kalau tidak ada gejala
        if not self.gejala_user:
            messagebox.showinfo("Hasil", "Tidak ada gejala dipilih")
            return

        skor_max = -1
        hasil = ""
        solusi = ""

        for penyakit, data in knowledge_base.items():
            skor = sum(1 for g in data["gejala"] if g in self.gejala_user)

            if skor > skor_max:
                skor_max = skor
                hasil = penyakit
                solusi = data["solusi"]

        total = len(knowledge_base[hasil]["gejala"])
        persen = (skor_max / total) * 100

        messagebox.showinfo(
            "Hasil Diagnosa",
            f"Penyakit: {hasil}\n"
            f"Kecocokan: {persen:.0f}%\n\n"
            f"Solusi:\n{solusi}"
        )

        self.frame.pack_forget()
        self.btn_mulai.pack()
        self.label.config(text="Diagnosa selesai. Coba lagi?")
        self.label_nomor.config(text="")

# ================= RUN =================
root = tk.Tk()
app = SistemPakar(root)
root.mainloop()
