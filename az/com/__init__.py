import logging
import azure.functions as func
import platform
import json
import time
import netifaces
from . import db

uri = "mongodb://tesis:IwdcAGz5fHe50Ogk28zeiTDAhQXQK0Ej6QKEkKAH9j4XO4UrADWilTcsmp5TK6EE3G809KXAPWWpuxKlbs3aUA==@tesis.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"


def main(req: func.HttpRequest) -> func.HttpResponse:
    init_time = time.time()
    interfaces = netifaces.interfaces()
    inf_interfaces = []
    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        inf_interfaces.append({"int": i, "addr": addrs[netifaces.AF_LINK]})
    db.save(uri)
    return json.dumps(
        {
            "OS_type": platform.linux_distribution(),
            "NET_address": inf_interfaces,
            "TIME_init": init_time,
            "TIME_end": time.time()
        }
    )
