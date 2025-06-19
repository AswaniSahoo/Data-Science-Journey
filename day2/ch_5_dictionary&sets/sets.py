s={1,5,78,34}
#s={} will creat a empty dictionary
e =set() # it is an empty set

s = {1, 2, 3}
s.add(4) #add single element to the set
print(s)  # {1, 2, 3, 4}

s = {1, 2, 3}
s.remove(2) #Raises KeyError if the element is not found.
print(s)  # {1, 3}

s = {1, 2, 3}
s.discard(2)# Does not raise error
print(s)  # {1, 3}

s = {1, 2, 3}
element = s.pop() # Raises KeyError if the set is empty.
print(element)  # Arbitrary element, e.g., 1

s = {1, 2, 3}
s.clear()
print(s)  # set()

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)  # {1, 2, 3, 4, 5}

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.intersection(s2)
print(s3)  # {3}

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.difference(s2)
print(s3)  # {1, 2}

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.symmetric_difference(s2)
print(s3)  # {1, 2, 4, 5}

s1 = {1, 2}
s2 = {1, 2, 3}
print(s1.issubset(s2))  # True

s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2))  # True

s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))  # True

