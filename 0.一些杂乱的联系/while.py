# a = 1

# while a < 5:
#     print('Now the number is ' + str(a))
#     a = a + 1

flag = True
number = 1

while flag:
    if number <= 3:
        answer = input('为啥女孩喜欢穿短裙？')
        if answer == '因为方便怀孕啊':
            flag = False
            print('恭喜你答对了')
        else:
            print('woops,答错了！')
    else:
        print('尝试次数用用完了')
        break
    print(f'这是第{number}次回答')
    number += 1
    