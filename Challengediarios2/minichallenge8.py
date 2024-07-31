def enqueue(queue, element):
    queue.append(element)

def dequeue(queue):
    return queue.pop(0)

def peek(queue):
    return queue[0]

mi_queue = []
enqueue(mi_queue, 30)
enqueue(mi_queue, 40)
print(peek(mi_queue))  
print(dequeue(mi_queue)) 
