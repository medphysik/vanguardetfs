import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import DataFrame
import numpy as np
from scipy import stats
import scipy.stats as stats
from scipy.stats import kurtosis

import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import pingouin as pg
from pingouin import ttest
import dash_table
import yfinance as yf

from pingouin import pairwise_ttests, read_dataset


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats
import scipy.stats as stats
from scipy.stats import kurtosis

import pingouin as pg
from pingouin import ttest

from pingouin import pairwise_ttests, read_dataset




from chart_studio.plotly import plot, iplot

import chart_studio.plotly as py
import cufflinks as cf
import pandas as pd
import numpy as np


import cufflinks as cf
import pandas as pd
import numpy as np

import plotly.tools as tls


import plotly.express as px

import chart_studio.plotly as py
import cufflinks as cf
import pandas as pd
import numpy as np

import pandas as pd

import chart_studio
chart_studio.tools.set_credentials_file(username='medphysik', api_key='NH7LBFZU8YzsfvhGfOoe')
# make plots

cf.go_offline()


data = yf.download("EDV BIV VGIT BLV VGLT VMBS BSV VTIP VGSH BND VCIT VCLT VCSH VTC VTEB VIG ESGV VUG VYM VV MGC MGK MGV VONE VONG VONV VTHR VOO VOOG VOOV VTI VTV VXF VO VOT VOE IVOO IVOG IVOV VTWO VTWG VTWV VIOO VIOG VIOV VB VBK VBR BNDW BNDX VWOB VT VSGX VEU VSS VEA VGK VPL VNQI VIGI VYMI VXUS VWO VOX VCR VDC VDE VFH VHT VIS VGT VAW VNQ VPU", period = "1d", interval = "15m")

dfdata = pd.DataFrame(data=data)

#print(dfdata.columns)
#print(dfdata['Adj Close', 'BNDW'])


#print plots of different classes


#US bond ETFs

USbondETF = { 'EDV': dfdata['Close', 'EDV'], 'BIV': dfdata['Close', 'BIV'], 'VGIT': dfdata['Close', 'VGIT'], 'BLV': dfdata['Close', 'BLV'], 'VGLT': dfdata['Close', 'VGLT'], 'VMBS': dfdata['Close', 'VMBS'], 'BSV': dfdata['Close', 'BSV'], 'VTIP': dfdata['Close', 'VTIP'], 'VGSH': dfdata['Close', 'VGSH'], 'BND': dfdata['Close', 'BND'], 'VCIT': dfdata['Close', 'VCIT'], 'VCLT': dfdata['Close', 'VCLT'], 'VCSH': dfdata['Close', 'VCSH'], 'VTC': dfdata['Close', 'VTC'], 'VTEB': dfdata['Close', 'VTEB']}
dfUSbondETF = pd.DataFrame(data=USbondETF)

normalized_dfUSbondETF=(dfUSbondETF)/(dfUSbondETF.max())


#US stock ETFs

USstockETF = { 'VIG': dfdata['Close', 'VIG'], 'ESGV': dfdata['Close', 'ESGV'], 'VUG': dfdata['Close', 'VUG'], 'VYM': dfdata['Close', 'VYM'], 'VV': dfdata['Close', 'VV'], 'MGC': dfdata['Close', 'MGC'], 'MGK': dfdata['Close', 'MGK'], 'MGV': dfdata['Close', 'MGV'], 'VONE': dfdata['Close', 'VONE'], 'VONG': dfdata['Close', 'VONG'], 'VONV': dfdata['Close', 'VONV'], 'VTHR': dfdata['Close', 'VTHR'], 'VOO': dfdata['Close', 'VOO'], 'VOOG': dfdata['Close', 'VOOG'], 'VOOV': dfdata['Close', 'VOOV'], 'VTI': dfdata['Close', 'VTI'], 'VTV': dfdata['Close', 'VTV'],'VXF': dfdata['Close', 'VXF'],'VO': dfdata['Close', 'VO'],'VOT': dfdata['Close', 'VOT'],'VOE': dfdata['Close', 'VOE'],'IVOO': dfdata['Close', 'IVOO'],'IVOG': dfdata['Close', 'IVOG'],'IVOV': dfdata['Close', 'IVOV'],'VTWO': dfdata['Close', 'VTWO'],'VTWG': dfdata['Close', 'VTWG'],'VTWV': dfdata['Close', 'VTWV'],'VIOO': dfdata['Close', 'VIOO'],'VIOG': dfdata['Close', 'VIOG'],'VIOV': dfdata['Close', 'VIOV'],'VB': dfdata['Close', 'VB'],'VBK': dfdata['Close', 'VBK'],'VBR': dfdata['Close', 'VBR']}
dfUSstockETF = pd.DataFrame(data=USstockETF)

