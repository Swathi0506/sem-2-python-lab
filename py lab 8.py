n=input()
c=0
s=0
cap=[]
small=[]
L=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
l=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
for i in n:
    if i in L:
        cap.append(i)
        c+=1
for j in n:
    if j in l:
        small.append(j)
        s+=1
print(c)
print(s)
