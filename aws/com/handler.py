import json

import uuid
import time as t
import platform
import sys
if "IS_LOCAL" not in os.environ:
    import unzip_requirements
    import netifaces
else:
    import netifaces
try:
    from db import save
except ImportError as e:
    print(f"Error to load module 1 {e}")
    sys.exit()


def handler(event, context):
    init_time = t.time()
    interfaces = netifaces.interfaces()
    inf_interfaces = []
    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        inf_interfaces.append({"int": i, "addr": addrs[netifaces.AF_LINK]})
    try:
        save()
    except Exception as e:
        print(e)

    response = {
        "statusCode": 200,
        "body": json.dumps(
            {
                "OS_type": platform.linux_distribution(),
                "NET_address": inf_interfaces,
                "TIME_init": init_time,
                "TIME_end": t.time()
            }
        )
    }

    return response
