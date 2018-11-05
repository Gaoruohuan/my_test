# 1. 创建一个文件，并写入当前日期
test_file = open('test.txt','r',encoding='UTF-8')
print(test_file.read(10))
test_file.close()