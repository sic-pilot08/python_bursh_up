# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(f"My first bicycle was a {bicycles[0].title()}")
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(2, 'ducati')
motorcycles.sort(reverse=True)
print(motorcycles)
# del motorcycles[1]
# print(motorcycles)