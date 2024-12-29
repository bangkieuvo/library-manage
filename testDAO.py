from function import*

u = login("alice01","123456")
print(borrowBook(u.id,10))
#returnBook(u.id,6)
print("==")
for b in getBorrowingList(u.id):
	print(vars(b))