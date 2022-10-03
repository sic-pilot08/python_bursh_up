banned_users = ['Andrew', 'Carolina', 'David']
user = input("Enter user name: ")
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish!")
else:
    print("You're banned from the activity in this group!")
