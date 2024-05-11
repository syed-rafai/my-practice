#single  thearding
# from time import sleep
# class A:
#     def run (self):
#         for i in range(10):
#             print("hi")
#             sleep(1)# once second it will print
# class B:
#     def run(self):
#         for i in range(10):
#             print("hello")
#             sleep(1)
# t1=A()
# t2=B()

# t1.run()
# t2.run()

#multi  thearding
# from time import sleep
# from threading import Thread
# class A(Thread):
#     def run(self):
#         for i in range(10):
#             print("hi")
#             sleep(1)

# class B(Thread):
#     def run (self):
#         for i in range (10):
#             print("hello")
#             sleep(1)
# t1=A()
# t2=B()

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print("how are you ? ")

#thread synchroinzation
#inconsistency in threading
# from threading import *
# class Table: #shared resource
#     def print_table(self,number):
#         for i in range(1,11):
#             print(number,"x",i,"=",number*i)
# class my_thread(Thread):#defining a thred
#     def __init__(self,tableobj,number):
#         Thread.__init__(self)
#         self.tableobj=tableobj
#         self.number=number
#     def run (self):
#         self.tableobj.print_table(self.number)
# tableobj=Table()
# t1=my_thread(tableobj,4)
# t2=my_thread(tableobj,8)
# t3=my_thread(tableobj,7)
# t1.start()
# t2.start()
# t3.start()

#handling inconsistency in threading
# from threading import *
# class Table: #shared resource
#     def print_table(self,number):
#         for i in range(1,11):
#             print(number,"x",i,"=",number*i)
# class my_thread(Thread):#defining a thred
#     def __init__(self,tableobj,number):
#         Thread.__init__(self)
#         self.tableobj=tableobj
#         self.number=number
#     def run (self):
#         threadlock.acquire()#running thread only gets locked
#         self.tableobj.print_table(self.number)
#         threadlock.release()#releasing the particular thread
# threadlock=Lock()#creating a thread lock
# tableobj=Table()

# # tableobj=Table()
# t1=my_thread(tableobj,4)
# t2=my_thread(tableobj,8)
# t3=my_thread(tableobj,7)
# t1.start()
# t2.start()
# t3.start()

#multithreaded priority queue
# get()- The get() removes and return an item from the queue.
#put()-The put adds item to a queue
#qsize()_ the qsize()returns the number of items that are currently in the queue
#empty()- The empty() returns True if queue us empty; other Flase.
#full()- the full()returns True if queue is full; otherwise,flase

# import queue
# import threading
# import time
# thread_exit_flag=0
# class sample_Thread(threading.Thread):
#     def __init__(self,threadID,name,q):
#         threading.Thread.__init__(self)
#         self.threadId=threadID
#         self.name=name
#         self.q=q
#     def run (self):
#         print("initializing"+self.name)
#         process_data(self.name,self.q)
#         print("Exiting"+self.name)
# #helper function to process data
# def process_data(threadName,q):
#     while not thread_exit_flag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data=q.get()
#             queueLock.release()
#             print("% s processing % s" %(threadName,data))
#         else:
#             queueLock.release()
#             time.sleep(1)
# thread_list=["thread-1","Thread-2","Thread-3"]
# name_list=["A","B","C","D","E"]
# queueLock=threading.Lock()
# workQueue=queue.Queue(10)
# threads=[]
# threadID=1
# #create new threads
# for thread_name in thread_list:
#     thread=sample_Thread(threadID,thread_name,workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID+=1

# #Full the queue
# queueLock.acquire()
# for items in name_list:
#     workQueue.put(items)
# queueLock.release()
# #wait for the queue to empty
# while not workQueue.empty():
#     pass
# # notify threads it's time to exit
# thread_exit_flag=1
# #wait threads it's time to exit
# thread_exit_flag=1

# #wait for all threads to complete
# for t in threads:
#     t.join()
# print("Exit main thread")




