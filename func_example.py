# def update(x):
#     print(id(x))
#     x=8
#     print("x ",x)

# a=10
# print(id(a))
# update(a)
# print("a ",a)

def updateLst(newLst):
    print(id(newLst))
    newLst[1]=24
    print("In fun ",newLst)

lst=[10,24,30]
print(id(lst))
updateLst(lst)
print("LST ",lst)