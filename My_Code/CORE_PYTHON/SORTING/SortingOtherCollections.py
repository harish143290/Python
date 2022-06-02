'''
    L.sort(key=None,reverse=False)
'''

t=(30,50,40,10,20,5)
'''
t.sort( )  AttributeError
  AttributeError: 'tuple' object has no attribute 'sort'
'''

s={30,40,50,20,10,4}
'''
s.sort()
   AttributeError: 'set' object has no attribute 'sort'
'''

st="abdfegchi"
'''
st.sort()
  AttributeError: 'str' object has no attribute 'sort'
'''

stu={"a":"anu","c":"cnu","b":"balu"}
'''
stu.sort()
  AttributeError: 'dict' object has no attribute 'sort'
'''
