def search(mas1,mas2):
    a=[]
    if len(mas1)>=len(mas2):
        for i in range(0,len(mas1)):
            if mas1[i] in mas2:
                if mas1[i] not in a:
                    a.append(mas1[i])
    else:
        for i in range(0,len(mas2)):
            if mas2[i] in mas1:
                if mas2[i] not in a:
                    a.append(mas2[i])
    if len(a)<1:
        print("у массивов нет общих элементов(×﹏×)")
    else:
        print("элементы, которые содержаться в обоих массивах: ",a)

size1 = int(input('введите размер массива '))
size2 = int(input('введите размер массива '))
one, two = [], []
for i in range(0, size1):
    op = float(input('введите число '))
    one.append(op)
for i in range(0, size2):
    op = float(input('введите число '))
    two.append(op)
search (one,two)

