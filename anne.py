#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anne Soru Bombardımanı Simülatörü v1.0
Türk annesinin süper gücü: Sonsuz soru sorma yeteneği.
"""

import random
import time
import sys

# Gizli kod: base64 ile saklanmış (decode etmeye çalışma, boşuna)
# aGVya2VzIGl5aSBkZSBvbHNhIGJ1IGdlbGVja2VnaW4ga29udXNtdQ==

sorular = [
    "Yemek yedin mi?",
    "Ne zaman eve geleceksin?",
    "O kızla/oğlanla ne oluyor?",
    "Para yetiyor mu?",
    "İş nasıl gidiyor?",
    "Akrabalara selam söyle",
    "Kilo verdin mi yoksa aldın mı?",
    "Ne zaman evleneceksin?",
    "Çocuk yapmayacak mısın?",
    "Telefonun şarjı var mı?",
    "Hava soğuk, kalın giyin",
    "Komşu teyze sordu, sen nasılsın?",
    "Bu akşam ne yiyeceksin?",
    "Arkadaşlarınla görüşüyor musun?",
    "Doktor kontrolüne gittin mi?",
    "Ev kirli mi, temizle",
    "Baban sordu, her şey yolunda mı?",
    "Sen çok çalışıyorsun, dinlen biraz",
    "Bu kıyafet sana yakışmamış",
    "Ne zaman tatile çıkacaksın?"
]

def anne_bombardi():
    print("\n" + "="*50)
    print("   ANNE SORU BOMBARDIMANI BAŞLADI")
    print("   Kaçış şansı: %0")
    print("="*50 + "\n")
    
    seviye = 1
    while True:
        soru = random.choice(sorular)
        
        # Seviyeye göre şiddet artışı
        if seviye > 5:
            soru = soru.upper() + " !!!"
        if seviye > 10:
            soru = "OĞLUM/KIZIM!!! " + soru
        if seviye > 15:
            soru = soru + " Cevap versene!"
        
        print(f"[Seviye {seviye}] Anne: {soru}")
        
        # Rastgele bekleme (gerçekçi anne temposu)
        bekleme = random.uniform(0.5, 3.0)
        time.sleep(bekleme)
        
        # Ara sıra ek yorum
        if random.random() < 0.3:
            ekler = [
                "Hadi cevap ver.",
                "Duymadın mı?",
                "Telefona bakıyorsun herhalde.",
                "Komşu da sordu aynı şeyi.",
                "Ben senin iyiliğin için soruyorum."
            ]
            print(f"         Ek: {random.choice(ekler)}")
        
        seviye += 1
        
        # Sonsuz döngü, Ctrl+C ile kurtulabilirsin (belki)
        if seviye % 20 == 0:
            print("\n--- Anne nefes alıyor... 3 saniye ---\n")
            time.sleep(3)

if __name__ == "__main__":
    try:
        anne_bombardi()
    except KeyboardInterrupt:
        print("\n\nKaçtın! Ama annen biliyor... Bir dahaki sefere daha hızlı soracak.")
        sys.exit(0)
