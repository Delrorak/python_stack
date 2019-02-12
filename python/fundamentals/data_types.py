x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])

empty_list = ['tom']
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

empty_list[0]='dachshund'
print(empty_list[0])
print(type(empty_list[0]))
print(len(empty_list[0]))
total = 10
total = total + x + len(empty_list[0])
print(total)
total =10 + int(len(empty_list[0]))
print(total)

