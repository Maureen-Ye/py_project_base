#传递参数
def test_age(myage):
#定义参数
    my_bf_age = myage / 2 + 10
#将计算后的结果返回
    return my_bf_age

#定义变量，调用输出结果
age = test_age(32)


print('my boy friend age is',age)