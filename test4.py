#定义一个字典，分别使用a、b、c、d作为字典的关键字，值为任意内容
adir = {'a':1,'b':2,'c':3,'d':4}
print(adir)

#为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕
adir['c'] = 'cake'
print(adir)

#取出字典中关键字为d的值
print(adir['d'])

# 1. 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕
str1 = 'hello'
# 集合里的元素不能重复
print(set(str1))