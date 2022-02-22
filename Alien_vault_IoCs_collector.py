from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import csv
malware_name=input('enter malware family name:   ')
input= input('enter the pulse id:   ')
otx = OTXv2("Enter you api key")
# Get all the indicators associated with a pulse
indicators = otx.get_pulse_indicators(input)
with open('./'+malware_name+'.csv','w') as add:

    for indicator in indicators:
        data=(indicator["indicator"])
        add.write(data)
        add.write("\n")
        
        # print(data, data)
       
# Get everything OTX knows about google.com
otx.get_indicator_details_full(IndicatorTypes.DOMAIN, "https://otx.alienvault.com/pulse/")
