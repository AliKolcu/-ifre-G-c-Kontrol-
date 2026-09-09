# =========================================
# Şifre Gücü Kontrol Sistemi
# =========================================
# Hazırlayan: Ali Muharrem Kolcu
# Açıklama: Bu proje girilen şifrenin belirli güvenlik 
# kriterlerini karşılayıp karşılamadıgını kontrol etmek
# amacıyla hazırlanmıştır.
#
# Kontrol Edilen Özellikler:
# En az 8 karakter
# Büyük harf
# Küçük harf
# Rakam
# Özel karakter
# Kullanılan Python Konuları:
# Fonksiyon
# if / else
# any() fonksiyonu
# string metotları
# input() ve print()
# =========================================


# Şifrenin gücünü kontrol eden fonksiyon
def sifre_gücü(sifre):
    # Şifrede büyük harf olup olmadığını kontrol eder
    upper = any(c.isupper() for c in sifre)
    # Şifrede küçük harf olup olmadığını kontrol eder
    lower = any(c.islower() for c in sifre)
    # Şifrede rakam olup olmadığını kontrol eder
    digit = any(c.isdigit() for c in sifre)
    # Şifrede özel karakter olup olmadığını kontrol eder
    karakter = any(c in "*.+^'!&,:;?\>!" for c in sifre)
    # Şifrenin tüm güvenlik şartlarını kontrol eder
    if len(sifre) < 8 or not (upper and lower and digit and karakter):
        return "zayif"
    else:
        return "güçlü"
# Kullanıcıdan şifreyi alır
sifre=input("Şifre girin:")
# Şifrenin gücünü ekrana yazdırır
print("sifre gücü :",sifre_gücü(sifre))