#打印小星星
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print('%d*%d=%d'%(i,j,i*j),end='\t')
#         # print(f'{i} * {j} = {i*j}',end='\t')
#         j+=1
#     print()
#     i+=1


for i in range(1,10,1):
    for j in range(1,i+1,1):
        print('%d*%d=%d' %(i,j,i*j),end='\t')
    print()
    continue