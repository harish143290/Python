
import collections

stu={}
stu.update({"sno":101})
stu.update({"sname":"roja"})
stu.update({"scity":"kmm"})
print(stu)
print("============================")

stu2=collections.OrderedDict()
stu2.update({"sno":101})
stu2.update({"sname":"roja"})
stu2.update({"scity":"kmm"})
print(stu2)

'''Note: update Python 3.6 dict collection is unordered
collection, from python 3.7 onwards dict collection
ordered collection '''







