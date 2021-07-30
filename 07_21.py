#Python Notes
#Numbers: Integer&Float
print(2)
print(2+3)
print(type(3))
print(3.)
print(2.7)
print(7.0)
print(type(1.))

#Boolean Type: 
print(type(True))
print(type(False))
print(2>3)
print(type(5>3))

#-------------------------TYPE CASTING------------------------- it just take the integer part, it doesn't round up
print(int(2.4))
print(float(-70))

#----------------------VARIABLE ASSIGNMENT----------------------
a=3
print(a)
print(a-2)

print(a+9)
b=3-8 #Variable=Expression
print(b)
print(b+9)
b=a+5
print(b)
a=a+3 
print(a)
a-=2
print(a)

#integer division
print(7//2)
print(5//2.5)
print(5//2.0)

#exponentiate  5²
print(5**2)
print(5**-1)

#String Type=Nonscalar
print(type("3"))
print(type('-2'))

print("5"+"7")
print("5+10")

#Escape Sequences   \" or \'
print("Bana \"İspanya'ya gidecek misin\" diye sordu")
print('Bana "İspanya\'ya gidecek misin" diye sordu ')

# \n : new line         \t: tab 
print("İsim\nSoyisim")
print("İsim \nSoyisim")
print("İsim\n Soyisim")
print("T.C. No\tDoğum Tarihi")

#to print \
print("Şişli\\İstanbul")

merhaba = "Merhaba nasılsın bugün?"
print(merhaba)

print("merhaba"+"ben"+"Ayşe")
print("merhaba "+"ben "+"Ayşe")
print("merhaba"+" "+"ben"+" "+"Ayşe")

mesaj="Kendine iyi bak"
isim="Can"
print(mesaj+" "+isim)

#Succesive Concatenation
print(4*"ha")
print("1"+7*("0"))
print(type("1"+7*("0")))

#len()
print(len("4857600869903"))
print(len("Orta Doğu Teknik Üniversitesi "))
print(len(" "))
#--------------------------------------------
def split_and_join(line):
     a = line.split(" ")
     a = "-".join(a)
     return a
if __name__ == '__main__':
    line = "Benim adım Deniz"
    result = split_and_join(line)
    print(result)
#--------------------------------------------
def split_and_join(line):
     a = line.split("?")
     a = "-".join(a)
     return a
if __name__ == '__main__':
    line = "ben?futbol?oynamayı?çok?severim"
    result = split_and_join(line)
    print(result)    

#Indexing
isim="Deniz"
print(isim[3])
print("Deniz"[1])
print(isim[-1])     #Give the last element
print(len(isim))

#Slicing
print(isim[0:4])    #include 0th but not include 4th
print(isim[0:])     #From the beginning to the end
print(isim[:])      #From the beginning to the end
print(isim[:len(isim)]) #From the beginning to the end
print(isim[2:])     #To the end
print(isim[:3])     #From the begginning
print(isim[3:20])   #takes it as far as it can[the end]
print(isim[::2])
print(isim[0:3:2])  #[beggining:the end :step]
print(isim[::-1])   #reversing
print(isim[::-2])
print(isim[10:0:-1])

#Casting in strings
a="4"
print(int(a))
print(type(int(a)))
b="5.3"
print(float(b))
print(type(float(b)))
print(int(float(b)))

x=input("Enter an integer:")
print(type(x))

y=int(input("Enter an integer:"))
print(type(y))

mesaj = input("Mesajı girin:")
isim = input("İsim girin:")
print(mesaj + " " + isim)

print("elma" == "elma")
print("ab" < "b")
print("abc" < "abb")

#Logical Operators 
print(not True)
print(not not True)
print(True and True)
print(False and True)
print(False and False)
a=4
b=6
c=8
print((a<b) and (b<c))
print((a>b)and (b<c))
print(True or True)
print(False or False)
print((a>b) or (b<c))

#Short Circuit
print((5<3) or print("Hey"))
print((5>3) or print("Hey"))

#if-else
x=int(input("x değerini giriniz"))
if x%2 == 0:
   print("Sayımız çifttir.")
else:
    print("Sayımız tektir.")
print("Programımız sona ermiştir.")

#if-else-elif
x=int(input("0 ile 100 arasında bir sayı giriniz."))
if x == 100:
    print("Sayınız 100'e eşit.")
elif x >= 90:
    print("Sayınız 90 ile 100 arasında.")
elif x >= 80:
    print("Sayınız 80 ile 90 arasında.")
else:
    print("Sayınız 0 ile 80 arasında.")
print("Programımız sona ermiştir.")

#nested if(iç içe loop)
x=int(input("Bir sayı giriniz:"))
if x%3 == 0: 
    if x%2 == 0:
        print("Sayı hem 3'e hem 2'ye bölünüyor.")
    else:
        print("Sayı 3'e bölünüyor, 2'ye bölünmüyor.")
else:
    print("Sayı 3'e bölünmüyor.")
print("Programımız sona ulaştı.")
#---------------------------------------------------------
x=int(input("Bir sayı giriniz:"))
if x % 2 ==0 and x % 3 == 0:
    print("Sayınız 3'e ve 2'ye tam bölünüyor.")
print("Programımız sona ulaştı.")
#---------------------------------------------------------
cevap = input("x in değeri 2 olsun mu? y/n")

if cevap == "y": # cevap == "y" testimiz oluyor
    x = 2
else:
    x = 0

print(x)

#Ternary Conditionals
cevap = input("x in değeri 2 olsun mu? y/n")
x = 2 if cevap=="y" else 0
print(x)

#While
x=int(input("Lütfen bir sayı giriniz:"))
while x % 3 !=0 :
    x=int(input("Sayı 3'e bölünmüyor. Lütfen yeni bir sayı giriniz:"))
print("Sayınız 3'e bölünüyor ve sayınızın 3'e bölümü",x/3)
 #-----------------------------------------------------------------------
a = -7
while a<5:
     print(a)
     a+=3
#program to add even integers from 0 to 50 
toplam=0
x=0
while x<=50:
    x+=2
    toplam=toplam+x
print(toplam)

#for
for i in "Kahramanmaraş":
    print(i)
#-------------------------------------------
toplam=0
for a in range(51):
    toplam=toplam+a
print(toplam)
#--------------------------------------------
for i in range(5):
    print(i)
#--------------------------------------------
üs=1
for i in range(5):
    üs*=5
print(üs)

#Break
for i in range(10):
    if i == 3:
        break
    print(i)
#--------------------------------------------
x = 0

while x < 10:
    print(x)
    x += 1
    if x == 3:
        break  
#continue
for i in range(10):
    
    if i == 3:
        continue
    print(i)  

#List
notlar = [78, 80, 43, 65, 90]
print(notlar[0])
print(notlar[1:3])
notlar[0:3]=92,87,50
print(notlar)
notlar[0:3]=91,78 #Hata verir
print(notlar)
print(len(notlar))
#append():add an element at the end
notlar.append(25)
print(notlar)
#extend([]):add several elements at the end
notlar.extend([95,54,67])
print(notlar)
#insert(index,object):add an element at specific point and each index greater than 3 increase 1 
notlar.insert(3, 100)
print(notlar)
#remove():Delete an existing element from list
notlar.remove(78)
print(notlar)
#pop():delete an specific element or return its value
notlar.pop(2) #delete
print(notlar)
print(notlar.pop(1)+8) #return its value 
#count(obj):Prints how many times 1 element is written.
print(notlar.count(91))
print(notlar.count(68))
#Aliasing: 
a = 2
b = a
print(b)
a = a + 1
print(a) #güncel
print(b) #güncel değil 
l = [1,2,3]
l2 = l
print(l)
print(l2)
l[0] = 200
print(l) #güncel
print(l2) #güncel

#copy
l2 = l.copy()
print(l)
print(l2)
l[0] = 300
print(l) #güncel
print(l2) #güncel değil 
#List Concatenation
l1=[0.2,0.7,3.6]
l2=[7.1,5.0,4.2]
print(l1+l2)
#finding index
print(l1.index(3.6))
print(l2.index(5.0))
#reverse
l1.reverse() #l1i günceller
print(l1)
print(l2[::-1])#l2yi güncellemez, atama yapman gerekir 
print(l2)
l3=l2[::-1]
print(l3)
#Sorting:
l=["s","y","k","n"]
lst=sorted(l)
print(sorted(l)) #güncellemez
print(l)
print(lst)
l.sort() #günceller
print(l)
lst2=[1,-7,5,44,63,17,-4,0]
print(sorted(lst2))
mylst=[[46,-7,22,0,-14],[45,87,2,-1,-44]] #sadece ilk elemanlara bakarak sıralama yapar
print(sorted(mylst))
mylst2=[[46,-7,22,0],[46,-9,4,45]] 
print(sorted(mylst2))

#Tuple
x = 10
y = 34
konum = (10, 34)
print(konum[0]) #indexing
print(konum[:])
t = (1,2,3,"a")
print(t)
t = ((1,2),3)
print(t)
print(t[0])
t = ([1,2,3],2,(1,2))
t[0][0] = 23
print(t)
x = 2
y = 3
(x, y) = (y, x)
print(x)
print(y)
l = [1,2,3,4]
print(40 in l) #eleman  kontrolü
l=83,5,6,7
print(83 in l)
#set
s={1,2,3,1} #1,2,3 bastırır
print(s)
a={} #empty set
print(type(a))
l = [1,2,3,4,1,2]
print(set(l))
#setler indexlenemez,elemanları değiştirilebilir
s.add(8)
print(s)
s.remove(1)
print(s)
#discard:remove gibi çalışır. Olmayan elemanı silmeye çalışırsan hata vermez.True
#difference
s1 = set([1,5,10])
s2 = set([2,5,3])
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)
#symmetric difference
print(s1.intersection(s2))
print(s2.intersection(s1))
print(s1&s2)
#union
print(s1.union(s2))
print(s2.union(s1))
#disjoint or not
print(s1.isdisjoint(s2))
#subset or not
print(s1.issubset(s2))
s3=set([2,5])
#superset
print(s2.issuperset(s3))
s = set('HackerRank')
print(s)
s.add('HackerRank')
print(s)
#-------------------------------------------
notlar=[90,72,81,40]
t = 0
for e in notlar:
    print(e)

for e in notlar:
    t += e
    
ortalama = t / len(notlar)

print("Ortalama:",ortalama)
toplam=0
for i in range(len(notlar)):
    toplam+=notlar[i]
ortalama=t/len(notlar)
print("Ortalama:",ortalama)
#----------------------------
for e in notlar:
    print(e)
    break
#=
for i in range(len(notlar)):
    print(notlar[i])
    break
#her notu 10'ar arttırma:
for e in notlar:
    e+=10
    print(e)
#=
print("Güncel Notlar :")
for i in range(len(notlar)):
    notlar[i]+=10
    print(notlar[i])
    print("------")
# güncel listeyi bastırma : 
for i in range(len(notlar)):
    notlar[i]-=5
print(notlar)
#belirli bir indexin değişmemesi (2.eleman)
for i in range(len(notlar)):
    if i == 1:
        continue
    notlar[i] += 5
print(notlar)
#Bir elemanın varlığını kontrol etme: 
x = int(input("Hangi sayıyı kontrol edeyim?:"))
l = [2,3,40,100,10,1]
for e in l:
    print(e) # iterasyon break ile çıkmış mı görelim mi diye
    if e == x:
        print("Buldum!!")
        break
    else:
        print(x,"i bulamadım.")
#Tuple'lerda İterasyon
t = (1,2,3,4)
for e in t:
    print(e)

toplam = 0
for e in t:
    toplam += e
print(toplam)

for i in range(len(t)):
    print(t[i])
#Dictionary'lerde İterasyon
d = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,71]}
for k in d:
    print(k)

