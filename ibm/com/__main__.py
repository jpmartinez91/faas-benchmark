import platform
import time
import netifaces
from db import save

passw = "bf411e2fb1145bdc381a98e07c00c5cf3cadbfef7b76cac0309828127d45826e"
username = "3e64ca7e-2cf2-43f6-8c33-203a0d72f985-bluemix"
url = "https://3e64ca7e-2cf2-43f6-8c33-203a0d72f985-bluemix:bf411e2fb1145bdc381a98e07c00c5cf3cadbfef7b76cac0309828127d45826e@3e64ca7e-2cf2-43f6-8c33-203a0d72f985-bluemix.cloudantnosqldb.appdomain.cloud"


def main(params):
    init_time = time.time()
    interfaces = netifaces.interfaces()
    inf_interfaces = []
    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        inf_interfaces.append({"int": i, "addr": addrs[netifaces.AF_LINK]})
    save(username, passw, url)
    return {
        "OS_type": platform.linux_distribution(),
        "NET_address": inf_interfaces,
        "TIME_init": init_time,
        "TIME_end": time.time()
    }
