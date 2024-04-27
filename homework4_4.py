contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts saved.")

def main():
    print("Welcome! I'm your console assistant.")

    while True:
        user_input = input("Enter command (type 'exit' to quit): ").lower()

        if user_input == "exit" or user_input == "close":
            print("Goodbye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        else:
            parts = user_input.split()
            command = parts[0]
            args = parts[1:] if len(parts) > 1 else []

            if command == "add" and len(args) == 2:
                add_contact(*args)
            elif command == "change" and len(args) == 2:
                change_contact(*args)
            elif command == "phone" and len(args) == 1:
                show_phone(*args)
            elif command == "all" and len(args) == 0:
                show_all()
            else:
                print("Invalid command.")

if __name__ == "__main__":
    main()