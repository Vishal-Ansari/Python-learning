import pickle

# cars=["BMW","AuDI","Maruti suzuki","Ferrari"]
# file="mycars.pkl"
# myfile=open(file,"wb")
# pickle.dump(cars,myfile)
# myfile.close()

file="mycars.pkl"
myfile=open(file,"rb")
mycars=pickle.load(myfile)
print(mycars)