# PROJECT: CONTACT MANAGEMENT SYSTEM
# PS NO: 95

contacts = []


def validate_phone(phone):

    if len(phone) != 10 or not phone.isdigit():
        return False

    return True


def is_duplicate(phone, exclude_name=None):

    for contact in contacts:

        if contact["phone"] == phone:

            if exclude_name is not None and contact["name"].lower() == exclude_name.lower():
                continue

            return True

    return False



def add_contact():

    print("\n--- ADD CONTACT ---")

    name = input("Enter name: ").strip()

    phone = input("Enter phone number: ").strip()

    email = input("Enter email (optional): ").strip()

    
    if not validate_phone(phone):

        print("Invalid phone number. Enter exactly 10 digits.")

        return

    
    if is_duplicate(phone):

        print("Contact with this number already exists.")

        return

    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    
    contacts.append(new_contact)

    print(f"Contact added: {name} | {phone}")



def view_contacts():

    print("\n--- ALL CONTACTS ---")  

    if len(contacts) == 0:

        print("No contacts found.")

        return

    for contact in contacts:

        print(
            f'{contact["name"]} | '
            f'{contact["phone"]} | '
            f'{contact["email"]}'
        )



def search_contact():

    print("\n--- SEARCH CONTACT ---")

    search_name = input("Enter name to search: ").strip().lower()

    found = False

    for contact in contacts:

        if search_name in contact["name"].lower():

            print(
                f'{contact["name"]} | '
                f'{contact["phone"]} | '
                f'{contact["email"]}'
            )

            found = True

    if not found:

        print("Contact not found.")



def update_contact():

    print("\n--- UPDATE CONTACT ---")

    name = input("Enter contact name to update: ").strip()

    found_contact = None

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            found_contact = contact

            break

    if found_contact is None:

        print("Contact not found.")

        return

    new_phone = input("Enter new phone number: ").strip()

    
    if not validate_phone(new_phone):

        print("Invalid phone number. Enter exactly 10 digits.")

        return

    
    if is_duplicate(new_phone, exclude_name=found_contact["name"]):

        print("Contact with this number already exists.")

        return

    
    found_contact["phone"] = new_phone

    print(f"Phone updated: {new_phone}")



def delete_contact():

    print("\n--- DELETE CONTACT ---")

    name = input("Enter contact name to delete: ").strip()

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            contacts.remove(contact)

            print(f"Contact '{contact['name']}' deleted.")

            print(f"Total contacts: {len(contacts)}")

            return

    print("Contact not found.")


def main():

    while True:

        print("\n================================")
        print("   CONTACT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            add_contact()

        elif choice == "2":

            view_contacts()

        elif choice == "3":

            search_contact()

        elif choice == "4":

            update_contact()

        elif choice == "5":

            delete_contact()

        elif choice == "6":

            print("Thank you for using Contact Management System!")

            break

        else:

            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":

    main()
