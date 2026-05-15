# ----SOME ESSENTIAL BUILT IN METHOD-----
#--1-.count()
print('hello'.count('l')) #2
#--2-.endswith()
print('Hello pyRevit Hackers'.endswith('Hackers')) #True
#--3-.find()
print('Hello pyRevit Hackers'.find('R')) #14
#--4-.format()
text_1 = '{a},{b},{c}'.format(a = 'You can also',
                           b = 'specify argument',
                           c = 'when combining a lot of string')
print(text_1)
#--5-.index
print('hel'.index('l')) #2
#--6.islower() and .isupper()
print('lower'.islower()) #True
print('Lower'.islower()) #False
#--7.join()
items = ['A', 'B', 'C', 'D']
print(''.join(items))  #ABCD
print(','.join(items)) #A,B,C,D
print('-'.join(items)) #A-B-C-D
#--8.lower()
print('HELLO'.lower()) #hello
#--9.split()
print('I love python'.split()) # By default, it split by space
print('apple,banana,orange'.split(',')) #split by comma
#---REGULARS--
#1.capitalize()
print('This Is Capitalized'.capitalize())
#2.casefold() Google it.
#3.replace()
print('hello'.replace('l', 'L'))  # heLLo
#---------------------------LIST METHODS-------------
#1--index()--------
my_list = [1,2]
idx = my_list.index(2)
print(idx)
#2--insert()-------
ins_n = [1,2,3,4,5,6]
ins_n.insert(2,4)
print(ins_n)
#3--pop()-------
pop_n = [1,2,3,4,5,6,]
pop_n.pop(1)
print(pop_n)
#4--remove()-
remove_n = [1,2,3,4,5,6,2]
remove_n.remove(2)
print(remove_n)
#5--sort-----
sort_n = [6,2,3,4,5,1]
sort_n.sort(reverse = True)
print(sort_n)
#5--copy()-----
copied = [1,2,3]
new_copied = copied.copy()
copied.append(5)
print(new_copied)
#6--count()-------
count_n = [1,2,3,3,5,6]
print(count_n.count(6))
#7--reverse()--
rev = [1,2,3,4,5,6,7]
rev.reverse()
print(rev)
#8--clear()----
clear_n = [1,2,3,4,5,6]
clear_n.clear()
print(clear_n)
#------------------TUPLE METHODS-----------------
#1--count()----
my_tuple = (1,2,3,4,5,6,5)
how_m = my_tuple.count(5)
print(how_m)
#2--index()------
idx = (1,2,3)
print(idx.index(2))
#--------DICT METHODS------------------------
#1--get()----
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
value = my_dict.get('c') # or my_dict['c']
print(value)
#2--items()------
items = my_dict.items()
print((items))
#3--keys()-----
keys = my_dict.keys()
print(keys)
#4--value------
values = my_dict.values()
print(values)
#5--setdefault()--------
value_c = my_dict.setdefault('c', 5)
value_d = my_dict.setdefault('d', 'the item does not exist')
print(value_c)
print(value_d)
#6--update()------------
my_dict_2 = {
    'd': 4,
    'e': 5,
    'f': 6
}
my_dict.update(my_dict_2)
print(my_dict)
#7--you can also copy and clear
#8--fromkeys()------
keys = ['a', 'b', 'c']
new_dict = my_dict.fromkeys(keys, 0)
print(new_dict)
#9--pop()-------
value = my_dict.pop('c')
print(value)
print(my_dict)
#10--popitem()---
item  = my_dict.popitem()
print(item)