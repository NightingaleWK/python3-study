def zhihu(func): # 这里定义一个zhihu的参数，func是一个var，任何值都行，届时数据会传给func
    def warpper():
        print('谢邀')
        func() #a就是下面那几个的函数
        print('以上')
    return warpper

@zhihu #@zhihu是answer1 = zhihu(answer1)的简化
def answer1(): # 当我们执行到这，会执行zhihu函数，answer会被当作一个参数传到zhihu里的func
    print('我1啥也不知道')

@zhihu
def answer2():
    print('我2也是都不知道')

@zhihu
def answer3():
    print('我是3，也不知道')

@zhihu
def answer4():
    print('那我叫4！啥都不知道')

@zhihu
def answer5():
    print('我5因为不知道所以不知道')


answer1()
answer2()
answer3()
answer4()
answer5()