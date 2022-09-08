import time
initial=time.time()

k=0
while k<10:
    print("vishal ansari")
    time.sleep(2)  # this is to use to get late....
    k=k+1
print("while loop ran in",time.time()-initial,"seconds")

initial2=time.time()
for i in range(0,10):
    print("thnku bhai")
print("for loop ran in",time.time()-initial2,"seconds")



# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)