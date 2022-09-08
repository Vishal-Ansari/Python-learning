import requests
r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(r.text)
print(r.status_code)

url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data={
    "p1":4,
    "p2":8
}

r2=requests.post(url=url,data=data)