for k in d:
    v = d[k]
    print(v)

print("--------------------")
d = {"student_1": 90, "student_2": 80, "student_3": 72}


for k in d:
    value = d[k]
    if value > 85:
        print(k)
print("--------------------")
for k,v in d.items():
    print("key değeri:", k, "value değeri:", v)
#x.split() 
s="Kart Numaranızı Giriniz:"
print(s.split())#boşluğa göre ayırıyor
x="sen-markete-gidecek-misin"
print(x.split("-"))#"-" a göre ayırıyor
s2="Mehmet,Ayşe,Burak,Serkan,İrem"
print(s2.split(","))
#"x".join(l)
l=["limon","portakal","nar"]
print(",".join(l))
print(l)

ilçe=input("İlçe giriniz:")
şehir=input("Şehir giriniz:")
x=[ilçe,şehir]
print("/".join(x))

print("-----------")
squares = []
for i in range(1,11):
      squares.append(i*i)
print(squares)
#Bunun aynısını list comprehension kullanarak da yapabiliriz.
squares = [i * i for i in range(1,11)]
print(squares)
#Cube
def cube(x):
    return x*x*x
cubes=[cube(x) for x in range(-6,6)]
print(cubes)
#=
cubes=[x**3 for x in range(-6,6)]
print(cubes)

