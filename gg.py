class Hewan:
  def __init__ (self, nama, jenis, umur):
    self.nama = nama # atribut nama
    self.jenis = jenis # atribut jenis
    self.umur = umur # atribut umur
    def bersuara(self):
     print(f"{self.nama} mengeluarkan suara")
def info(self):
     return f"Nama: {self.nama}, Jenis: {self.jenis}, Umur: {self.umur} tahun"
# Membuat objek dari class Hewan
kucing = Hewan("Kitty", "Kucing", 3)
anjing = Hewan("Rex", "Anjing", 5)
# Mengakses atribut dan method
print(kucing.info())
kucing.bersuara()
print(f"Umur: {anjing.umur} tahun")
