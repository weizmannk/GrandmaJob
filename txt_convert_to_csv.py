import pandas as pd 
import numpy as np 
import os 
import glob 


datapath = os.getcwd()

txt_file = glob.glob((datapath+'/**/*.txt').split("/")[-1], recursive=True)
save_txt_file = [f.split(".")[0].split("_")[0] for f in txt_file]

for file in txt_file :
    for i in range(len(save_txt_file)):
            
            
        data_read = pd.read_table(file, sep=" ", header=None, names= ["Transient", "Date", "Time",  "MJD", "delay", "filter",  "mag", "err_mag", "upp_mag", "Instrument", "values", "detection", "astronomer"  ])
        
        data ={"Transient"  : data_read['Transient'], 
               "Time_Iso"   : data_read['Date'] +" "+ data_read['Time'], 
               "MJD"        : data_read['MJD'], 
               "delay"      : data_read['delay'],
               "filter"     : data_read['filter'],  
               "mag"        : data_read['mag'], 
               "err_mag"    : data_read['err_mag'], 
               "upp_mag"    : data_read['upp_mag'], 
               "Instrument" : data_read['Instrument'],
               "values"     : data_read['values'],
               "detection"  : data_read['detection'],
               "astronomer" : data_read['astronomer']
               } 
 
        df = pd.DataFrame(data=data)
       
        df.to_csv(save_txt_file[i]+".csv")