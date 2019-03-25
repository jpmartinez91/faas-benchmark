import json
import logging
import azure.functions as func
import platform
import netifaces
from . import predict
import time


def main(req: func.HttpRequest) -> func.HttpResponse:
    init_time = time.time()
    interfaces = netifaces.interfaces()
    inf_interfaces = []
    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        inf_interfaces.append({"int": i, "addr": addrs[netifaces.AF_LINK]})
    try:
        predecir = predict.run()
    except Exception as e:
        return func.HttpResponse(f"Error {e}")
    return json.dumps(
        {
            "OS_type": platform.linux_distribution(),
            "NET_address": inf_interfaces,
            "TIME_init": init_time,
            "TIME_end": time.time()
        }
    )
