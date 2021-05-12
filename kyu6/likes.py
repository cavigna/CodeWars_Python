def likes(names):

    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return str(names[0]) + " likes this"
    elif len(names) == 2:
        return f'{str(names[0])} and {str(names[1])} like this'
        str(names[0]) + " and "+str(names[1]) + " like this"
    elif len(names) == 3:
        return f'{str(names[0])}, {str(names[1])} and {str(names[2])} like this'

    return f'{str(names[0])}, {str(names[1])} and {str(len(names)-2)} others like this'


print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
