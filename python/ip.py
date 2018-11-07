#/bin/python
# coding: utf-8

"""
多进程抓取IP归属地并入库MYSQL
by zhangbc
last modify: 2017-04-21
"""


import sys
import requests
import re
import time
import multiprocessing
import cymysql


def get_ip_info(ip):
    """
    从百度获取IP的地址信息
    :param ip: IP地址
    :return:
    """

    rex1 = r'<span class="c-gap-right">([\S]+)</span>([\S]+) ([\S]+)'
    rex2 = r'<span class="c-gap-right">([\S]+)</span>([\S]+)'
    rex3 = r'\d+\.\d+\.\d+\.\d+'
    url = 'https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%s' % ip

    rs = requests.session()
    headers = {
        "Host": "www.baidu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    contents = rs.get(url=url, headers=headers).content.replace('IP地址:&nbsp;', '')
    data = re.findall(rex1, contents)
    if not data:
        data = re.findall(rex2, contents)

    if data and re.findall(rex3, data[0][0]):  # 必须是合法IP才记录,否则记录Errorlog
        ip_dict = dict()
        ip_dict["ip"] = data[0][0]
        ip_dict["addr"] = data[0][1]
        try:
            ip_dict["carrier"] = data[0][2]
        except:
            ip_dict["carrier"] = ""

        insert_sql = 'insert into ip_info(ip, addr, carrieroperator) VALUES ' \
              '(\'%(ip)s\', \'%(addr)s\', \'%(carrier)s\')' % ip_dict
        save(sql=insert_sql)

    time.sleep(3)


def get_ips(ia, ib, ic, ie):
    """
    获取批量IP地址
    :param ia: IP地址的A段, 若为0，则0~255
    :param ib: IP地址的B段, 若为0，则0~255
    :param ic: IP地址的C段, 若为0，则0~255
    :param ie: IP地址的D段, 若为0，则0~255
    :return: 返回IP值数组
    """

    radix = xrange(0, 256)
    if ia > 0:
        ia = xrange(ia, ia+1)
    else:
        ia = [i for i in radix if i > 0]

    if ib > 0:
        ib = xrange(ib, ib+1)
    else:
        ib = radix

    if ic > 0:
        ic = xrange(ic, ic+1)
    else:
        ic = radix

    if ie > 0:
        ie = xrange(ie, ie+1)
    else:
        ie = radix

    ips = [str(x)+"."+str(y)+"."+str(m)+"."+str(n)
           for x in ia for y in ib for m in ic for n in ie]
    return ips


def main():
    """
    实现主体函数，多进程
    :return:
    """

    pool = multiprocessing.Pool(processes=10)
    ips = get_ips(1, 1, 0, 0)
    print len(ips)
    for ip in ips:
        try:
            pool.apply_async(get_ip_info, (ip,))
        except Exception as ex:
            print ex
            pass

    pool.close()
    pool.join()


if __name__ == '__main__':

    startTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'Begin:' + startTime
    main()
    EndTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'End:%s' % EndTime