def test_age(myage = 50):
    my_bf_age = myage / 2 + 10
    return my_bf_age

#定义变量输出结果
age1 = test_age(22)
age2 = test_age() #默认传了定义过的值（myagge=50）

print('my boy friend age is',age1)
print('my boy friend age is',age2)