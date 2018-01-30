import os
arama=input("Aramak istediðiniz dosya ismini girin = ")
konum=input("Aranacak konum (C yada D) =")
print("Aranýyor,bekleyin...")

if konum=="C":
    os.chdir("C:/")
    for i,j,dosya_isimleri in os.walk("C:/"):
        for a in dosya_isimleri:
                if (a.endswith(arama)):
                    print(a,"bulundu. Konumu = ",i)
elif konum=="D":
    os.chdir("D:/")
    for i,j,dosya_isimleri in os.walk("D:/"):
        for a in dosya_isimleri:
                if (a.endswith(arama)):
                    print(a,"bulundu. Konumu =",i)
else:
    print("Yanlýþ konum girdiniz C yada D konumunu girin.")