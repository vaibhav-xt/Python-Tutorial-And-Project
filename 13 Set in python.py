s = set()
print(type(s))

setlist = set([1, 2, 3, 4])
print(setlist)
print(type(setlist))
s.add(1)    # here you can see that we have added two times 1 but when we print  once
s.add(1)    # it written only because it property of set that is write ony unique words.
s.add(3)
s1 = s.union({5, 6, 7, 8})
s2 = s.intersection([1, 2, 6, 7, 8])
s3 = s.isdisjoint([5, 6, 7])
print(s1)
print(s2)
print(s3)

# here you can use all the functions like remove(), pop(), pop() like that all functions