normalized_dfUSstockETF=(dfUSstockETF)/(dfUSstockETF.max())


#International Bond ETF

INTbondETF = { 'BNDW': dfdata['Close', 'BNDW'], 'BNDX': dfdata['Close', 'BNDX'], 'VWOB': dfdata['Close', 'VWOB']}
dfINTbondETF = pd.DataFrame(data=INTbondETF)

normalized_dfINTbondETF=(dfINTbondETF)/(dfINTbondETF.max())



#INT stock ETFs

INTstockETF = { 'VSGX': dfdata['Close', 'VSGX'], 'VEU': dfdata['Close', 'VEU'], 'VSS': dfdata['Close', 'VSS'], 'VEA': dfdata['Close', 'VEA'], 'VGK': dfdata['Close', 'VGK'], 'VPL': dfdata['Close', 'VPL'], 'VNQI': dfdata['Close', 'VNQI'], 'VIGI': dfdata['Close', 'VIGI'], 'VYMI': dfdata['Close', 'VYMI'], 'VXUS': dfdata['Close', 'VXUS'], 'VWO': dfdata['Close', 'VWO']}
dfINTstockETF = pd.DataFrame(data=INTstockETF)

normalized_dfINTstockETF=(dfINTstockETF)/(dfINTstockETF.max())


#US stock Sector ETFs

USstocksectorETF = { 'VOX': dfdata['Close', 'VOX'], 'VCR': dfdata['Close', 'VCR'], 'VDC': dfdata['Close', 'VDC'], 'VDE': dfdata['Close', 'VDE'], 'VFH': dfdata['Close', 'VFH'], 'VHT': dfdata['Close', 'VHT'], 'VIS': dfdata['Close', 'VIS'], 'VGT': dfdata['Close', 'VGT'], 'VAW': dfdata['Close', 'VAW'], 'VNQ': dfdata['Close', 'VNQ'], 'VPU': dfdata['Close', 'VPU']}
dfUSstocksectorETF = pd.DataFrame(data=USstocksectorETF)

normalized_dfUSstocksectorETF=(dfUSstocksectorETF)/(dfUSstocksectorETF.max())



#Total Vanguard ETFs

TOTALETF=pd.concat([dfUSbondETF, dfUSbondETF, dfINTstockETF, dfINTbondETF, dfUSstocksectorETF], axis=1)

#USbondETF+USstockETF+INTbondETF+INTstockETF+USstocksectorETF

dfTOTALETF = pd.DataFrame(data=TOTALETF)

normalized_dfTOTALETF=(dfTOTALETF)/(dfTOTALETF.max())

#Total Vanguard ETFs2


