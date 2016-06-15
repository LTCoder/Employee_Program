mistake = "N"
command = input("Add employee to system? (Y/N) ").upper()
using = False
while command not in ['Y', 'N']:
	print("Invalid input, please try again")
	command = input("Add employee to system? (Y/N) ").upper()
if command == "Y":
	file = open("workers.txt", "w")
	using = True
while command != "N":
	first_Name = input("Enter the worker's first name: ").upper()
	if first_Name.isalpha() != True:
		while first_Name.isalpha() != True:
			print("Only letters can be in a name, try again.")
			first_Name = input("Enter the worker's first name: ").upper()
	last_Name = input("Enter the worker's last name: ").upper()
	if last_Name.isalpha() != True:
		while last_Name.isalpha() != True:
			print("Only letters can be in a last name, try again.")
			last_Name = input("Enter the worker's last name: ").upper()
	salary = input("Enter the worker's salary: ")
	if salary.isdigit() != True:
		while salary.isdigit() != True:
			print("Only digits can be in a salary, try again.")
			salary = input("Enter the worker's salary: ")
	job_title = input("Enter the worker's job title: ").upper()
	if job_title.isalpha() != True:
		while job_title.isalpha() != True:
			print("Only letters can be in a job title, try again.")
			job_title = input("Enter the worker's job_title: ").upper()
	print("Details of worker addded: " + "\n" + "First name: " + first_Name + "\n" + "Last name: " + last_Name + "\n" + "Salary: " + salary + "\n" + "Job Title: " + job_title)
	mistake = input("Is the above information correct? (Y/N) ").upper()
	if mistake.isalpha() != True:
		while mistake.isalpha() != True:
			print("Invalid input, please try again.")
			mistake = input("Is the above information correct? (Y/N) ").upper()
	if mistake == "N":
		command = input("Restart? (Y/N) ").upper()
	else:
		file.write(first_Name + " ")
		file.write(last_Name)
		file.write(", ")
		file.write(salary)
		file.write(", ")
		file.write(job_title)
		file.write("\n")
		command = input("Add another employee to system? (Y/N) ").upper()
if using == True:
	file.close()