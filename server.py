
from opcua import Server
from random import randint
import time
from random import randrange, uniform , choice
from string import ascii_lowercase, ascii_uppercase
import sys,psutil,os

def getRandomstrimg(size):
    return"".join(choice(all_chars)
    for i in range(size))


def cpu_usage():
    process = psutil.Process(os.getpid())
    return process.cpu_times().user
def get_ram_in_MB():
 process = psutil.Process(os.getpid())
 return process.memory_info().rss/(1024**2)
start=0
finish=0
j=0
server = Server()
start=cpu_usage()
space_url = "opc.tcp://localhost:53530"

server.set_endpoint(space_url)
node = server.get_objects_node()
oxygen = node.add_variable("ns=1;s=oxygen", "Oxygen", 0)
oxygen.set_writable()
all_chars = ascii_lowercase + ascii_uppercase
server.start()
while j<=1000:
 
 oxygen_val = getRandomstrimg(10)
 oxygen.set_value(oxygen_val)
 
 
 finish=cpu_usage()
 print("------------------------------------------------")
 print("val s " + str(oxygen_val) + " to Topic TEMPERATURE")
 print(sys.getsizeof(oxygen_val))
 print("CPU Usage :",finish-start ,"%")
 print("RAM Usage :" ,get_ram_in_MB(),"Mb")
 time.sleep(3)
 
