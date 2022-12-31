#SORU 1-:Aşağıdaki kod bloğun çıktısı?

# mylist=[1,2,3,4,5,6,7]
# youlist=[1,2,3,4,5,6,7]

# def index():
#     if len(mylist) == len(youlist) and mylist[3]==4:
#         print(mylist[len(mylist)-len(youlist)])
#     else:
#         print(youlist[0:3])
        
# index()



#SORU 2-:Aşağıdaki kod bloğun çıktısı?

# mylist=[1,2,3,4,5,6,7]
# a=5
# while len(mylist)==7:
#     for i in mylist:
#             a+=1
#             mylist.pop()
#             break
# print(a) :


       
#SORU 3-:Aşağıdaki kod bloğun çıktısı?

# sayilar = [1,2,3,4,5,6]
# yeniListe = []
# a=2
# for sayi in sayilar:
#     if sayi % 2 == 0:
#       yeniListe.append(sayi * sayi)
#     if len(yeniListe)==len(sayilar):
#         a+=sayi
      
# print(yeniListe) 
# print(a) 
    
    
#SORU 4-:Aşağıdaki kod bloğun çıktısı?


# def Main():
#     sayilar = [1,2,3,4,5,6,7,8,9]
#     yeniliste=[]
#     a=0
#     b=3
#     for i in sayilar :
#         if i % 2 !=0 or a==b:
#             yeniliste.append(i)
#         else:
#            for k in yeniliste:
#                a += k
            
#     print(yeniliste)
#     print(a)
        
# Main()

#SORU 5:
#Aşağıdakilerden hangisinde Class Yapısı doğru yazılmııştır?

#A)class Ogrenci:
        #def __init__(self,isim,soyisim):
        #self.isim=isim
        #self.soyisim=soyisim

#B)class isim:
        #def init_(self,isim,soyisim)

#C)class isim:
        #pass

#D)class main:
        #self.isim
        #self.soyad
        
#E)class Main:
        #self.isim
        #self.soyad
        
        
#SORU 6:
#Aşağıdakilerden hangisinde okuma işlem doğru yazılmııştır?

#A) a = open("deneme.txt","w")
    #a.write("python bootcamp")
    #a.close()

#B   a = open("deneme.txt","w")
    #a.close()

        
#C) a = open("deneme.txt","r")
    #a.read("python bootcamp")
    #a.close()
    
#D) a = open("deneme.txt","r+")
    #a.read("python bootcamp")
    #a.close()
    
#SORU 7:
#Aşağıdakilerden hangisinde  Hata Yönetimin'deki "finally" anlamı doğru tanımlanmıştır?

#A)finally ifadesini gerçek dünya problemlerinde her zaman yürütülmesi gereken işlerde kullanabilir.
#B)finally ifadesini hata yönetiminde son hatayı belirtmek için kullanılır.
#C)finally ifadesini "SyntaxError" hatası alındığı zaman kullanılır.
#D)finally ifadesini "NameError" hatası alındığı zaman kullanılır.


#SORU 8:
#Aşağıdakilerden hangisinde  Pyhton Flask'da "if-else" ifadesi doğru tanımlanmıştır?

#A):
# {% if secenek == 1 %}
    # <p>secenek 1</p>
    
    # {% else %}
    # <p>diger secenekler</p>
    # {% endif %}
    
#B):
# {$ if secenek == 1 $}
    # <p>secenek 1</p>
    
    # {$ else $}
    # <p>diger secenekler</p>
    
    
#C):
# if secenek == 1 
    # <p>secenek 1</p>
    
#  else: 
    # <p>diger secenekler</p>
    
#D):
# if secenek == 1 
    # %println(secenek 1)%
    
#  else: 
    # %println(diger secenekler )%
    

#SORU 9-:Aşağıdaki kodun bloğun çıktısı?

# def ikiKati(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 2
#         return wrapper

# def kareAl(func):
#   @wraps(func)
#   def wrapper(*args, **kwargs):
#      result = func(*args, **kwargs)
#      return result * result
    
