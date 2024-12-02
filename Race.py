import os, signal, time
from multiprocessing import Value, Array

count = Value('i', 0)
processid = os.fork()
#print(processid)

# processid > 0 represents the parent process
if processid > 0 :
  print("\nParent Process:")
  print("Process ID:", os.getpid())
  print("Child's process ID:", processid)
  for i in range(0,1000):
    count.value = count.value + 1
  print("Parent Process: count.value ",count.value)
  time.sleep(1.0) #Wait for the process has done in the child process

  os.kill(processid, signal.SIGSTOP)
  print("Child stopped...")
  print("Parent Process: count.value ",count.value)

# processid = 0 represents the created child process
else :
  print("\nChild Process:")
  print("Process ID:", os.getpid())
  print("Parent's process ID:", os.getppid())
  for i in range(0,1000):
    count.value = count.value + 1
  print("Child Process: count.value ",count.value)
  