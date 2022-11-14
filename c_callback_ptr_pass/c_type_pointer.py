# %%
import ctypes
# %%

CONSTANT_VALUE = 10

# %% pointer for void
value_pointer = ctypes.c_void_p(CONSTANT_VALUE)
value_pointer.value

# %% pointer for class


class myClass:
    pass


myclass = myClass()
class_pointer = ctypes.py_object(myClass)
print(class_pointer)
print(class_pointer.value)