TOTALETF2={'EDV': dfdata['Close', 'EDV'], 'BIV': dfdata['Close', 'BIV'], 'VGIT': dfdata['Close', 'VGIT'], 'BLV': dfdata['Close', 'BLV'], 'VGLT': dfdata['Close', 'VGLT'], 'VMBS': dfdata['Close', 'VMBS'], 'BSV': dfdata['Close', 'BSV'], 'VTIP': dfdata['Close', 'VTIP'], 'VGSH': dfdata['Close', 'VGSH'], 'BND': dfdata['Close', 'BND'], 'VCIT': dfdata['Close', 'VCIT'], 'VCLT': dfdata['Close', 'VCLT'], 'VCSH': dfdata['Close', 'VCSH'], 'VTC': dfdata['Close', 'VTC'], 'VTEB': dfdata['Close', 'VTEB'], 'VIG': dfdata['Close', 'VIG'], 'ESGV': dfdata['Close', 'ESGV'], 'VUG': dfdata['Close', 'VUG'], 'VYM': dfdata['Close', 'VYM'], 'VV': dfdata['Close', 'VV'], 'MGC': dfdata['Close', 'MGC'], 'MGK': dfdata['Close', 'MGK'], 'MGV': dfdata['Close', 'MGV'], 'VONE': dfdata['Close', 'VONE'], 'VONG': dfdata['Close', 'VONG'], 'VONV': dfdata['Close', 'VONV'], 'VTHR': dfdata['Close', 'VTHR'], 'VOO': dfdata['Close', 'VOO'], 'VOOG': dfdata['Close', 'VOOG'], 'VOOV': dfdata['Close', 'VOOV'], 'VTI': dfdata['Close', 'VTI'], 'VTV': dfdata['Close', 'VTV'],'VXF': dfdata['Close', 'VXF'],'VO': dfdata['Close', 'VO'],'VOT': dfdata['Close', 'VOT'],'VOE': dfdata['Close', 'VOE'],'IVOO': dfdata['Close', 'IVOO'],'IVOG': dfdata['Close', 'IVOG'],'IVOV': dfdata['Close', 'IVOV'],'VTWO': dfdata['Close', 'VTWO'],'VTWG': dfdata['Close', 'VTWG'],'VTWV': dfdata['Close', 'VTWV'],'VIOO': dfdata['Close', 'VIOO'],'VIOG': dfdata['Close', 'VIOG'],'VIOV': dfdata['Close', 'VIOV'],'VB': dfdata['Close', 'VB'],'VBK': dfdata['Close', 'VBK'],'VBR': dfdata['Close', 'VBR'], 'BNDW': dfdata['Close', 'BNDW'], 'BNDX': dfdata['Close', 'BNDX'], 'VWOB': dfdata['Close', 'VWOB'],'VSGX': dfdata['Close', 'VSGX'], 'VEU': dfdata['Close', 'VEU'], 'VSS': dfdata['Close', 'VSS'], 'VEA': dfdata['Close', 'VEA'], 'VGK': dfdata['Close', 'VGK'], 'VPL': dfdata['Close', 'VPL'], 'VNQI': dfdata['Close', 'VNQI'], 'VIGI': dfdata['Close', 'VIGI'], 'VYMI': dfdata['Close', 'VYMI'], 'VXUS': dfdata['Close', 'VXUS'], 'VWO': dfdata['Close', 'VWO'],'VOX': dfdata['Close', 'VOX'], 'VCR': dfdata['Close', 'VCR'], 'VDC': dfdata['Close', 'VDC'], 'VDE': dfdata['Close', 'VDE'], 'VFH': dfdata['Close', 'VFH'], 'VHT': dfdata['Close', 'VHT'], 'VIS': dfdata['Close', 'VIS'], 'VGT': dfdata['Close', 'VGT'], 'VAW': dfdata['Close', 'VAW'], 'VNQ': dfdata['Close', 'VNQ'], 'VPU': dfdata['Close', 'VPU']}

dfTOTALETF2 = pd.DataFrame(data=TOTALETF2)

normalized_dfTOTALETF2=(dfTOTALETF2)/(dfTOTALETF2.max())




#total
df=normalized_dfTOTALETF2

#figures for 1 day


figure2=df.corr(method='spearman').iplot(asFigure=True,kind='heatmap',title="Spearman Total Vanguard ETFs 1D",  filename='SpearmanTotal Vanguard ETFs 1D', colorscale='spectral')

figure1=df.iplot(asFigure=True, title = "Stocks 1 D normalized", xTitle="Time", yTitle="Normalized Price")

#1month
data = yf.download("EDV BIV VGIT BLV VGLT VMBS BSV VTIP VGSH BND VCIT VCLT VCSH VTC VTEB VIG ESGV VUG VYM VV MGC MGK MGV VONE VONG VONV VTHR VOO VOOG VOOV VTI VTV VXF VO VOT VOE IVOO IVOG IVOV VTWO VTWG VTWV VIOO VIOG VIOV VB VBK VBR BNDW BNDX VWOB VT VSGX VEU VSS VEA VGK VPL VNQI VIGI VYMI VXUS VWO VOX VCR VDC VDE VFH VHT VIS VGT VAW VNQ VPU", period = "1mo")

dfdata = pd.DataFrame(data=data)

#print(dfdata.columns)
#print(dfdata['Adj Close', 'BNDW'])


#print plots of different classes


#US bond ETFs

USbondETF = { 'EDV': dfdata['Close', 'EDV'], 'BIV': dfdata['Close', 'BIV'], 'VGIT': dfdata['Close', 'VGIT'], 'BLV': dfdata['Close', 'BLV'], 'VGLT': dfdata['Close', 'VGLT'], 'VMBS': dfdata['Close', 'VMBS'], 'BSV': dfdata['Close', 'BSV'], 'VTIP': dfdata['Close', 'VTIP'], 'VGSH': dfdata['Close', 'VGSH'], 'BND': dfdata['Close', 'BND'], 'VCIT': dfdata['Close', 'VCIT'], 'VCLT': dfdata['Close', 'VCLT'], 'VCSH': dfdata['Close', 'VCSH'], 'VTC': dfdata['Close', 'VTC'], 'VTEB': dfdata['Close', 'VTEB']}
dfUSbondETF = pd.DataFrame(data=USbondETF)

