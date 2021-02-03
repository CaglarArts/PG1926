class Okul:
    def __init__(self, sinifSayisi, ogrenciSayisi, personelSayisi, okulduzeyi, kapalisporsalonu):
        self.sinifsayi = sinifSayisi
        self.ogrencisayi = ogrenciSayisi
        self.personelsayi = personelSayisi
        self.okulduzeyi = okulduzeyi
        self.sporsalonu = kapalisporsalonu

class Sinif(Okul):
    def __init__(self, ogrenciSayisi, dersSayisi, sinifOgretmeni, sinifbaskani):
        self.ogrencis = ogrenciSayisi
        self.derssayisi = dersSayisi
        self.sinifogretmeni = sinifOgretmeni
        self.sinifbaskan = sinifbaskani

antalyaAnadolu = Okul(18, 537, 47, "lise", "Mevcut")
antalyaAnadolu9A = Sinif(33, 12, "Zeynep OKUYUCU", "Ahmet MADEN")
antalyaAnadolu10B = Sinif(34, 13, "Ömer TOMBUL", "Tuana KAPICI")

basinevleri = Okul(32, 757, 53, "ortaokul", "Mevcut")
basinevleri6C = Sinif(22, 9, "Abdurrahman İNCE", "Mahmut TURAN")
basinevleri7F = Sinif(23, 10, "Namık KURU", "Melih GÖKSEL")

aziziye = Okul(22, 437, 53, "ilkokul", "Mevcut değil")
aziziye1A = Sinif(22, 7, "Ayşegül DİKEN", "Ali ŞAH")
aziziye3C = Sinif(20, 8, "Berke KALECİK", "Mert VEZİR")