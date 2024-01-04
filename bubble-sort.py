##Bubble sorting (İkinci yazdığım bubble sort) Sınav için daha iyi
def bubble(dizi2):
    dizi2 = [3,12,1,5,7,4,0]
    for i in range(0,len(dizi2)-1):
        for j in range(0,len(dizi2)-i-1): ## Bu şekilde yazmamızın sebebi en büyük sayı sürekli karşılaştırılarak en sona atılıyor. Onu bir daha işleme
            ##dahil etmek istemiyoruz.
            if(dizi2[j]>dizi2[j+1]):
                temp = dizi2[j]
                dizi2[j] = dizi2[j+1]
                dizi2[j+1] = temp

    return dizi2
 




