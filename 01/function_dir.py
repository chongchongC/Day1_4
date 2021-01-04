#coding=utf-8
#dir:查看可循环对象的属性

str = "abc efg" #字符串
lst = [1,2,3,4] #列表
tpl = (1,2,3,4) #元组
fle = open("data.txt") #文件

print(dir(str))
print(dir(lst))
print(dir(tpl))
print(dir(fle))

#可循环对象，都有一个__iter__方法 与 __next__方法