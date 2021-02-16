import requests
import logging
import sys
import os
import json
import pytz
from datetime import datetime
from datetime import datetime, date

logging.basicConfig(
    # format="%(asctime)s level=%(levelname)-7s %(message)s",
    format="%(message)s level=%(levelname)-7s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)


class PayloadParser:

    payload = []   

    def getIndecon(self):

        URL = "https://www.indecon.online/last"       

        try:
            r = requests.get(url=URL)

            data = r.json()

            for key, value in data.items():
                #print(value)
                #print("---------------------------------")  
                template = {}
                date_time = datetime.fromtimestamp(value["date"])
                d = date_time.strftime("%d/%m/%Y %H:%M:%S")

                
                template["key"]   = value["key"]
                template["name"]  = value["name"]
                template["unit"]  = value["unit"]
                template["date"]  = d
                template["value"] = value["value"]

                self.payload.append(template)
 
            print(self.payload)               

        except Exception as error:
            print(error)
            template = {"error":"Error en el api de Indecom Online"}
            self.payload.append(template)
            sys.exit(1)
            
        return self.payload