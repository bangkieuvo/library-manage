from DAO import *
from model import *
from service import *
import tool

def printList(l):
	for object in l:
		print(tuple(vars(object).values()))

aD = AdministratorDAO()
uD = UserDAO()
cD = CategoryDAO()
bD = BookDAO()
bbD = BorrowedBookDAO()
b = bbD.find(1)
list = bbD.findBorrowingByUserId(1)
printList(list)





