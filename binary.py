
def to16BitBin(num):
    value = bin(num).split('b')[1]
    zeros = (16-len(value))*'0'
    return zeros+value

print(int(to16BitBin(1035), 2))

details = {'name': 'lee',
            'age': 25,
            'interests': ['sex', 'football', 'girls', {'car': 'ferrari'}]}


print(type(details))


array = {3:'hi', 4:'my', 5:'name', 6:'is', 8:'lee'}
print(array[8])