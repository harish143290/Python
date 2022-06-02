

'''
   [<expression> for variable in iterable if test]
'''

lst=[i for i in range(1,21) if i%3==0 ]
print(lst)
print("- "*30)

lst_names=["anu","srinivas","cnu","balu","raj","ram"]
lst_3=list( filter(lambda n : len(n)==3 ,lst_names) )
print("Names with 3 char : ",lst_3)

lst_r=[i for i in lst_names if len(i)==3]
print("lst_r : ",lst_r)


