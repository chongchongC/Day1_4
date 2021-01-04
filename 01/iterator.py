#coding=utf-8

class Data:
    def __init__(self):
        self.counter = 0
    def __iter__(self): #返回一个可迭代对象，一般是对象本身
        return self
    def __next__(self): #用来取值，就是返回一个数据；1.返回数据  2.结束迭代
        if self.counter >= 5: #控制迭代结束
            raise StopIteration
        else:
            self.counter +=1
            return "Y"

data = Data()
print(dir(data)) #打印属性
print(dir(Data))
print("Y" in data)
for d in data:
    print(d)

