i = 4

if (i % 4 == 0 or i < 12) and not i == 4:
    print('the value of i is less than expected - line 4')
elif i == 12:
    print('the value of i is equal to expected value - line 6')
else:
    print('the value of i more than expected - line 8')
print('the end\n\n')

# age = int(input("Please enter your age: "))
# name = input("What's your name? ")
# greeting = f"Hello {name}!" if age <= 18 else f"How do you do, Mr. {name}!"
# print(greeting)


name_list = ['James', "Stacy", 'Bob', "Jessica"]
name_list.append('R2D2')
name_list.insert(2, 'Chewbacca')
name_list.remove('Bob')


my_tup = tuple(name_list[::])


for a_name in name_list:
    if a_name[0].upper() == 'J':
        print(f'the length of the name {a_name} is {len(a_name)} letters')


sum = 0
for i in range(33, 0, -3):
# for i in range(99):
    print(f'the value of i is {i}')
    sum += i
print(f'the final value of sum is {sum}')