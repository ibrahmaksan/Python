
import random
import time

def bubble(dizi2):
    
    for i in range(0,len(dizi2)-1):

        for j in range(0,len(dizi2)-i-1): ## Bu şekilde yazmamızın sebebi en büyük sayı sürekli karşılaştırılarak en sona atılıyor. Onu bir daha işleme
            ##dahil etmek istemiyoruz.
            if(dizi2[j]>dizi2[j+1]):
                temp = dizi2[j]
                dizi2[j] = dizi2[j+1]
                dizi2[j+1] = temp

    return dizi2

def insertion(dizi):
    adım = 0
    for i in range(1,len(dizi)):

        key = dizi[i]

        for j in range(i-1,-1,-1):

            if(key<dizi[j]):
                temp = dizi[j]
                dizi[j] = key
                dizi[j+1] = temp
                key = dizi[j]
            else:
                break

        adım+=1
    return dizi

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Diziyi ikiye böl

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Sol yarıyı sırala
        merge_sort(right_half)  # Sağ yarıyı sırala

        i = j = k = 0

        # İki alt diziyi birleştir
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Eğer sol yarıdan eleman kalmışsa
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Eğer sağ yarıdan eleman kalmışsa
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
        return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # İlk başta, minimum elemanın indeksi i olarak kabul edilir
        min_index = i

        # Dizideki minimum elemanın indeksini bul
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Minimum elemanı bulunan yerle değiştir
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def heapify(arr, n, i):
    largest = i  # En büyük elemanın indeksi
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Sol çocuk, kökten daha büyükse
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    # Sağ çocuk, en büyük olan sol çocuktan daha büyükse
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    # Kök, en büyük değilse, yer değiştir ve alt ağacı heapify işlemine tabi tut
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    return arr


def heap_sort(arr):
    n = len(arr)

    # Max heap oluştur
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Heap'tan elemanları çıkararak sırala
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Kökü, sıralı kısmın sonundaki elemanla değiştir
        heapify(arr, i, 0)  # Yeniden heapify işlemine tabi tut
    
    return arr





while(1):
    secim = int(input("1-Buble\n2-Insertion\n3-Selection\n4-Merge\n5-Heap"))
    dizi = []

    for i in range(10000):
        dizi.append(random.randint(0,100))
    
    start = time.time()

    if(secim == 1):
        dizi = bubble(dizi)
    elif(secim ==2):
        
        dizi = insertion(dizi)
    
    elif(secim == 3):
    
        dizi = merge_sort(dizi)
    
    elif(secim == 4):
    
        dizi = selection_sort(dizi)
        
    elif(secim == 5):
        
        dizi = heap_sort(dizi)
        
    else:
        print("Hatalı bir tuşlama yaptınız")
        break;

    end = time.time()

    print("Dizi : ",dizi)
    print(end-start)





