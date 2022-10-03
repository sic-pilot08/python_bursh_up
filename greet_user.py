def greet_user(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


user_names = ['hannah', 'ty', 'margot']
greet_user(user_names)