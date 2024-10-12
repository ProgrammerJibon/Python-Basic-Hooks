datas = {
    "name": "Jibon",
    "age":  23,
    "id":   59
}


print(datas)

# here, key returns the keys of datas like foreach ($datas as $key=>$values)
for key in datas.keys():
    print(key, "\t=>\t", datas[key])
    
# here, key returns the values of datas
for key in datas.values():
    print(key)
    
# here, key returns the whole item of datas as a tupple
for key in datas.items():
    print(key[0], "\t=>\t", key[1])
    
# here, key, values returns the keys of datas like foreach ($datas as $key=>$values)
for key, value in datas.items():
    print(key, "\t=>\t", value)