# def func_name(a,b,c,d):
#     print(a,b,c,d)
# func_name("vishal","arman","vaibhav","nehal")    

def func(normal,*args,**kwargs):  # we can use anything instead of args like name or anything ,.....its not mendatory to use args as a argument
    # print(args[0])
    print(normal)
    for items in args:
        print(items)
    print("\n now i would show you the content of the kwargs")   
    for key,value in kwargs.items():
        print(f"{key} is a {value}")



normal="i am a normal argument taken in this programme"
kw={"vishal":"programmer","arman":"blogger","raghav":"chutku"}
x=["vishal","shariq","gularfeen","aabad"] # wheatther its a list or tuple it gets stored as a tuple
func(normal,*x,**kw)

# we can not take argumens as func(*args,normal).. this is wrong way and it will through an error
# the correct way is func(normal,*args,**kwargs)...this is the convention
# args and kwargs are optional ...