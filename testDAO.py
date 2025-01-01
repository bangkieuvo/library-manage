from function import*
from service import*
s = CategoryService()
o = s.find(1)
o.haha = "kkk"
print(type(o))
print(vars(o))

