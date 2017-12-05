from influxdb import InfluxDBClient
import pybitflyer
import time

user = 'root'
password = 'root'
dbname = 'bitcoin'

api = pybitflyer.API(api_key="6BfKj1imKGZyqc6cCSLrg4",
                     api_secret="j/8IcBbL2jPe5qtVCmxB7+jzIvTzTogIeNXyys2A46s=")
client = InfluxDBClient("localhost", "8086", user, password, dbname)

while True:
	try:
		ticker = api.ticker(product_code="FX_BTC_JPY")
		
		json_body = [
			{
				"measurement": "bf_ticker",
				"fields":ticker
			}
		]
		
		client.write_points(json_body)
		
		time.sleep(15)
	except:
		time.sleep(1)