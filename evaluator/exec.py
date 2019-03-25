import concurrent.futures
import models
import sys
import argparse
import time
import requests
import save
from datetime import datetime

InfluxDB = save.Connector(f"faas_benchmark")
# Establece La base de datos a utilizar
# InfluxDB.setDb(f"faas_benchmark")


def request(func):
    provider = func.provider
    function = func.func
    time_call = time.time()
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    result = requests.get(url=func.url)
    if result.status_code == requests.codes.ok:
        time_respose = time.time()
        data = result.json()
        data_tags = {}
        data_tags["provider"] = provider
        data_tags["function"] = function
        data_fields = {}
        keys = data.keys()
        if "message" not in keys:
            if type(data["OS_type"]) == list:
                data_fields["OS_type"] = data["OS_type"][0]
                data_fields["OS_release"] = data["OS_type"][1]
            # tiempo de ejecucion en la nube
            data_fields["TIME_init"] = data["TIME_init"]
            data_fields["TIME_end"] = data["TIME_end"]
            # tiempo de llamada y respuesta
            data_fields["TIME_requests"] = time_call
            data_fields["TIME_respose"] = time_respose
            # tiempo real de ejecucion
            data_fields["TIME_exec"] = data["TIME_end"] - data["TIME_init"]
            # Tiempo de espera entre llamada e inicio de ejecucion
            data_fields["TIME_request_initExee"] = time_call - \
                data["TIME_init"]
            # Tiempo de espera entre fin de ejecucion y devolucion de respuesta
            data_fields["TIME_endExe_response"] = time_respose - \
                data["TIME_end"]
            # tiempo dutacion de llamada
            data_fields["TIME_request_response"] = time_respose - time_call
            for net in data["NET_address"]:
                if net["int"] != "lo" and net["addr"][0]["addr"] != "00:00:00:00:00:00":
                    data_fields[net["int"]] = net["addr"][0]["addr"]
            data_to_db = {}
            data_to_db["measurement"] = f'metric_{function}'
            data_to_db["tags"] = data_tags
            data_to_db["time"] = current_time
            data_to_db["fields"] = data_fields
            InfluxDB.save(data_to_db)
        else:
            print("err")
    print(f"Process {os.getpid()} is processing function {func.func} - {func.provider} whit status.code {result.status_code}")


def run(funcs):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(request, funcs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prepare to call the Cloud functions")
    parser.add_argument('-f', '--function', default="local",
                        metavar='function',
                        help='-f 1 : math | -f 2 : com | -f 3 ml')
    args = parser.parse_args()
    try:
        # if args.function == "1":
        #     run(models.functionsMath)
        # elif args.function == "2":
        #     run(models.functionsCom)
        if args.function == "1":
            run(models.functionsCom)
        elif args.function == "local":
            run(models.functionsLocal)
        else:
            sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)
