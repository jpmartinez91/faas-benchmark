
import time
from db import save
import platform
import netifaces
import json


def com(request):
    init_time = time.time()
    interfaces = netifaces.interfaces()
    inf_interfaces = []
    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        inf_interfaces.append({"int": i, "addr": addrs[netifaces.AF_LINK]})
    save()
    return json.dumps(
        {
            "OS_type": platform.linux_distribution(),
            "NET_address": inf_interfaces,
            "TIME_init": init_time,
            "TIME_end": time.time()
        }
    )
