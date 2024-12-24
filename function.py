from service import*
import tool
def login(userName,password):
	service = UserService()
	u = service.findByUserName(userName)
	if u == None:
		return None
	if u.hashedPassword == tool.encrypt(password):
		return u

u = login("vbk1212","123456")
if u != None:
	print(vars(u))
else:
	print("login Fail!")