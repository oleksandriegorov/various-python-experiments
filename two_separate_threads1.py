
FULLSTOP=False

def handler(signal, frame):
  global FULLSTOP
  FULLSTOP=True
  print("Received signal to stop")

def watcher():
  while True:
    q.put('1.1.1.1:user.domain.com')
    time.sleep(1)
    if FULLSTOP is True:
      print("Watcher is stopping")
      break

def writer():
  while True:
    while q.empty() is False:
      print(q.get())
    time.sleep(4)
    if FULLSTOP is True:
      print("Writer is stopping")
      break


signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)
q=Queue.Queue()
t1 = threading.Thread(target=watcher)
t2 = threading.Thread(target=writer)
t1.start()
t2.start()
while FULLSTOP is False:
  time.sleep(5)
print("Main thread is stopped")
t1.join()
t2.join()
