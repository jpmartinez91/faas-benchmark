import sys
import json
import os
import platform
import time
if "IS_LOCAL" not in os.environ:
    import unzip_requirements
    import netifaces
else:
    import netifaces
try:
    from . import fft as exc
except ImportError as e:
    import fft as exc


def handler(event, context):
    init_time = time.time()
    interfaces = netifaces.interfaces()
    inf_interfaces = []
    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        inf_interfaces.append({"int": i, "addr": addrs[netifaces.AF_LINK]})
    try:
        frequency, fourier = exc.run(20097152, 0.1)
    except Exception as e:
        return f'Un error ocurrio {e}'
    else:
        list_ = []
        for i in range(0, 100):
            list_.append({"frequency": frequency[i], "fourier": fourier[i]})
    response = {
        "statusCode": 200,
        "body": json.dumps(
            {
                "OS_type": platform.linux_distribution(),
                "NET_address": inf_interfaces,
                "TIME_init": init_time,
                "TIME_end": time.time()
            }
        )
    }
    return response