even_squares=[]
for e in squares:
    if e%2==0:
        even_squares.append(e)
print(even_squares)
#----------------------------------------
def is_odd(x): 
    if x % 2 == 0:
        return False
    if x % 2 == 1:
        return True
odd_squares = [e for e in squares if is_odd(e)]
print(odd_squares)
#----------------------------------------
def empty(x): 
    if x % 2 == 0:
        return False
    if x % 2 == 1:
        return False
empty_squares = [e for e in squares if empty(e)]
print(empty_squares)
#----------------------------------------
weird_squares = [e if e % 2 == 0 else -1 for e in squares]
print(weird_squares)
#Set Comprehension
numbers = [1,2,3,4,5,6,7,1,2]
set_numbers = {s for s in numbers if s in [1,2,3,4,5,6,1,2]}
print(set_numbers)
#Dictionary Comprehension
square_dict = {e:e * e for e in range(1,11)}
print(square_dict)
print(square_dict[9])
#Nested List Comprehension
m = [[j for j in range(7)] for i in range(5)]
print(m)
#-------------------------------------------
new_m = []
for l in m:
    print(l)
    for e in l:
        new_m.append(e)
        print(e)
#variable unpacking: 
x,y,z=(6,7,8)
a,_=(5,99) # _: Kullanmayacağını belirtir.
x,y,*z=(1,9,6,7,8,5,21) #*z: kalan elamanları eşitler
print(x)
print(y)
print(z)
print(type(z)) #tek değer olsa bile list döndürür 
x,*y,z=(1,2,3,4)
print(y)
#*ı sadece 1 kere kullanabilirsin , error verir
x, y, *_ = (4, 7, 11, 12, 13)
print(x)
print(y)
#Enumerate
l = [(1,2), (10,20)]
for e in l:
    print(e)


