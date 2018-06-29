# Compare
name1 = input('请输入第一个文件名')
name2 = input('请输入第二个文件名')
f1 = open('C:\\Users\\Lenovo\\Desktop\\' + name1, 'r')
f2 = open('C:\\Users\\Lenovo\\Desktop\\' + name2, 'r')
count = 0
diffent=[]
for line1 in f1:
    line2=f2.readline()
    count+=1
    if line1 != line2:
        diffent.append(count)
f1.close()
f2.close()
if len(diffent)==0:
    print('两个文件完全一样')
else:
    print('共有%d处不同，分别是：'%len(diffent))
    for i in diffent:
        print('第%d行不一样'%i)
