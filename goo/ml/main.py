import flask
import predict
import json
import tempfile
import os
import time
import platform
import netifaces


def ml(request):
    init_time = time.time()
    interfaces = netifaces.interfaces()
    inf_interfaces = []
    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        inf_interfaces.append({"int": i, "addr": addrs[netifaces.AF_LINK]})
    prediccion = []
    try:
        prediccion = predict.run()
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
