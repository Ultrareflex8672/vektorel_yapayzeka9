# open("deneme.txt") # var olan dosyayı okuma modunda açma
# open("deneme1.txt","w") # var olan dosyayı okuma modunda açma
# d = open("deneme1.txt","w") # var olan dosyayı okuma modunda açma
d = open("deneme1.txt","a") # var olan dosyayı okuma modunda açma
d.write("abc\n")

d = open("deneme1.txt") 
okunan = d.read()
print(okunan)