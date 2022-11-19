#%%
fool_lst = ["apple", "orange", "cake", "あめ"]
for food in fool_lst:
    print(food)
    
#%%
for i in range(0,5,1):
    print("loop:",i)
#%%
count = 0
for i in range(0,10,2):
    print("i:", i, "count:", count)
    count += 1
    i = 1

#%%
num_lst = list(range(0,10))

result_1 = [i for i in num_lst]
print("result_1:",result_1)

result_2 = [i for i in num_lst if i > 5]
print("result_2:",result_2)