for e in l:
    a, b = e
    print(a)
    print(b)
    print("*********")

for a, b in l:
    print("tuple'ın ilk elemanı", a)
    print("tuple'ın ikinci elemanı", b)
    print("-----------------------------")
    #enumerate() bize (index, element) olarak verecek.
adlar = ['Tyler', 'Blake', 'Cory', 'Cameron']
for e in adlar:
    print(e)

for i, e in enumerate(adlar):
    print(i, "indexindeki eleman:", e)
#start
for i, e in enumerate(adlar, start = 100):
    print(i, "lokasyonunda bulunan eleman:", e)

#zip()
satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for i in range(len(maliyet)):
    s = satis[i]
    c = maliyet[i]
    kar = s - c
    print(f'Total profit: {kar}')

print("************************")
satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for s, c in zip(satis, maliyet):
    kar = s - c
    print(f'Total profit: {kar}')
#zip() ile Dictionary Yaratmak:
keys = ['isim', 'soyad', 'ulke', 'is']
values = ['Denis', 'Walker', 'Turkey', 'data scientist']
d = {}
for k, v in zip(keys, values):
    d[k] = v
    print(d)
    print(d["isim"])

#Fonksiyonlar
x=int(input("x'i giriniz"))
y=int(input("y'yi giriniz"))
z=int(input("z'yi giriniz"))
def f(x,y,z):
    return 5*x*x+3*y-z 
