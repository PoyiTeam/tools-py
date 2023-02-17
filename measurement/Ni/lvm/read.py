# %%
from lvm_read import read

# %%
data = read('./data/long.lvm')
print(type(data))
# %%
arr_1 = data[5]['data']