normalized_dfUSbondETF=(dfUSbondETF)/(dfUSbondETF.max())


#US stock ETFs

USstockETF = { 'VIG': dfdata['Close', 'VIG'], 'ESGV': dfdata['Close', 'ESGV'], 'VUG': dfdata['Close', 'VUG'], 'VYM': dfdata['Close', 'VYM'], 'VV': dfdata['Close', 'VV'], 'MGC': dfdata['Close', 'MGC'], 'MGK': dfdata['Close', 'MGK'], 'MGV': dfdata['Close', 'MGV'], 'VONE': dfdata['Close', 'VONE'], 'VONG': dfdata['Close', 'VONG'], 'VONV': dfdata['Close', 'VONV'], 'VTHR': dfdata['Close', 'VTHR'], 'VOO': dfdata['Close', 'VOO'], 'VOOG': dfdata['Close', 'VOOG'], 'VOOV': dfdata['Close', 'VOOV'], 'VTI': dfdata['Close', 'VTI'], 'VTV': dfdata['Close', 'VTV'],'VXF': dfdata['Close', 'VXF'],'VO': dfdata['Close', 'VO'],'VOT': dfdata['Close', 'VOT'],'VOE': dfdata['Close', 'VOE'],'IVOO': dfdata['Close', 'IVOO'],'IVOG': dfdata['Close', 'IVOG'],'IVOV': dfdata['Close', 'IVOV'],'VTWO': dfdata['Close', 'VTWO'],'VTWG': dfdata['Close', 'VTWG'],'VTWV': dfdata['Close', 'VTWV'],'VIOO': dfdata['Close', 'VIOO'],'VIOG': dfdata['Close', 'VIOG'],'VIOV': dfdata['Close', 'VIOV'],'VB': dfdata['Close', 'VB'],'VBK': dfdata['Close', 'VBK'],'VBR': dfdata['Close', 'VBR']}
dfUSstockETF = pd.DataFrame(data=USstockETF)

normalized_dfUSstockETF=(dfUSstockETF)/(dfUSstockETF.max())


#International Bond ETF

INTbondETF = { 'BNDW': dfdata['Close', 'BNDW'], 'BNDX': dfdata['Close', 'BNDX'], 'VWOB': dfdata['Close', 'VWOB']}
dfINTbondETF = pd.DataFrame(data=INTbondETF)

normalized_dfINTbondETF=(dfINTbondETF)/(dfINTbondETF.max())



#INT stock ETFs

INTstockETF = { 'VSGX': dfdata['Close', 'VSGX'], 'VEU': dfdata['Close', 'VEU'], 'VSS': dfdata['Close', 'VSS'], 'VEA': dfdata['Close', 'VEA'], 'VGK': dfdata['Close', 'VGK'], 'VPL': dfdata['Close', 'VPL'], 'VNQI': dfdata['Close', 'VNQI'], 'VIGI': dfdata['Close', 'VIGI'], 'VYMI': dfdata['Close', 'VYMI'], 'VXUS': dfdata['Close', 'VXUS'], 'VWO': dfdata['Close', 'VWO']}
dfINTstockETF = pd.DataFrame(data=INTstockETF)

normalized_dfINTstockETF=(dfINTstockETF)/(dfINTstockETF.max())


#US stock Sector ETFs

USstocksectorETF = { 'VOX': dfdata['Close', 'VOX'], 'VCR': dfdata['Close', 'VCR'], 'VDC': dfdata['Close', 'VDC'], 'VDE': dfdata['Close', 'VDE'], 'VFH': dfdata['Close', 'VFH'], 'VHT': dfdata['Close', 'VHT'], 'VIS': dfdata['Close', 'VIS'], 'VGT': dfdata['Close', 'VGT'], 'VAW': dfdata['Close', 'VAW'], 'VNQ': dfdata['Close', 'VNQ'], 'VPU': dfdata['Close', 'VPU']}
dfUSstocksectorETF = pd.DataFrame(data=USstocksectorETF)

normalized_dfUSstocksectorETF=(dfUSstocksectorETF)/(dfUSstocksectorETF.max())



#Total Vanguard ETFs

TOTALETF=pd.concat([dfUSbondETF, dfUSbondETF, dfINTstockETF, dfINTbondETF, dfUSstocksectorETF], axis=1)

