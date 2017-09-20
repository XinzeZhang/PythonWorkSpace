from threading import Thread
import subprocess
from Queue import Queue
import re
import sys

num_threads = 10
queue = Queue()


def pinger(i, q):
    while True:
        ip = q.get()
        ret = subprocess.call("ping -n 1 %s" % ip, shell=True,
                              stdout=open(r'ping.temp', 'w'), stderr=subprocess.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
        else:
            print "%s is down" % ip
        q.task_done()


for i in range(num_threads):
    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()


host_file = open(r'hosts.txt', 'r')
ips = []
re_obj = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
for line in host_file:
    for match in re_obj.findall(line):
        ips.append(match)
host_file.close()


for ip in ips:
    queue.put(ip)

print "Main Thread Waiting"
queue.join()
print "Done"

result = raw_input("Please press any key to exit")
if result:
    sys.exit(0)
