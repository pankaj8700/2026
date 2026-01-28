def add_contact(name, contact_no = None, alternate_no = None, email_id= None):
    temp_dir = []
    if name.strip() == "":
        sys.exit("Not allow")
    else:
        temp_dir.append(name)
        temp_dir.append(contact_no)
        temp_dir.append(alternate_no)
        temp_dir.append(email_id)
        directory.append(temp_dir)
        return temp_dir

def search_by_name(name):
    for i in directory:
        if i[0] == name:
            print(i)
        else:
            print("name not found")
            
def search_by_no(no):
    for i in directory:
        if i[1] == no:
            print(i)
        else:
            print("no. not found")
def clear_dir():
    directory.clear()
    print(directory)

def delete_name_or_no(value): 
    for contact in directory: 
        if contact[0] == value or contact[1] == value: 
            directory.remove(contact) 
            print("Deleted:", contact) 
            return 
    print("Value not found")

def count_():
    print(len(directory))

def initialize_directory():
    
    while True:
        print("1. for adding new contact:")
        print("2. for search by name:")
        print("3. for search by no.")
        print("4. for clear directory:")
        print("5. for delete either by name or no.")
        output = int(input("please enter what you want to do:"))
        if output == 1:
            name = input("please input name:")
            no = input("please enter no.:")
            alternate_no = input("please enter alternate_no.")
            email_id = input("please enter email_id:")
            add_contact(name, no, alternate_no, email_id)
        elif output == 2:
            name = input("please enter your name:")
            search_by_name(name)
        elif output == 3:
            no = input("please enter no.")
            search_by_no(no)
        elif output == 4:
            clear_dir()
        elif output == 5:
            value = input("enter:")
            delete_name_or_no(value)
        else:
            print("invalid choice")
directory = []
initialize_directory()