#USbondETF+USstockETF+INTbondETF+INTstockETF+USstocksectorETF

dfTOTALETF = pd.DataFrame(data=TOTALETF)

normalized_dfTOTALETF=(dfTOTALETF)/(dfTOTALETF.max())

#Total Vanguard ETFs2


TOTALETF2={'EDV': dfdata['Close', 'EDV'], 'BIV': dfdata['Close', 'BIV'], 'VGIT': dfdata['Close', 'VGIT'], 'BLV': dfdata['Close', 'BLV'], 'VGLT': dfdata['Close', 'VGLT'], 'VMBS': dfdata['Close', 'VMBS'], 'BSV': dfdata['Close', 'BSV'], 'VTIP': dfdata['Close', 'VTIP'], 'VGSH': dfdata['Close', 'VGSH'], 'BND': dfdata['Close', 'BND'], 'VCIT': dfdata['Close', 'VCIT'], 'VCLT': dfdata['Close', 'VCLT'], 'VCSH': dfdata['Close', 'VCSH'], 'VTC': dfdata['Close', 'VTC'], 'VTEB': dfdata['Close', 'VTEB'], 'VIG': dfdata['Close', 'VIG'], 'ESGV': dfdata['Close', 'ESGV'], 'VUG': dfdata['Close', 'VUG'], 'VYM': dfdata['Close', 'VYM'], 'VV': dfdata['Close', 'VV'], 'MGC': dfdata['Close', 'MGC'], 'MGK': dfdata['Close', 'MGK'], 'MGV': dfdata['Close', 'MGV'], 'VONE': dfdata['Close', 'VONE'], 'VONG': dfdata['Close', 'VONG'], 'VONV': dfdata['Close', 'VONV'], 'VTHR': dfdata['Close', 'VTHR'], 'VOO': dfdata['Close', 'VOO'], 'VOOG': dfdata['Close', 'VOOG'], 'VOOV': dfdata['Close', 'VOOV'], 'VTI': dfdata['Close', 'VTI'], 'VTV': dfdata['Close', 'VTV'],'VXF': dfdata['Close', 'VXF'],'VO': dfdata['Close', 'VO'],'VOT': dfdata['Close', 'VOT'],'VOE': dfdata['Close', 'VOE'],'IVOO': dfdata['Close', 'IVOO'],'IVOG': dfdata['Close', 'IVOG'],'IVOV': dfdata['Close', 'IVOV'],'VTWO': dfdata['Close', 'VTWO'],'VTWG': dfdata['Close', 'VTWG'],'VTWV': dfdata['Close', 'VTWV'],'VIOO': dfdata['Close', 'VIOO'],'VIOG': dfdata['Close', 'VIOG'],'VIOV': dfdata['Close', 'VIOV'],'VB': dfdata['Close', 'VB'],'VBK': dfdata['Close', 'VBK'],'VBR': dfdata['Close', 'VBR'], 'BNDW': dfdata['Close', 'BNDW'], 'BNDX': dfdata['Close', 'BNDX'], 'VWOB': dfdata['Close', 'VWOB'],'VSGX': dfdata['Close', 'VSGX'], 'VEU': dfdata['Close', 'VEU'], 'VSS': dfdata['Close', 'VSS'], 'VEA': dfdata['Close', 'VEA'], 'VGK': dfdata['Close', 'VGK'], 'VPL': dfdata['Close', 'VPL'], 'VNQI': dfdata['Close', 'VNQI'], 'VIGI': dfdata['Close', 'VIGI'], 'VYMI': dfdata['Close', 'VYMI'], 'VXUS': dfdata['Close', 'VXUS'], 'VWO': dfdata['Close', 'VWO'],'VOX': dfdata['Close', 'VOX'], 'VCR': dfdata['Close', 'VCR'], 'VDC': dfdata['Close', 'VDC'], 'VDE': dfdata['Close', 'VDE'], 'VFH': dfdata['Close', 'VFH'], 'VHT': dfdata['Close', 'VHT'], 'VIS': dfdata['Close', 'VIS'], 'VGT': dfdata['Close', 'VGT'], 'VAW': dfdata['Close', 'VAW'], 'VNQ': dfdata['Close', 'VNQ'], 'VPU': dfdata['Close', 'VPU']}

dfTOTALETF2 = pd.DataFrame(data=TOTALETF2)

normalized_dfTOTALETF2=(dfTOTALETF2)/(dfTOTALETF2.max())

#total
df=normalized_dfTOTALETF2