#   return wrapper


#!!!!!Soru burası!!!!:
# @ikiKati
# @kareAl
# def topla(a,b):
#     return a+b

#print(topla(2,3))


#SORU 10-:Aşağıdaki kodun bloğun çıktısı?

# def main():
#     try:
#         func()
#         print("func cagrildi")
#     except ZeroDivisionError:
#         print("Zero hata alındı")
#     except:
#         print("hata var")
        
# def func():
#     print(1/0)


#main()

#SORU 11-:Aşağıdaki kod bloğun çıktısı?

# a=["he","she","we"]

# b=''.join(a)
# print(b)

#SORU 12-:Aşağıdaki kod bloğun çıktısı?

# a=[[3, 4], [5,6 ]]

# sum=1

# for i in a:
#     for j in i:
#         if j > 4:
#             sum = sum *j
            
# print(sum)



#SORU 13-:Aşağıdaki kod bloğun çıktısı?
# i=1
# c=0

# while (i < 8):
#     if((i !=4) or (not (i > 6))):
#         c += i
#         i += c
            
# print(c)

#SORU 14-:Aşağıdaki kod bloğun çıktısı?

# a=[]

# sum=0

# for i in range(1,8,2):
#     if i < 6:
#         a.append(i)
#         break
        
# else:
#         for k in a:
#             sum +=k
            

# print(sum)

#SORU 15-:Aşağıdaki kod bloğun çıktısı?

# a=[1,2,23,44,55]

# for i in a:
#     print(i)
  
# else:
#     print("emre")    


#SORU 16-Aşağıdaki kod bloğun çıktısı?

# a=[]

# c=0

# for i in range(1,10,2):
#     if i < 5:
#         continue
#     a.append(i)
    
# else:
#     for k in a:
#         c +=k
    

# print(c)
    

#SORU 17-:Aşağıdaki kod bloğun çıktısı?

# a=[1,2,3,4,5]

# def main():
#     return a 


# xyz=0

# for i in main():
#     if a[i-1] < 4:
#         xyz += i
    
# print(xyz)

#SORU 18-:Aşağıdaki kod bloğun çıktısı?

# a=6
# xyz=0

# while a:
#     if a < 4:
#         xyz += a
     
#     a -= 3
# else:
#     xyz +=a +1    
    
# print(xyz)

#SORU 19:

#Aşağıdakilerden hangisinde  Pyhton Flask'da "render_template" ifadesi doğru tanımlanmıştır?

#A) return render_template(%"index.html", book%)

#B)return render_template("index.html")

#C)return render_template(%"index.html", go_page%)
 
#D)return render_template("index.html", book=book)


#SORU 20:
#Aşağıdakilerden hangisinde  Hata Yönetimin'deki "raise" anlamı doğru tanımlanmıştır?

#A)Hata fırlatma "raise" anahtar kelimesi ile yapılır. 

#B)"finally" ifadesi için eş anlamda kullanılabilir.

#C)"Try" içerisinde kullanılan bir anahtar kelimedir. 

#D)"raise" kelimesi ZeroDivisionError belirtirken kullanılabilir.

#SORU 21:
#Aşağıdakilerden hangisinde "start_swith" anlamı doğru tanımlanmıştır?

#A)Tanımladımız bir değişkenin,verdiğimiz kelime ile başlıyormu diye kontrol eder.
    #Örnek:a="emre"  x=a.startswith("em")  print(x=TRUE) 

#B)Tanımladımız bir değişkenin,ilk index'deki elemanını alır.
    #Örnek:a="emre"  x=a.startswith() print(x=[e]) 

#C)Tanımladımız bir değişkenin,kaç index'i elemanlı olduğunu gösterir.
   #Örnek:a="emre"  x=a.startswith() print(x=[4]) 


#D)Tanımladımız bir değişkenin,ilk elemanını siler. 
   #Örnek:a="emre"  x=a.startswith() print(x="mre") 