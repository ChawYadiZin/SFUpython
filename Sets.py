#Sets

Sets.py
 

includes a data type for sets.
Curly braces or the set() function can be used to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # show that duplicates have been removed

'orange' in basket        # fast member testing
'crabgrass' in basket

Demonstrate set opreations on uniqe letters from
a = set('abracadabra')
b = set('alacazm')
a 						# unique letters in a
a - b 					# letters in a but not in b
a | b 					# letters in a or b or both
a & b 					# letters in both a and b
a ^ b 					# letters in a or b but not both


x = set('23802348')
y = set('57839012')
x - y
y - x
x ^ y
y | x
x & y
x

a = { x for x in 'abracadabra' if x not in 'abc'}
abracadabra

--------

friuts = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

friuts.add("cucumber")
friuts
friuts.update("grape")
friuts
friuts.remove("banana")
friuts
friuts.discard("banana")
friuts

Dictionaries

# Dictionaries

#Another usedul data type built into pyhton is the dictionary

tel = {'jack': 4098,'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel

---------

del tel ['sape']
tel['irv'] = 4127
tel

---------

del tel['sape']
tel [ir]





When lopping throgh Dictionaries

knights = {'gallahad': 'the pure','robin': 'the brave','sape' : 4355}
for k, v in knights.items():
	print(k, v)

for x, y in enumerate(['tic', 'tac', 'toe']):
	print(x, y)