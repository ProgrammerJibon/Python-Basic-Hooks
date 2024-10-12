datas = [30,70,17,10,15,100]

# insert uses to insert data in any index
datas.insert(0, 7)

# sort makes the array  sorted
datas.sort()

# append add a data to the end
datas.append(10)

# extend combines to arrays to a single array
datas.extend([11,3,10,4,20])
# or we can also extend like this
datas = datas + [0,1,2,3]
datas = [5,6,8,9] + datas
datas = [21,26,28,29] + datas + [30,31,32,33]

# pop removes the last element
datas.pop(10)

# remove func do search and remove the first finded element
datas.remove(10)

# index do the search and return the index of an element
# print(datas.index(10))

# count function return the total number of a element
# print(datas.count(10))

# __len__ returns the size of array
print(datas.__len__())
print(len(datas))


print(datas)