#figures for 1 Mo


figure3=df.corr(method='spearman').iplot(asFigure=True,kind='heatmap',title="Spearman Total Vanguard ETFs 1Mo",  filename='SpearmanTotal Vanguard ETFs 1Mo', colorscale='spectral')

figure4=df.iplot(asFigure=True, title = "Stocks 1 Mo normalized", xTitle="Time", yTitle="Normalized Price")


#YTD
data = yf.download("EDV BIV VGIT BLV VGLT VMBS BSV VTIP VGSH BND VCIT VCLT VCSH VTC VTEB VIG ESGV VUG VYM VV MGC MGK MGV VONE VONG VONV VTHR VOO VOOG VOOV VTI VTV VXF VO VOT VOE IVOO IVOG IVOV VTWO VTWG VTWV VIOO VIOG VIOV VB VBK VBR BNDW BNDX VWOB VT VSGX VEU VSS VEA VGK VPL VNQI VIGI VYMI VXUS VWO VOX VCR VDC VDE VFH VHT VIS VGT VAW VNQ VPU", period = "YTD")

dfdata = pd.DataFrame(data=data)

#print(dfdata.columns)
#print(dfdata['Adj Close', 'BNDW'])


#print plots of different classes


#US bond ETFs

USbondETF = { 'EDV': dfdata['Close', 'EDV'], 'BIV': dfdata['Close', 'BIV'], 'VGIT': dfdata['Close', 'VGIT'], 'BLV': dfdata['Close', 'BLV'], 'VGLT': dfdata['Close', 'VGLT'], 'VMBS': dfdata['Close', 'VMBS'], 'BSV': dfdata['Close', 'BSV'], 'VTIP': dfdata['Close', 'VTIP'], 'VGSH': dfdata['Close', 'VGSH'], 'BND': dfdata['Close', 'BND'], 'VCIT': dfdata['Close', 'VCIT'], 'VCLT': dfdata['Close', 'VCLT'], 'VCSH': dfdata['Close', 'VCSH'], 'VTC': dfdata['Close', 'VTC'], 'VTEB': dfdata['Close', 'VTEB']}
dfUSbondETF = pd.DataFrame(data=USbondETF)

normalized_dfUSbondETF=(dfUSbondETF)/(dfUSbondETF.max())


#US stock ETFs

USstockETF = { 'VIG': dfdata['Close', 'VIG'], 'ESGV': dfdata['Close', 'ESGV'], 'VUG': dfdata['Close', 'VUG'], 'VYM': dfdata['Close', 'VYM'], 'VV': dfdata['Close', 'VV'], 'MGC': dfdata['Close', 'MGC'], 'MGK': dfdata['Close', 'MGK'], 'MGV': dfdata['Close', 'MGV'], 'VONE': dfdata['Close', 'VONE'], 'VONG': dfdata['Close', 'VONG'], 'VONV': dfdata['Close', 'VONV'], 'VTHR': dfdata['Close', 'VTHR'], 'VOO': dfdata['Close', 'VOO'], 'VOOG': dfdata['Close', 'VOOG'], 'VOOV': dfdata['Close', 'VOOV'], 'VTI': dfdata['Close', 'VTI'], 'VTV': dfdata['Close', 'VTV'],'VXF': dfdata['Close', 'VXF'],'VO': dfdata['Close', 'VO'],'VOT': dfdata['Close', 'VOT'],'VOE': dfdata['Close', 'VOE'],'IVOO': dfdata['Close', 'IVOO'],'IVOG': dfdata['Close', 'IVOG'],'IVOV': dfdata['Close', 'IVOV'],'VTWO': dfdata['Close', 'VTWO'],'VTWG': dfdata['Close', 'VTWG'],'VTWV': dfdata['Close', 'VTWV'],'VIOO': dfdata['Close', 'VIOO'],'VIOG': dfdata['Close', 'VIOG'],'VIOV': dfdata['Close', 'VIOV'],'VB': dfdata['Close', 'VB'],'VBK': dfdata['Close', 'VBK'],'VBR': dfdata['Close', 'VBR']}
dfUSstockETF = pd.DataFrame(data=USstockETF)

normalized_dfUSstockETF=(dfUSstockETF)/(dfUSstockETF.max())


#International Bond ETF

INTbondETF = { 'BNDW': dfdata['Close', 'BNDW'], 'BNDX': dfdata['Close', 'BNDX'], 'VWOB': dfdata['Close', 'VWOB']}
dfINTbondETF = pd.DataFrame(data=INTbondETF)

