new = ["himanshi","sakshi",'manju','jyoti','vijay','anil','raju','preeta']
print(new)

print(len(new))

print(type(new))

print(new[0:2])
print(new[2:4])
print(new[4:6])
print(new[6:8])

print(new[0:7:2])
print(new[0:7:3])

list = ['sakshi','himanshi','preeta','srishti','karan','rishabh']
print(list)

print(f'Good work done by , {list[0]}'.title())
print(f'Great job , {list[1]}'.title())

for student in list:
    print(f"Great job , {student}".title() )

for x in new:
    print(f"Please send your emails , {x}")

for ironman in list:
    print(f"Good work done {ironman}".title())
    print(f"Please send me your all details  {ironman} ".title())

for ironman in list:
    print(f"Good work done {ironman}".title())
    print(f"Please send me your all details  {ironman} \n  ".title())