# input() 输入
has_ticket = int(input("是否有票："))
# print(has_ticket)
if has_ticket == 1:
    knife_length = float(input('请确定倒的长度： '))
    if knife_length < 20.0:
        print('允许上车!')
        exit(0)
    else:
        print('不允许上车！')
else:
    print('无票不许上车')