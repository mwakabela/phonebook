class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        """
        Adds a new contact to the phonebook
        """
        name = input("Enter the name of the contact: ").lower()
        number = input("Enter the phone number of the contact: ")
        self.contacts[name] = number
        print(f"Contact {name} added with number {number} \n")

    def update_contact(self):
        """
        Updates a contact's number
        """
        name = input("Enter the name of the contact you want to update: ").lower()
        if name in self.contacts:
            number = input("Enter the new phone number of the contact: ")
            self.contacts[name] = number
            print(f"Contact {name} updated with number {number} \n")
        else:
            print(f"Contact {name} not found. \n")

    def delete_contact(self):
        """
        Deletes a contact from the phonebook
        """
        name = input("Enter the name of the contact you want to delete: ").lower()
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted. \n")
        else:
            print(f"Contact {name} not found. \n")

    def search_contact(self):
        """
        Search a contact by name and return the number
        """
        name = input("Enter the name of the contact you want to search: ").lower()
        if name in self.contacts:
            return self.contacts[name]
        else:
            return f"Contact {name} not found. 'n"

    def view_contacts(self):
        """
        Returns all the contacts in the phonebook
        """
        if self.contacts:
            return self.contacts
        else:
            return "No contacts found. \n"


phonebook = Phonebook()

while True:
    print("Welcome to your personal phonebook! \n")
    print("1. View all contacts")
    print("2. Add a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Search a contact")
    print("6. Exit")

    user_input = input("Enter your choice: ").lower()
    if user_input == "1":
        print(phonebook.view_contacts())
    elif user_input == "2":
        phonebook.add_contact()
    elif user_input == "3":
        phonebook.update_contact()
    elif user_input == "4":
        phonebook.delete_contact()
    elif user_input == "5":
        print(phonebook.search_contact())
    elif user_input == "6":
        break
    else:
        print("Invalid input. Please enter a valid choice.")
