# Function to add a contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    contacts.append(contact)
    print("Contact added successfully!")

# Function to display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts:")
    for contact in contacts:
        print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")

# Main function to run the program
def main():
    contacts = []
    while True:
        print("\n1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
