
import gc

print("is GC enabled ? : ",gc.isenabled() )
gc.disable()
print("is GC enabled ? : ",gc.isenabled() )
gc.enable()
print("is GC enabled ? : ",gc.isenabled() )
