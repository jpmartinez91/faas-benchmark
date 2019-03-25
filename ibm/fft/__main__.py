import platform
import time
import netifaces
import fft as exc


def main(params):
    init_time = time.time()
    interfaces = netifaces.interfaces()
    inf_interfaces = []
    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        inf_interfaces.append({"int": i, "addr": addrs[netifaces.AF_LINK]})
    frequency, fourier = exc.run(20097152, 0.1)
    list_ = []
    for i in range(0, 100):
        list_.append({"frequency": frequency[i], "fourier": fourier[i]})
    return {
        "OS_type": platform.linux_distribution(),
        "NET_address": inf_interfaces,
        "TIME_init": init_time,
        "TIME_end": time.time()
    }
