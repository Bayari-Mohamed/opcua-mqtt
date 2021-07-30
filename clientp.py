from opcua import Client
import time,psutil,os



def cpu_usage():
    process = psutil.Process(os.getpid())
    return process.cpu_times().user
def get_ram_in_MB():
 process = psutil.Process(os.getpid())
 return process.memory_info().rss/(1024**2)
start=0
finish=0
space_url = "opc.tcp://localhost:53530"

client = Client(space_url)
start=cpu_usage()
client.connect()
while True:
 print("------------------------------------------------")
 print("Data collection started: resource endpoint at {}".format(space_url))

 oxygen_node = client.get_node("ns=1;s=oxygen")
 oxygen_val = oxygen_node.get_value()

 print("Oxygen: " + str(oxygen_val))

 finish=cpu_usage()

 
 print("CPU Usage :",finish-start ,"%")
 print("RAM Usage :" ,get_ram_in_MB(),"Mb")
 time.sleep(3)
