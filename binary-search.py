
import math

##Binary search recursive:
def find(sayi,dizi,bas,son):
    
    if (not (sayi in dizi)):
        print("Aranan sayi listede yoktur.")
        return

    orta = math.floor((bas+son)/2)

    if(sayi == dizi[orta]):
        print(f"{dizi[orta]} sayisi {orta}.indextedir.")

    elif(sayi>dizi[orta]):
        find(sayi,dizi,orta+1,son)
                
    elif(sayi<dizi[orta]):
        find(sayi,dizi,bas,orta-1)
    
        
find(6,[1,2,3,4,5,6,7,8,9,10,11,12],0,12)
