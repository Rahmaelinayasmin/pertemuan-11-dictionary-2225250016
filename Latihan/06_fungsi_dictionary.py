# Latihan 6: Fungsi Pencarian Dictionary

def cari(data, nim):
    return data.get(nim, "Data tidak ditemukan")


mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "nilai": 85
    },
    "A002": {
        "nama": "Budi",
        "nilai": 78
    }
}

print("Hasil pencarian A002:")
print(cari(mahasiswa, "A002"))

print("\nHasil pencarian A003:")
print(cari(mahasiswa, "A003"))