letters = ['a','b','c','d']

# 这里是全部打印出来
# for letters in letters:  
#     print(letters)

# 打印出前两个字母
# for letters in letters[0:2]:
#     print(letters)

# 假设C是一个幸运的字母
# for letters in letters: 
#     if letters == 'c':
#         print('U are so lucky')
#     else:
#         print('Just a ' + letters)

# 假设看到C后就停止循环，跳出去
for letters in letters: 
    if letters == 'c':
        print('U are so lucky')
        break
    else:
        print('Just a ' + letters)
