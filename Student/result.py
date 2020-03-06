

import student
import mary

x = student.a["code"]
y = student.a["code"]
z = student.a["student"] 
print(x ,' ',y,' ',z)

a = student.a["age"]
b = student.a["mother"]
c = student.b["student"]
d = student.b["father"]
print(a,' ',b,' ',c,' ',d)

for i in range(len(mary.a)):
	print(i, mary.a[i])