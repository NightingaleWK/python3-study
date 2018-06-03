def triangle():
    name = input('您的姓名是？')
    width = int(input(name + '你好！请输入三角形的底边长：'))
    height = int(input('请输入三角形的高：'))
    result = width*height//2
    print(f'三角形的面积是： {result} ')

triangle()
