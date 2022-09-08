f1=open("a.txt")

try:
    f=open("does.txt")

except Exception as e:
    print(e)
    
else:
    print("this will run only if when except is not running")

finally:
    print("run this anyway...")
    f1.close()
print("important stuff")