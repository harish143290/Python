

'''
   [<expression> for variable in iterable if test]
'''

lst=["Ramesh","raj","Suresh","Srija","RojA","madhu"]
print(lst)

lstr=[i for i in lst if i.startswith('R') or i.startswith('r')]
print("Result is : ",lstr)
