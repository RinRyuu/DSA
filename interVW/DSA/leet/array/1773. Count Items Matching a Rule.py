items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey = "color"
ruleValue = "silver"
keys = {'type': 0, 'color': 1, 'name': 2}
c = 0
index = keys[ruleKey]
for i in items:
    if i[index] == ruleValue:
        c += 1
print(c)  