'''  invalid
1.
try:
    pass
'''

''' invalid
2.
except ValueError:
    pass
'''

'''  invalid
3.
else:
    pass
'''

''' invalid 
4.
finally:
    pass
'''

'''
5.valid
try:
    pass
except:
    pass
'''

'''
6.
try:
    pass
except ValueError:
    pass
except KeyError:
    pass
'''

'''
7. valid
try:
    pass
except ValueError:
    pass
except:
    pass
'''

'''
8.invalid : Default Except means except without
exception should be the last
try:
    pass
except:
    pass
except ValueError:
    pass
'''

'''
9.valid
try:
    pass
except(ValueError,KeyError):
    pass
'''

'''
10.valid
try:
    pass
except(ValueError,KeyError) as e:
    pass
'''

'''
11.valid
try:
    pass
except(ValueError,KeyError):
    pass
else:
    pass
'''

'''
12.
try:
    pass
except(ValueError,KeyError):
    pass
else:
    pass
finally:
    pass
'''

'''Note : Based on the application req we can write
    try:
       pass
    except ExceptionClsName:
       pass

    either in the try or except or else or finally.

try:
    try:pass
    except:pass
except(ValueError,KeyError):
    pass
else:
    pass
finally:
    pass


Note : Based on the application req we can write
    try:
       pass
    except ExceptionClsName:
       pass
    else:
       pass

    either in the try or except or else or finally.

try:
    try:pass
    except:pass
except(ValueError,KeyError):
    pass
else:
    try: pass
    except ExceptionName:
        pass
    else:
        pass
finally:
    pass

Note : Based on the application req we can write
    try:
       pass
    except ExceptionClsName:
       pass
    else:
       pass
    finally:
       pass

    either in the try or except or else or finally.

try:
    try:pass
    except:pass
except(ValueError,KeyError):
    pass
else:
    try: pass
    except ExceptionName:
        pass
    else:
        pass
    finally:
        pass
finally:
    pass
'''

try:
    pass
except:
    pass

try:
    pass
finally:
    pass
    
























