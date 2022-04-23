
kelime = input("Kelimeyi giriniz : ")

for i in range(len(kelime)):
    sayı = 0
    belirtec = 1
    for j in range(len(kelime)):
        if(kelime[i] == kelime[j]):
            sayı += 1


    if(i==0):
        print("{} harfinden {} tane var.".format(kelime[i],sayı))
        continue

    m = i-1

    while(m>=0):    
        if(kelime[i] == kelime[m]):
            break
        
        if(m==0):
            print("{} harfinden {} tane var.".format(kelime[i],sayı))     
        m-=1
       
    
