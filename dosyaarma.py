import os
arama=input("Aramak istedi�iniz dosya ismini girin = ")
konum=input("Aranacak konum (C yada D) =")
print("Aran�yor,bekleyin...")

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
    print("Yanl�� konum girdiniz C yada D konumunu girin.")