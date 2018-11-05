#使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
str = 'abcdefg'
if len(str) == 10:
    print('字符串的长度等于10')
else:
    print('字符串长度不等于10')

#提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出
user_input = input('请输入1-40之间的数字:')
int_user_input = int(user_input)
if 1<=int_user_input<=10:
    print('输入的数字在1-10之间')
elif 11<=int_user_input<=20:
    print('输入的数字在11-20之间')
elif 21<=int_user_input<=30:
    print('输入的数字在21-30之间')
elif 31<=int_user_input<=40:
    print('输入的数字在31-40之间')
else:
    print('请输入正确的数值')

#使用for语句输出1-100之间的所有偶数
for num in range(1,101):
    if (num%2) == 0:
        print(num)

#使用while语句输出1-100之间能够被3整除的数字
num = 0
while num<=100:
    num = num + 1
    if num%3 == 0:
        print(num)