print(f(x,y,z))
print(f(3,4,5)) #calling function

def square(x):
    return x*x
print(square(square(2)))

def weird():
    return 5
print(weird())
#Birden çok değer döndüren fonksiyonlar: 
def f(x):
    return 2*x, 10*x
print(f(10))# Type:tuple

#Predefined Parameters : 
def hello(end, start = "Hello"):
   print(start + " " + end)
print(hello("Denis"))

def power(x, y=1):    
    return x ** y
print(power(3))

def f(x, y=1, z=2):  
    return x + y + z
print(f(2))

#Argümanalrın Değerlerinin Güncellenip Güncellenmediği Durumlar 
a=2
def f(x):
    x=4
    return x 
print(a) #a nın değeri değişmedi 

l = [1,2,3]
l2 = l
l2[0]=9
print(l2)
print(l)#bu da değişir

l = [1,2,3]
l2 = l.copy()
l2[0]=9
print(l)#değişmez
print(l2)




""" first class function. Bunun anlamı fonksiyonların diğer veri
 tipleri gibi manipüle edilebilir ve başka fonksiyonlara argüman olarak verilebilir."""
def kare(x):
    return x**2
a=kare #bir fonksiyonu bir değişkene atayabilirisn
print(a(2))
print(kare(5))

def f2(x, f):      # Bir fonksiyonu başka bir fonksiyonun argümanı olarak da verebilirsin 
    return f(x) + 4
print(f2(3,kare))

def f3(x):
    return x**5
print(f2(2, f3)) 
#Fonksiyonları Obje Olarak Kullanmak
l = [1,2,3,4]


def apply(l, f):
    """
    l bir liste, 
    f listenin tüm elemanlarına uygulanacak fonksiyon
    sonunda listenin orijinali elemanlarına fonksiyonun uygulanmış haliyle güncellenir
    """
    n = len(l)
    for i in range(n):
        l[i] = f(l[i])
    
    def kare(x):
        return x**2
apply(l, kare)
print(l)

l = [1,2,3,4]
def kup(x):
    return x**3
apply(l, kup)
print(l)

#Fonksiyonlar Listesini Belirli Bir Değere Uygulamak
def apply_funcs(f_list, x):
    l = []
    for f in f_list:
        l.append(f(x))   
    return l
print(apply_funcs([kare, kup], 5))

#Underscore Placeholders:uzun sayıların okunabilirliğini arttırır
num_1 = 90000000000
num_2 = 90_000_000_000
print(num_1-num_2)

print(num_1)
print(num_2)
print(type(num_2)) #integer

num_3 = 0.12_11_12 #for floats
print(num_3)
print(type(num_3)) #float

#F-string: f-string de yaptığımız tek şey aslında değişkenlerin değerlerini veya hesaplamaların sonucunu stringin içine gömmek.
isim = input("İsim:")
print(f"verilen isim {isim}")

l = [1,2,3,4]
print(f"verilen liste {l}")
#{} içerisine değeri hesaplanacak herhangi bir şey yazılabilir.
print(f"verilen isim {isim.capitalize()}") #Baş harfi büyük yapma

def kare(x):
    return x**2
x = 10
print(f"{x} sayısının karesi {kare(x)}")

""" 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı 
listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]"""
data=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = []
def flatten_list(data):
    for element in data:
        if type(element) == list:
             flatten_list(element)
        else:
             flat_list.append(element)
flatten_list(data)
print(flat_list)
       



""""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
 Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]"""
boyut=int(input("Listenin boyutunu giriniz"))
for i in range(boyut):
    lst[i]=input("Elemanları giriniz:")
def Ters(lst): 
    lst.reverse() 
    return lst      
print(Ters(lst)) 
lst2=[[1, 2], [3, 4], [5, 6, 7]]
print(Ters(lst2))

