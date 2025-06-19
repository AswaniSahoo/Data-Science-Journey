marks = {
    "harry":100,
    "aswin": 85,
    "key": "value",
    "list": [23,56 ,89] 
}
# print(marks.items())
# print(marks.keys())
# marks.update({"aswin":89,"subham":96})
print(marks.get("aswin"))#both gives same value 
print(marks["aswin"])
print(marks.get("subham"))#gives none
print(marks["subham"])#gives error
