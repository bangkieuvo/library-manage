from DAO import UserDAO
from model import User
import hashlib
u = User(888,"hha","hehe",hash(1234))
print(hashlib.sha256(("1234").encode("utf-8")))