

def counting_sort(dizi,exp):

    n = len(dizi)
    count = [0]*10
    output = [0]*n

    for i in range(n-1):
        index = dizi[i]//exp
        count[index%10] += 1

    for i in range(10):
        count[i] += count[i-1]


    i = n-1 ##Bu kısmı kendi yazdığımız counting-sort'a da uyarlayalım.
    while i >= 0:
        index = dizi[i] // exp
        output[count[index % 10] - 1] = dizi[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        dizi[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Örnek kullanım
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)   





print("Siralanmis dizi : ",arr)
    