# A script to count string in a list:
line = input('Enter the content of your list, separated by commas: ')
my_list = [i.strip() for i in line.split(',')]
counter = 0
for i in my_list:
    try:
        float(i)
        counter += 1
    except:
        pass
print(f'There are {len(my_list)- counter} str in your list')