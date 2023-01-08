# https://quantcorner.wordpress.com/2014/11/18/downloading-eias-data-with-python/

import json
import numpy as np
import pandas as pd
from urllib.error import URLError, HTTPError
from urllib.request import urlopen




class EIAtakeDataBySeriesID(object):
    
    def __init__(self, token, seriesID):
       
        self.token = token
        self.seriesID = seriesID
        self.RawData = self.TakeRawData()
        self.TimeSeries = self.TakeTimeSeries()
        self.Unit = self.TakeUnit()
        self.Name = self.TakeName()

        
    def TakeRawData(self):
        # Construct url
        url = 'http://api.eia.gov/series/?api_key=' + self.token + \
                   '&series_id=' + self.seriesID.upper()

        try:
            # URL request, URL opener, read content
            response = urlopen(url);
            raw_byte = response.read()
            raw_string = str(raw_byte, 'utf-8-sig')
            jso = json.loads(raw_string)
            return jso

        except HTTPError as e:
            print('HTTP error type.')
            print('Error code: ', e.code)

        except URLError as e:
            print('URL type error.')
            print('Reason: ', e.reason)


    def TakeTimeSeries(self):
        
        DateTimeFormat = None
        
        if self.TakeFrequency == 'H':
            DateTimeFormat = '%Y%m%dT%HZ'
        elif self.TakeFrequency == 'D':
            DateTimeFormat = '%Y%m%d'
            
        dateSeries = self.RawData['series'][0]['data']
        dateSeriesDF = pd.DataFrame(dateSeries, columns = ['Date','value'])\
                        .assign(Date = lambda x: pd.to_datetime(x['Date'], \
                                                        format=DateTimeFormat) ) \
                       .set_index('Date')
        return dateSeriesDF


    def TakeUnit(self):   
        
        Unit = self.RawData['series'][0]['units']      
        return Unit
    
    
    def TakeName(self):
        
        Name = self.RawData['series'][0]['name']      
        return Name
    
    def TakeFrequency(self):
        
        Name = self.RawData['series'][0]['f']      
        return f