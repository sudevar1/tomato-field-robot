
import cv2
import numpy as np
from pathlib import Path

# 1. DOSYA YOLUNU BELİRLE
klasor = Path(__file__).resolve().parent
resim_yolu = klasor / "domates.jfif"

# 2. FOTOĞRAFI OKU
resim = cv2.imread(str(resim_yolu))

if resim is None:
    print("Fotoğraf okunamadı!")

else:
    print("Fotoğraf başarıyla okundu!")

    # 3. GÖRÜNTÜNÜN ÖZELLİKLERİNİ ÖĞREN
    yukseklik, genislik, kanal = resim.shape

    print("Yükseklik:", yukseklik)
    print("Genişlik:", genislik)
    print("Kanal sayısı:", kanal)
    print("İlk piksel (BGR):", resim[0, 0])

    # 4. ROI - GÖRÜNTÜNÜN ORTASINI KIRP
    y1 = yukseklik // 4
    y2 = 3 * yukseklik // 4

    x1 = genislik // 4
    x2 = 3 * genislik // 4

    roi = resim[y1:y2, x1:x2]

    print("ROI boyutu:", roi.shape)

    # 5. GÖRÜNTÜYÜ 224x224 BOYUTUNA GETİR
    roi_224 = cv2.resize(roi, (224, 224))

    print("Yeni görüntü boyutu:", roi_224.shape)

    # 6. BGR FORMATINDAN RGB FORMATINA DÖNÜŞTÜR
    roi_rgb = cv2.cvtColor(
        roi_224,
        cv2.COLOR_BGR2RGB
    )

    print("BGR piksel:", roi_224[0, 0])
    print("RGB piksel:", roi_rgb[0, 0])

    # 7. NORMALİZASYON İŞLEMİ
    # Piksel değerlerini 0-255 aralığından
    # -1 ile +1 aralığına dönüştür

    roi_normalize = (
        roi_rgb.astype(np.float32) / 127.5
    ) - 1.0

    print("Normalize görüntü boyutu:", roi_normalize.shape)
    print("Minimum değer:", roi_normalize.min())
    print("Maksimum değer:", roi_normalize.max())
    print("Normalize ilk piksel:", roi_normalize[0, 0])

    # 8. İŞLENMİŞ GÖRÜNTÜYÜ KAYDET
    kayit_yolu = klasor / "domates_224.jpg"

    basarili = cv2.imwrite(
        str(kayit_yolu),
        roi_224
    )

    if basarili:
        print("Görüntü başarıyla kaydedildi!")
    else:
        print("Görüntü kaydedilemedi!")

    # 9. GÖRÜNTÜLERİ EKRANDA GÖSTER
    cv2.imshow("Orijinal Goruntu", resim)
    cv2.imshow("Kirpilan ROI", roi)
    cv2.imshow("224x224 Goruntu", roi_224)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
