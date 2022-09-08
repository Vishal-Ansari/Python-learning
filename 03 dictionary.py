d1={}
#print(type(d1))
d2={"vishal":"burgur","shadmani":"macroni","rukyya":"pizza",
"ammi":"paan","bauji":{"bidi":"paan","election":"vote"},
"shariq":"college and ghumna","pesa":"barbaad"}
#d2["rukhsar"]="suleman" 
#d2["sonam"]="naeem"
# or use d2.update({"kheera":"pyaaz"})
#dd2["shabnam"]="fakru"
#d2["bakra"]="kabab"
#dprint(d2)
#d3=d2  it doesnot copy d2 to d3 it only point to d2......
#del d3["bakra"]
d3=d2.copy()
#del d3["bakra"]
print(d3.keys())
print(d3.items())
