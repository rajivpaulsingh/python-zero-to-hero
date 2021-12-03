
list1 = [1,2,3]

# append
list1.append(4)
print(list1)


# count
print(list1.count(10))
print(list1.count(2))


# extend
x = [1,2,3]
x.append([4,5])
print(x)

x = [1,2,3]
x.extend([4,5])
print(x)


# index
list1.index(2)


# insert
list1.insert(2, 'inserted')
print(list1)


# pop
ele = list1.pop()
print(list1)
print(ele)


# remove
list1.remove('inserted')
print(list1)


# reverse
list2 = [1,2,3,4,5]
list2.reverse()
print(list2)


# sort
list2.sort()
print(list2)

