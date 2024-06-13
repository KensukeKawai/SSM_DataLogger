
import os
import datetime
import csv

def savefile(timeseries_data):
    path = os.getcwd()                  # Absolute Path
    dtime = datetime.datetime.now()
    now = str(dtime.year) + str(dtime.month).zfill(2) + str(dtime.day).zfill(2) + '_' + str(dtime.hour).zfill(2) + str(dtime.minute).zfill(2) + str(dtime.second).zfill(2)
    csvpath = path + '\\savedata' + '\\' + now + '.csv'      # path\yymmdd_hhmmss.csv
    
    data_transposed = [list(x) for x in zip(*timeseries_data)]
    
    #Save Measurement Data
    with open(csvpath, 'w', newline='') as csvfile:
        csvwrite = csv.writer(csvfile)
        csvwrite.writerows(data_transposed)
    
    return None