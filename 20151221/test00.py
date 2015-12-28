lock_file = "lock.txt"
account_file = "account.txt"


with open(account_file) as f:
	account_list = f.readlines()
for i in account_list:
	h = i.split()
	print(h[0])
	print(h[1])
	print("===================")

