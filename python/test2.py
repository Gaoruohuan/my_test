#定义一个含有5个数字的列表
list = ['abc',2,'456',4,5]

#为列表增加一个元素 100
list.append(100)
print(list)

#使用remove()删除一个元素后观察列表的变化
list.remove(2)
print(list)


#使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
print(list[:3])
print(list[-1])


ltuple1 = ('abc',2,'456',4,5)
print(ltuple1[-2])
ltuple2 = ('123','a','456','b')
ltuple3 = ltuple1+ltuple2
print(ltuple3)
print(len(ltuple3))
