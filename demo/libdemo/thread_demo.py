import threading

print(threading.main_thread())


class ChildThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print(f"Child - {i}")


ct = ChildThread()
ct.start()

for i in range(1, 11):
    print(f"Main - {i}")
