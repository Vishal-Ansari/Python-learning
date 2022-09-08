# question 5
# vishal ansari
def sort_by_value(d,reverse=False):
    return dict (sorted(d.items(),key = lambda x:x[1],reverse = reverse))
print("Original Dictionary elements:")
my_dict2 = {'Honesty':7, 'is':2, 'the':3, 'best':4, 'policy':6}
print(my_dict2)
print("\nSort (descending) the elemenmts by their length:")

print(sort_by_value(my_dict2, True))
print("vishal ansari secction N 200111238")