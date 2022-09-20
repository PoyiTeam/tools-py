#%%
import queue

#%% put

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)

print(q.empty())
print(q.get())
print(q.get())
print(q.get())
print(q.empty())

#%% limited queue size, queue will stuck while queue is filled
q = queue.Queue(maxsize=3)

for i in range(5):
    q.put(i)
    print("put " + str(i))

while not q.empty():
    print(q.get())

#%% limited queue size, queue will delete oldest element and put new

max_qsize = 4
q = queue.Queue(maxsize=max_qsize)

for i in range(10):
    q.put(i)
    print("put " + str(i))
    while q.qsize() > max_qsize - 1:
        q.get(block=False)  # same as q.get_nowait()