normalized_dfINTbondETF=(dfINTbondETF)/(dfINTbondETF.max())



#INT stock ETFs

INTstockETF = { 'VSGX': dfdata['Close', 'VSGX'], 'VEU': dfdata['Close', 'VEU'], 'VSS': dfdata['Close', 'VSS'], 'VEA': dfdata['Close', 'VEA'], 'VGK': dfdata['Close', 'VGK'], 'VPL': dfdata['Close', 'VPL'], 'VNQI': dfdata['Close', 'VNQI'], 'VIGI': dfdata['Close', 'VIGI'], 'VYMI': dfdata['Close', 'VYMI'], 'VXUS': dfdata['Close', 'VXUS'], 'VWO': dfdata['Close', 'VWO']}
dfINTstockETF = pd.DataFrame(data=INTstockETF)

normalized_dfINTstockETF=(dfINTstockETF)/(dfINTstockETF.max())


#US stock Sector ETFs

USstocksectorETF = { 'VOX': dfdata['Close', 'VOX'], 'VCR': dfdata['Close', 'VCR'], 'VDC': dfdata['Close', 'VDC'], 'VDE': dfdata['Close', 'VDE'], 'VFH': dfdata['Close', 'VFH'], 'VHT': dfdata['Close', 'VHT'], 'VIS': dfdata['Close', 'VIS'], 'VGT': dfdata['Close', 'VGT'], 'VAW': dfdata['Close', 'VAW'], 'VNQ': dfdata['Close', 'VNQ'], 'VPU': dfdata['Close', 'VPU']}
dfUSstocksectorETF = pd.DataFrame(data=USstocksectorETF)

normalized_dfUSstocksectorETF=(dfUSstocksectorETF)/(dfUSstocksectorETF.max())



#Total Vanguard ETFs

TOTALETF=pd.concat([dfUSbondETF, dfUSbondETF, dfINTstockETF, dfINTbondETF, dfUSstocksectorETF], axis=1)

#USbondETF+USstockETF+INTbondETF+INTstockETF+USstocksectorETF

dfTOTALETF = pd.DataFrame(data=TOTALETF)

normalized_dfTOTALETF=(dfTOTALETF)/(dfTOTALETF.max())

#Total Vanguard ETFs2


TOTALETF2={'EDV': dfdata['Close', 'EDV'], 'BIV': dfdata['Close', 'BIV'], 'VGIT': dfdata['Close', 'VGIT'], 'BLV': dfdata['Close', 'BLV'], 'VGLT': dfdata['Close', 'VGLT'], 'VMBS': dfdata['Close', 'VMBS'], 'BSV': dfdata['Close', 'BSV'], 'VTIP': dfdata['Close', 'VTIP'], 'VGSH': dfdata['Close', 'VGSH'], 'BND': dfdata['Close', 'BND'], 'VCIT': dfdata['Close', 'VCIT'], 'VCLT': dfdata['Close', 'VCLT'], 'VCSH': dfdata['Close', 'VCSH'], 'VTC': dfdata['Close', 'VTC'], 'VTEB': dfdata['Close', 'VTEB'], 'VIG': dfdata['Close', 'VIG'], 'ESGV': dfdata['Close', 'ESGV'], 'VUG': dfdata['Close', 'VUG'], 'VYM': dfdata['Close', 'VYM'], 'VV': dfdata['Close', 'VV'], 'MGC': dfdata['Close', 'MGC'], 'MGK': dfdata['Close', 'MGK'], 'MGV': dfdata['Close', 'MGV'], 'VONE': dfdata['Close', 'VONE'], 'VONG': dfdata['Close', 'VONG'], 'VONV': dfdata['Close', 'VONV'], 'VTHR': dfdata['Close', 'VTHR'], 'VOO': dfdata['Close', 'VOO'], 'VOOG': dfdata['Close', 'VOOG'], 'VOOV': dfdata['Close', 'VOOV'], 'VTI': dfdata['Close', 'VTI'], 'VTV': dfdata['Close', 'VTV'],'VXF': dfdata['Close', 'VXF'],'VO': dfdata['Close', 'VO'],'VOT': dfdata['Close', 'VOT'],'VOE': dfdata['Close', 'VOE'],'IVOO': dfdata['Close', 'IVOO'],'IVOG': dfdata['Close', 'IVOG'],'IVOV': dfdata['Close', 'IVOV'],'VTWO': dfdata['Close', 'VTWO'],'VTWG': dfdata['Close', 'VTWG'],'VTWV': dfdata['Close', 'VTWV'],'VIOO': dfdata['Close', 'VIOO'],'VIOG': dfdata['Close', 'VIOG'],'VIOV': dfdata['Close', 'VIOV'],'VB': dfdata['Close', 'VB'],'VBK': dfdata['Close', 'VBK'],'VBR': dfdata['Close', 'VBR'], 'BNDW': dfdata['Close', 'BNDW'], 'BNDX': dfdata['Close', 'BNDX'], 'VWOB': dfdata['Close', 'VWOB'],'VSGX': dfdata['Close', 'VSGX'], 'VEU': dfdata['Close', 'VEU'], 'VSS': dfdata['Close', 'VSS'], 'VEA': dfdata['Close', 'VEA'], 'VGK': dfdata['Close', 'VGK'], 'VPL': dfdata['Close', 'VPL'], 'VNQI': dfdata['Close', 'VNQI'], 'VIGI': dfdata['Close', 'VIGI'], 'VYMI': dfdata['Close', 'VYMI'], 'VXUS': dfdata['Close', 'VXUS'], 'VWO': dfdata['Close', 'VWO'],'VOX': dfdata['Close', 'VOX'], 'VCR': dfdata['Close', 'VCR'], 'VDC': dfdata['Close', 'VDC'], 'VDE': dfdata['Close', 'VDE'], 'VFH': dfdata['Close', 'VFH'], 'VHT': dfdata['Close', 'VHT'], 'VIS': dfdata['Close', 'VIS'], 'VGT': dfdata['Close', 'VGT'], 'VAW': dfdata['Close', 'VAW'], 'VNQ': dfdata['Close', 'VNQ'], 'VPU': dfdata['Close', 'VPU']}

