
## Insertion Sort:
def insertion(dizi):
    dizi = [3, 5, 1, 4, 2]
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


