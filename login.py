import re
from getpass import getpass

# Email format
match = re.compile(r"[A-Za-z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")

spcl_char =['$', '@', '#', '%'] # special char to use in password

def login():
	email_id = input("Enter your Mail ID : ")
	if email_id[0].isdigit() or not re.fullmatch(match, email_id):
		print("Enter valid Email ID")
	else:
		with open("login.txt", 'r') as db:
			for line in db:
				if email_id in line:
					_password = getpass("Enter your Password : ")
					if email_id+":"+_password in line:
						print("\nWELCOME TO DASHBOARD\n"
							f"\nSuccessfully logged in as {email_id}")
						return
					else:
						print("Invalid Credentials.")
			print("Mail ID not found in database. Please register.\n")
			register()


def forgot_password():
	email_id = input("Enter your registered Mail ID : ")
	if email_id[0].isdigit() or not re.fullmatch(match, email_id):
		print("Enter valid Email ID")
	else:
		with open("login.txt", 'r') as db:
			all_lines = db.readlines()
			db.close()
			for no, line in enumerate(all_lines):
				if email_id in line:
					new_pass = getpass("Enter your New Password : ")
					if len(new_pass) > 5 and len(new_pass) <16 and any(char.isdigit() for char in new_pass) and any(char.isupper() for char in new_pass) and any(char in spcl_char for char in new_pass):
						new_pass_conf = getpass("Enter confirm password : ")
						if new_pass == new_pass_conf:
							all_lines[no] = email_id+":"+new_pass+'\n'
							return all_lines
						else:
							print("Password does not match.")
					else:
						print("Please Enter the valid password\n"
					"Hints:\n"
					"\t1. Password should between 5 - 16 characters\n"
					"\t2. Password should have atleast one special character\n"
					"\t3. Password should have atleast one numerical character\n"
					"\t4. Password should have atleast one upper case character")
			print("Mail ID is not registered.")

def register():
	mail = input("\nEnter your Mail ID : ")
	if mail[0].isdigit():
		print("Invalid Mail Format\n"
			"Hint : Mail ID should not start with number")
	else:
		if re.fullmatch(match, mail):
			_reg_pass = getpass("Enter Password : ")
			if len(_reg_pass) > 5 and len(_reg_pass) <16 and any(char.isdigit() for char in _reg_pass) and any(char.isupper() for char in _reg_pass) and any(char in spcl_char for char in _reg_pass):
				_reg_pass_conf = getpass("Enter confirm password : ")
				if _reg_pass == _reg_pass_conf:
					with open('login.txt', 'a') as db:
						db.write(mail+":"+_reg_pass+'\n')
					print("User has been successfully registered.\n")
				else:
					print("Password does not match.")
			else:
				print("Please Enter the valid password\n"
					"Hints:\n"
					"\t1. Password should between 5 - 16 characters\n"
					"\t2. Password should have atleast one special character\n"
					"\t3. Password should have atleast one numerical character\n"
					"\t4. Password should have atleast one upper case character")
		else:
			print("Invalid Mail Format\n"
			"Hint : Please recheck the mail ID format")


print("WELCOME TO HOME PAGE\n\n"
	"1. Login\n"
	"2. Register\n"
	"3. Forgot Password\n")

user_choice = input("Enter your choice : ")

choices = ["1", "2", "3"]

attempt = 0
while user_choice not in choices and attempt < 3:
	user_choice = input("Enter your choice : ")
	attempt += 1

if user_choice not in choices:
	print("Oops! attempts exceeded please try again later.")
else:
	if user_choice == "1":
		login()
	elif user_choice == "2":
		register()
	else:
		datas = forgot_password()
		with open('login.txt', 'w') as rechange_db:
			for cred in datas:
				rechange_db.write(cred)
		print("Your Password has been updated.\n")
