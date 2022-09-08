# f=open("m.txt","w") # w jo h vo file ko khali krke fir likhta or agar append krte h to usi file m add krta h
# b=f.write("\n vishal is very hard wroking \n")
# print(b)
# f.close()


# f=open("m.txt","a") # w jo h vo file ko khali krke fir likhta or agar append krte h to usi file m add krta h
# b=f.write("\n vishal is very hard wroking \n")
# print(b)
# f.close()

# HANDLE READ AND WRITE BOTH
f=open("w.txt","r+")
print(f.read())
f.write("\nthank you\n")

b=input("give the input:--")
f.write(b)