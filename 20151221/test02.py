'''
测试for循环套if循环！
有三次机会输入密码，输入正确打印Yoo!;三次输错打印too many tries!
'''
locklist = []

user_name = input("Username:").strip()
with open("lock.txt", 'rt') as f1:
	for i in f1.readlines():
		i = i.strip()
		lock_list.append(i)
if user_name in lock_list:
	print("Sorry!%s were locked!"% user_name)
	isLocked = True
while not isLocked:
	loginSuccess = False
	print("start!")
	for i in range(3):
		pass_wd = input("passwd:").strip()
		with open('account.txt', 'rt') as f2:
			account_list = f2.readlines()
			if 
		if int(pass_wd) == n:
			print("Yoo!")
			loginSuccess = True
			break
	if loginSuccess is not True:
		print("too many tries!")
		with open('lock.txt', 'at') as f:
			f.write('%s\n'% user_name)