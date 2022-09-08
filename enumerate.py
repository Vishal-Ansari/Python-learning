list=["bhindi","kheer","rasmalai", "aloo", "apple","guava"]
# i=1
# for item in list:
#     if i%2 is not 0:
#         print(f"jarvis please buy {item}")
#     i=i+1

for index, item in enumerate(list):
    if index%2==0:
        print(f"jarvis please buy {item}")
