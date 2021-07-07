#Elijah Jedkins PSID: 1786452
parts = input().split()
name = parts[0]
while name != '-1':
    #Inserting try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
    except ValueError:
     age = 0

    print('{} {}'.format(name, age))
    parts = input().split()
    name = parts[0]
