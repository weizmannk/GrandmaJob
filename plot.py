import os
import glob

import optparse
from types import TracebackType
import pandas as pd
import numpy as np
from astropy.io import ascii
import optparse
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

# =============================================================================
# returns current working directory of a process.
# =============================================================================
datapath = os.getcwd()
# =============================================================================
#  input the csv file
# =============================================================================
csv_file = glob.glob((datapath+'/**/*.csv').split("/")[-1], recursive=True)
save_file_name = [f.split(".")[0] for f in csv_file]


def parse_commandline(csv):
    """[Loadind the data of cvs file ]

    :param folder: [output name to save the plots]
    :type folder: [str]
    :param csv: [ intput csv data ]
    :type csv: [type]
    :return: [return a dictionary contain plot directory, cvs file]
    :rtype: [optparse.Values]
    """

    parser = optparse.OptionParser()
    parser.add_option("--doPlots",  action="store_true", default=False)
    parser.add_option("-p", "--plotDir", default= "outputs")
    parser.add_option("-l", "--lightcurve", default=csv)

    opts, args = parser.parse_args()

    return opts


# =============================================================================
# extraction and filters cvs data
# =============================================================================
for i in range(len(csv_file)):
    # Parse command line
    opts = parse_commandline(csv_file[i])
    baseplotDir = opts.plotDir
    if not os.path.isdir(baseplotDir):
        os.makedirs(baseplotDir)
    
    save_fig_name = save_file_name[i]
    
    
    plotDir = os.path.join(baseplotDir, save_fig_name)
    if not os.path.isdir(plotDir):
        os.makedirs(plotDir)
    
    
   

    # =============================================================================
    # Read csv file 
    # =============================================================================
    all_data = ascii.read(opts.lightcurve, format='csv')
    #for transient in np.unique(all_data['Transient']):
    transient ='ZTF21ablssud'
    
        
    l = all_data[(all_data['Transient'] == transient)]
    
    #Remove charle Galdies
    lc = l[(l['Instrument'])!='ZnithObs']
    
    
    
    fig, axs = plt.subplots()
    plotName = "%s/lightcurve_%s.%s" % (plotDir, transient, 'pdf')
    
    # =============================================================================
    # Using filter to create the data table 
    # =============================================================================
    #for filt in np.unique(lc['filter']):
        
    
    for filt in ["B", "C"]:
                    
        # =========================================================================
        # Normal data
        # =========================================================================
        tab = lc[(lc['filter'] == filt) & (lc['mag']>0)]
        tab.rename_column("delay", "time")
        
        # =========================================================================
        # wrong data or upper limit mag
        # =========================================================================
        tab_upper =  lc[(lc['filter'] == filt) & (lc['mag']==0)]
        tab_upper.rename_column("delay", "time")
        
        # =========================================================================
        # data selected and reclasse by time increasing
        # =========================================================================
        tab.sort("time")
        tab_upper.sort("time")
        
        t  = tab['time']
        y  = tab['mag']
        dy = tab['err_mag']
        
        t_upper  =  tab_upper['time']
        y_upper  =  tab_upper['upp_mag']
        dy_upper =  tab_upper['err_mag']
        
        
        if filt == 'g' :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='darkolivegreen')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v', c='darkolivegreen')
                
        elif filt == 'r' :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='red')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v', c='red')

        elif filt == 'B' :
            axs.errorbar(t, y, dy, fmt='o-', label=filt, c='green')
            #axs.plot(t, y, dy, c='green')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v', c='green')
                
        elif filt == 'V' :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='darkgreen')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v',  c='darkgreen')
                
        elif filt == 'R' :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='darkred')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v',  c='darkred')
                
        elif filt == 'I' :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='lightsalmon')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v', c='lightsalmon')
                
        elif filt == 'C' :
            axs.errorbar(t, y, dy, fmt='o-', label=filt, c='yellowgreen')
            #axs.plot(t, y, c='yellowgreen')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v',  c='yellowgreen')
                
        elif filt == 'L' :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='darkorange')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v',  c='darkorange')
                
        elif filt == 'G' :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='teal')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v', c='teal')
        
        elif filt == 'w' :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='limegreen')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v', c='limegreen')
                
        elif filt == 'i' :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='blue')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v',  c='blue')
                
        else :
            axs.errorbar(t, y, dy, fmt='o', label=filt, c='k')
            if len(tab_upper) != 0:
                axs.errorbar(t_upper, y_upper, dy_upper, fmt='v',  c='k')
        
    
    axs.set_ylabel(r'Magnitude')
    axs.set_xlabel(r'ZTF First time detection')
    axs.legend(bbox_to_anchor=(1, 1), shadow=True, fancybox=True, loc='best')
    plt.tight_layout()
    axs.grid(True)
    axs.invert_yaxis()
    plt.savefig(plotName)
    plotNamePng = transient + ".png"
    #plotNamePdf = transient + ".pdf"
    plt.savefig(plotNamePng)
    #plt.savefig(plotNamePdf)
    plt.show()
            
