#
# #-----dir()------------
# x = [1,2,3]
# show = dir(x)
# print(show)
#
# #-----help()--------
#
# help(type)
#--Essential python Built_n function---
#-----help()
#-----dir()
#-----enumerate()
#-----isinstance() = type()
#-----open()
#-----isinstance()
#-----round()
#-----sorted()
#-----sum()



material = ['concrete', 'steel', 'glass','copper']
strengths = [25, 50, 15]

zipped = zip(material, strengths)
zip_list = list(zipped)
print(zip_list)
# count = 0
# for mat in material:
#     count += 1
#     print(count, mat)

for n, mat in enumerate(material,1):
    print(n, mat)
x = 42
y = 'hello'
z = [1,2,3]

if isinstance(x, int): # type(x) = int:
    print(x**2)

print(list(range(1,11)))
x = 0.2556749
print(round(x, 2))
#------regular ---
#---all()
#---abs()


# --------LIST METHOD-------

my_list = [1,2]
my_list.append(3)
print(my_list)

list_1 = [1, 2, 3]
list_2 = [4, 5, 7]

list_3 = list_1 + list_2
print(list_3)
list_1.extend(list_2)
print(list_1)
list_1.append(list_2)
print(list_1)
list_1.remove(list_2)
print(list_1)
print(list_1.index(7))

list_n = [1,2,3,4,2,3,1,6,8,10,2]
ind = list_n.index(2,2)
print(ind)

list_n.insert(0, 'zero')
print(list_n)
print(list_n.count(2))

#----Dict Method-----------

a = 45
a = float(a)
print(format(a, '.3f'))

print(round(56.002987,3))