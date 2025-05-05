kahve = "latte"
boyut = "large"
servis = "out"

kahve_fiyat = {"espresso": 2.5, "latte": 2.5, "mocha": 3.5}
boyut_fiyat = {"medium" : 0.0, "large": 1.0, "xl": 1.5}
servis_fiyat = {"in": 0.0, "out": 1.0}

if kahve in kahve_fiyat and boyut in boyut_fiyat and servis in servis_fiyat:
    toplam = kahve_fiyat[kahve] + boyut_fiyat[boyut] + servis_fiyat[servis]
    print("Toplam fiyat: £") + str(toplam)
else:
    print("Hayalı giriş yaptın, seçenekleri kontrol et!")   
