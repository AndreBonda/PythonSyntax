import json


obj = [1, "hello", "world"]
a = json.dumps(obj)
print(a) # [1, "hello", "world"]
print(a[0:2]) # [1