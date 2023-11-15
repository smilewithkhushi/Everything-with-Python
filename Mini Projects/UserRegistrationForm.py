def email_validation(email):
  # Checking if the email is valid or not
  if "@gmail.com" not in email:
    print("Invalid Email Address")


def phoneVerify(phone):
  if len(phone) != 10:
    print("Invalid Phone Number")


def info():
  # Creating a regestration form to apply for a job
  print("\n *******************************\n")
  print("\t <<< REGISTRATION FORM >>> ")
  print("<<< Enter your details here:")

  # The format for entering the details:-
  print("-->> Enter your valid full name")
  print(
      "-->> Age should be in numerical characters and only 20 and above are eligible for this job"
  )
  print("-->> Date of Birth should be in the following format")
  print("-->> Format of DOB: DD/MM/YYYY ")


response = "y"
while (response == "y"):
  info()

  # Taking the details from the user as an input.
  fname = input("Enter your first name:")
  lname = input("Enter your last name:")
  age = int(input("Enter your age:"))

  email = input("Enter your email id: ")
  email_validation(email)

  phone = input("enter your phone number: ")
  phoneVerify(phone)

  sub = input("Enter your subjects (use comma separated values): ")
  subjects = sub.split(",")

  fullname = fname + "_" + lname
  fileName = f"{fullname}_details.txt"
  #create a file to store the details

  with open(fileName, "w") as file:
    file.write("** REGISTRATION DATA **\n")
    file.write(f"Name: {fullname}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Phone number: {phone}\n")
    print("\n \n----> Your data has been collected\n")

  response = input("-> Do you want to continue? y/n : ")

print("\n\n ** THANK YOU FOR YOUR RESPONSE **")
