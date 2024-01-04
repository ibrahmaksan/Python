
## Counting Sort (Slaytta geçtiği şekilde Karmaşıklığı n+k)

dizi = [3,1,0,9,2,4,1,2,7,5,1,0,1,1]
n = len(dizi)
count = [0]*(max(dizi)+1) ##dizideki en çok eleman kadar yer açacak.
output = [0]*n


for i in range(n):
    count[dizi[i]] += 1

for i in range(1,len(count)): ##kümülatif toplama işlemini hallettik.
    count[i] += count[i-1]

i = n-1

while(i>=0):
    output[count[dizi[i]]-1] = dizi[i]
    count[dizi[i]]-=1
    i-=1

for i in range(n):
    dizi[i]=output[i]

print(dizi)