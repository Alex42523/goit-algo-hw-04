
#Вправа 1
def total_salary(path):
    total_salary = 0
    count = 0
    try:
        with open(path, 'r') as file:
            for line in file:
                try:
                    _,salary = line.strip().split(",")
                    total_salary += int(salary)
                    count += 1
                except ValueError:
                    continue
    except FileNotFoundError:
        return "Файл не знайдено"
    if count == 0:
        return (0, 0)
    average_salary = total_salary / count
    return total_salary, average_salary
print(total_salary("/home/alex/Documents/salary.txt"))


#Вправа 2
def get_cats_info(path):
    info = []
    try:
        with open(path, 'r') as file:
            for line in file:
                try:
                    identifier, name, age = line.strip().split(",")
                    full_info = ({"id": identifier, "name": name, "age": age})
                    info.append(full_info)
                except ValueError:
                    continue
    except FileNotFoundError:
        return "Файл не знайдено"
    return info
print(get_cats_info("/home/alex/Documents/cats_file.txt"))

#Вправа 4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
def show_all(args, contacts):
    return contacts
def change_contact (args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!\n My commands: \nHello \nAdd [name] [phone number] \nExit \nChange [name] [new phone] \nAll \nphone [name]")
    while True:
        user_input = input("Enter a command: \n")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
