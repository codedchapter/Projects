import csv

def load_contacts():
    contacts = []
    try:
        with open("contacts.csv", "r") as file: # open contacts.csv 
            # now reader will read the csv file 
            reader = csv.reader(file)
            for row in reader:
                contacts.append({"name": row[0], "phone": row[1]})
            # erroe handling in file not 
    except FileNotFoundError:
         pass
    return contacts

def save_contact(name, phone):
    with open("contacts.csv" ,"a") as file:
          writer = csv.writer(file)
          writer.writerow([name, phone])

def show_all(contacts):
    for contact in contacts:
        print(f"{contact['name']} - {contact['phone']}")
def search_contact(contacts, name):
    # your code here
    for contact in contacts:
      if contact["name"] == name:
         print(contact["phone"])
# Main program
contacts = load_contacts()

while True:
    print("\n1. Show all")
    print("2. Add contact")
    print("3. Search")
    print("4. Quit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        show_all(contacts)
    elif choice == "2":
        name = input("Name: ")
        phone = input("Phone: ")
        save_contact(name , phone)
        contacts.append({"name": name , "phone":phone})
        # your code here
    elif choice == "3":
        name = input("Search: ")
        search_contact(contacts , name)
        # your code here
    elif choice == "4":
        break