dfTOTALETF2 = pd.DataFrame(data=TOTALETF2)

normalized_dfTOTALETF2=(dfTOTALETF2)/(dfTOTALETF2.max())

#total
df=normalized_dfTOTALETF2

#figures for 1 Mo


figure5=df.corr(method='spearman').iplot(asFigure=True,kind='heatmap',title="Spearman Total Vanguard ETFs YTD",  filename='SpearmanTotal Vanguard ETFs YTD', colorscale='spectral')

figure6=df.iplot(asFigure=True, title = "Stocks YTD normalized", xTitle="Time", yTitle="Normalized Price")


import os
import dash
import dash_core_components as dcc
import dash_html_components as html

colors = {
    'background': '#000099',
    'text': '#000099'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H1(
        children='Stock Dashboard 0.1 by Andrew Rollin Davis, MD',
        style={
            'textAlign': 'center',
            'color': colors['text']
            }
        ),
        
        html.Div([
       
            html.Div([
                html.H3('1 Day all Vanguard Stocks Normalized'),
                dcc.Graph(id='g1', figure=figure1)
            ], style={'vertical-align': 'middle', 'width':'100%'}),

        ], className="row"),
        
         html.Div([
        
             html.Div([
                 html.H3('1 Day all Vanguard Stocks Normalized Corrrelations'),
                 dcc.Graph(id='g2', figure=figure2)
             ], className="six columns", style={'vertical-align': 'middle', 'width':'100%'}),

         ], className="row"),
         
         html.Div([
                
                     html.Div([
                         html.H3('1 Month all Vanguard Stocks Normalized '),
                         dcc.Graph(id='g3', figure=figure4)
                     ], className="six columns", style={'vertical-align': 'middle', 'width':'100%'}),

                 ], className="row"),
                 
        html.Div([
               
                    html.Div([
                        html.H3('1 Month all Vanguard Stocks Normalized Corrrelations'),
                        dcc.Graph(id='g4', figure=figure3)
                    ], className="six columns", style={'vertical-align': 'middle', 'width':'100%'}),

                ], className="row"),
                
        html.Div([
                        
                             html.Div([
                                 html.H3('YTD all Vanguard Stocks Normalized '),
                                 dcc.Graph(id='g5', figure=figure6)
                             ], className="six columns", style={'vertical-align': 'middle', 'width':'100%'}),

                         ], className="row"),
                         
        html.Div([
                       
                            html.Div([
                                html.H3('YTD all Vanguard Stocks Normalized Corrrelations'),
                                dcc.Graph(id='g6', figure=figure5)
                            ], className="six columns", style={'vertical-align': 'middle', 'width':'100%'}),

                        ], className="row"),
        
        
        
        
    
])


if __name__ == '__main__':
    app.run_server(debug=True)

