roles = {
    "admin": {"add", "delete", "update"},
    "editor": {"update", "view"},
    "viewer": {"view"}
}

users={}

while True:
    print("press 1 for add user")
    print("press 2 for remove user")
    print("press 3 for update user role")
    print("press 4 for check premisssion")
    print("press 5 for show users")
    print("press 6 for exit")

    user_choice = int(input("enter user choice: "))

    if user_choice == 1:
        user_name = input("enter your name: ")
        user_role = input("enter role (admin/editor/viewer): ")

        if user_role in roles:
            users[user_name] = user_role
            print("user added successfully")
        else:
            print("role not found")    
    elif user_choice == 2:
        remove_person = input("enter name to remove: ")
        if remove_person in users :
            del users[remove_person]
            print("user removed successfully")
        else:
            print("no user found")
    elif user_choice == 3:
        username = input("enter username: ")
        if username in users:
            new_role = input("enter new role: ")
            if new_role in roles:
                users[username] = new_role
                print("user role updated successfully")
            else:
                
                print("invalid role")
        else:
            print("user not found")            
    elif user_choice == 4:
        username = input("enter username: ")
        user_action = input("enter user action(add/delete/update/view): ")

        role = users[username]

        if user_action in roles[role]:
            print("yes you are allowed")
        else:
            print("no you are not allowed")    
    elif user_choice == 5:
        print("-----list of all users-----")
        if len(users)>0:
            for idx, item in users.items():
                print(idx, "->", item)
    elif user_choice == 6:
        print("You are exit")
        break
    else:
        print("please enter valid option")