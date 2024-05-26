# Module 3: Mini-Project | Contact Management System



import re


# def import_contacts():
#     my_contacts = {}
#     with open("/Users/pheonaohakwe/Coding_temple/Backend/week2/weekend/contact_manager.txt", "r") as file:
#         for line in file:
#             name, phone, email = line.strip().split(":")
#             my_contacts[name] = {f"{phone}{email}"}
#     print(my_contacts)
   



def export_contacts(contacts):
    my_contacts = contacts
    with open("/Users/pheonaohakwe/Coding_temple/Backend/week2/weekend/contact_manager.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}:\n")
            for contacts, email in phone.items():
                file.write(f"       {contacts}: {email}\n")


try:
    with open("/Users/pheonaohakwe/Coding_temple/Backend/week2/weekend/contact_manager.txt", "r") as file:
        for line in file:
            print(line.strip())
except Exception as e:
    print(f"An error occurred: {e}")

def add_contacts(contacts): 
    name = input("What is the first and last name of the contact you would like to add?: ").title()
    email = input("What is the email address of the contact you would like to add?: ")
    matched_email = re.match(r"\b[A-Za-z0-9À-ÿ._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", email)
    print(matched_email)
    if matched_email:
         print("Valid email")
    phone = input("What is the phone number of the contact you would like to add?: ")
    verified_phone = re.match(r"\d{3}\d{3}\d{4}", phone)
    if verified_phone:
         print("Valid phone number")
    else:
       print("Invalid phone number")

    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact added successfully: \n{contacts} ")
    
def view_contacts(contacts):
     print("This is a list of all your contacts:")
     for name, phone in contacts.items():
         print(contacts)
        


def search_contacts(contacts):
    searched_name=input("Please enter the contact first name and last name you're searching for: ")
    for name in contacts:
        if searched_name.lower() == name.lower():
            print(f"This is the contact you're searching for: \n{contacts[name]}")
        else: 
             print("The contact you're searching for does not exist.")
    
    

def delete_contacts(contacts):
    name = input("Please input the contact first and last name you're searching for: ").title()
    if name in contacts:
        del contacts[name]
        print(f"That contact has been deleted this is an updated list of contacts: {contacts}")
    
    else:
        print("The name does not match any of the contacts.")
      


def update_contacts(contacts):
    name = input(f"This is a list of your contacts: {contacts}. Input the name of the contact you want to update?").title()
    if name in contacts:
        update = input(" What would you like to update  name, email, phone: ").lower()
        if update == "name":
            updated_name = input("Please input the new first and last name you would like to update current contact with:").title()
            if name in contacts:
                contacts[updated_name] = contacts[name]
                del contacts[name]
                print(f"The name has been updated. Here is an updated list of contacts: \n{contacts}")
            else:
                print("The name you entered does not match any of the contacts.")
        elif update == "email":
            email = input("Please enter the name of contact for the email you would like to update.")
            updated_email = input("Please enter the new email of the contact: ")
            if email in contacts:
                contacts[name]["email"] = updated_email
                print(f"The email has been updated. Here is your updated list of contacts: \n(contacts)")
        elif update == "phone":
            phone = input("Please enter the name of contact of the phone you would like to update.")
            updated_phone = input("Please enter the new phone of the contact: ")
            if phone in contacts:
                contacts[name]["phone"] = updated_phone
                print(f"The phone has been updated. Here is your updated list of contacts: \n(contacts)")
        else:
             print("That name is not the Contact Manager contacts")           
        
   


def contact_manager():
   contacts = {}
   print("Welcome to the Contact Management System!")

   while True:
        response = input("""Please select an option from the menu below. Enter a valid response of add, update, delete, view, search,  export, or quit...: 
                            
        
            Menu:
                1. add.    
                2. delete.  
                3. update.
                4. view.    
                5. search.  
                6. export.
                7. quit.    
        """)
        if response == "add":
                add_contacts(contacts)

        elif response == "delete":
                    delete_contacts(contacts)

        elif response == "view":
                    view_contacts(contacts)

        elif response == "search":
                    search_contacts(contacts)

        elif response == "export":
                    export_contacts(contacts)

        elif response == "update":
                    update_contacts(contacts)

        elif response == "quit":
                    print("Leaving Contact Manager")
                    break
        else:
                    print("Please enter a valid response!")

contact_manager()





\