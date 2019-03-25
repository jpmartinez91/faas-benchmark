import fft as exc
import json
import os
import time
import platform
import netifaces


def math(request):
    init_time = time.time()
    interfaces = netifaces.interfaces()
    inf_interfaces = []
    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        inf_interfaces.append({"int": i, "addr": addrs[netifaces.AF_LINK]})
    try:
        frequency, fourier = exc.run(20097152, 0.1)
        list_ = []
        for i in range(0, 100):
            list_.append({"frequency": frequency[i], "fourier": fourier[i]})
    except Exception as e:
        return f'Un error ocurrio {e}'
    return json.dumps(
        {
            "OS_type": platform.linux_distribution(),
            "NET_address": inf_interfaces,
            "TIME_init": init_time,
            "TIME_end": time.time()
        }
    )
