# 1. 创建一个文件，并写入当前日期
import datetime
now = datetime.datetime.now()
print(type(now))
with open('test.txt', 'w') as file:
    # 注意write( )方法写入的内容是字符串类型
    file.write(str(now))


# 2. 再次打开这个文件，读取文件的前4个字符后退出
with open('test.txt', 'r') as file:
    text_4 = file.read(4)
    print(text_4)