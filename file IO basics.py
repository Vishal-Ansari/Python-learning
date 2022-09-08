# FILE IO Basics
"""
"r"--- open file for reading-- default
"w"--- open file for writing
"x"---creates file if not exist
"a"---add more content to the file
"t"--- text mode-- default
"b"---binary mode
"+"--- read and write
"""

f=open("m.txt")
# f=open("m.txt","rt")
# or:- f=open("m.txt","r")
# content=f.read(3676)
# print("1",content)
# print("2",content)

# for line in f:
#     print(line, end="")

# content=f.read()
# print(content)

# we can also use readline function 
print(f.readline())
f.close()