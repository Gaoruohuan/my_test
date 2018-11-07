#美元转换人民币
from decimal import Decimal
#import sys
#money = sys.argv[1]
money = input('请输入面值')
currency = money[-1]
value = int(money[:-1])
rate = Decimal('6.9465')

if currency == '$':
    print(str(value)+'美元等于{rmb}人民币'.format(rmb=str(value*rate)))
elif currency == '￥':
    print(str(value)+'人民币等于{dol}美元'.format(dol=str(value/rate)))
else:
    print('请输入正确的参数')
