poem = '''\
programming is fun
when the work is done
if you wanna make your work also fun:
   use python!
'''

#打开文件以编辑（'w'riting)
f = open("E:\测试文档\poem.txt","w")
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()

    if len(line)==0:
        break
    print(line,end="")

f.close()

