# a=1
# b='1'
# c=''
# c=str(a)+b
# print(a,end='')
# print(b,end='')
# print(c,end='')

# if __name__ == '__main__':

    # a = input("亲输入一个数字：")
    # print(a)
    # b=[1,2,'1']
    # a=(1,'1',b)
    # print(b)
    # print(a)
    # print(a[2])
    # print(b[0:2])
    # print(type(b))
    # print(type(a))
# a=(1,2,3)
# b=(2,3,'qwe')
# c=(a,b)
# d=(1,)
# print(c[0][2])
# print(c[1][1])
# print(a[0])
# print(a+b)
# print(c[1])
# print(a[0:2:1])
# list1=[1,2,34,33]
# list2=[2,34,55,3]
# list1.append(list2[1])
# list1.extend(list2)
# a=list1.count(34)
# list1.reverse()
# b=len(list1)
# print(a)
# print(b)
# print(list1)
# for i in range(b):
#     print(list1[i])
# print(b)


dic = {'ei':23,'e3':23}
dic1={}
# dic['fj'] = 23
# del (dic['fj'])
# dic['ei']=20
# print(type(dic['ei']))
# print(dic['ei'])
# print(dic)
# print(type(dic))
# # r=dic.items()
# # print(r)
# o=dic.values()
# print()
# print(o)
# k=['fj','jf']
# s=[1,2]
# dic2=dic.fromkeys(k,s)
# print(dic2)
# print(type(dic2))

# str= 'this is my name\nmy name is il'
# a=str.splitlines()
# b=str.rsplit()
# print(b)
#
# d = {1,23,3}
# print(d)
# print(type(d))
# s = '111222 333333'
# a = s.rsplit(' ')
# print(a)
# print(len(a))


def fj(n):
    if n==10:
        return(4+n)
    elif n==15:
        return (5*n)
    else:
        return ((n+1)*5/4+1)


def fj1(n):
    while n>1:
        if n==3:
            n=n-1
            continue
        print(n)
        n=n-1
        if(n==5):
            break
    return n

def fj2(n):
    for i in range(n):
        if i==3:
            return i
        print(i)
    return 0

def test():
    # print('说明fj02(n),这是一个for 循环函数，参数n是数字整数'
    #       '执行功能是打印0-（n-1）的数值，直到3，函数返回返回值为3，正常返回值为0')
    # print('')
    print('函数测试 调用fj2(5)')
    fj2(5)
    return 0 #-1是错误 0收正确 其他值是错误代码

if __name__ == '__main__':
    # print(fj(10))
    # fj1(5)
    # fj2(5)
    # test()
    list=[]
    dic = {'fj':1,'fie0':12}
    list.extend(dic.values())
    print(list)
