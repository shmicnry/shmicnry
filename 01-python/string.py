dict1={'name':'zhangsan','age':23,'gender':'女'}
# dict1['name']='lisi'
# # dict1.pop('name')
# print(dict1.items())
#循环遍历值
# for key in dict1.keys():
#     print(key,dict1[key])
i=0
key=input('请输入字典键值:')
if key in dict1.keys():
    while key in dict1.keys():
        if i<1:
            print(key,dict1[key])
            i+=1
        else:
            break
else:
    print('输入错误，请重新输入')
key = input('请重新输入:')
print(key)
print(type(key))