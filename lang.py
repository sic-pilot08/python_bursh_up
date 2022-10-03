# fav_lan = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# friends = ['phil', 'sarah']
# for name, lang in fav_lan.items():
#     print(f"Hi {name.title()}")
#
#     if name in friends:
#         print(f"\t{name.title()}, I see you love {lang.title()}!")
#
#
favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
print(favorite_languages['edward'][1])