from influxdb import InfluxDBClient  # requiere pip install
from influxdb.exceptions import InfluxDBClientError
import logging
import datetime
import calendar
day_now = datetime.date.today()
now = datetime.datetime.now()
month_name = calendar.month_name[day_now.month]
year = day_now.year
logging.basicConfig(filename='db.log', level=logging.DEBUG)  # Crea archivo log


class Connector:
    def __init__(self, name):
        self.client = InfluxDBClient("localhost", 8086, database=name)
        # self.client.switch_database(name)
        self.log = logging.getLogger(
            f'RUN://{year}-{month_name}-{day_now.day}_{now.hour}:{now.minute} => ')

    def save(self, data):  # Almacena las metricas
        json_data = []
        json_data.append(data)
        try:
            return self.client.write_points(json_data, time_precision="s")
        except InfluxDBClientError as err:
            self.log.error(f"Data: \n {data} \n no pudo ser guardada")
            return False

    def desconnect(self):
        self.client.close()
