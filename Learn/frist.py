name = '小谭'
if name is '谭泽宇':
    print('大傻逼')
elif name is 'tanztyu':
    print('hello tzybbb')
else:
    print('can not found name:' + name)

words = ['tt', 'zzz', 'y', 'bbbbb']
for whatever in words[:2]:
    print(whatever)
    print(len(whatever))

for test in range(5):
    print('tzy')

print('----------------')
for test in range(5, 12, 3):
    print(test)

count = 7
while count < 10:
    print(count)
    count += 1  # 跳出循环

"""
多行注释
"""

# 单行注释
print('--------again--------')

magic = 26
for change in range(50):
    if change is 2:
        print(magic, '跳出')
        break
    else:
        print(change)
print('=====================')
ExceptNumber = [1,3,5,7]
for x in range(0,25):
    if x in ExceptNumber:
        continue #break会跳出循环
    print(x)
"""    else:
        print(name)"""

fruits_available = ['grapes', 'apples', 'bananas', 'oranges', 'pears']
fruits_want = ['mangoes', 'apples', 'bananas', 'watermelons', 'pears']
for fruit in fruits_want:
    if fruit in fruits_available:
        print('We have ' + fruit +'.')
    else:
        print("Sorry, we don't have " + fruit +'.')
print('Check complete!')