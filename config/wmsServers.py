#!/usr/bin/env python

servers = {
   'cci': { 
      'name': 'cci',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/CCI-v1.0-D?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'providerShortTag': 'CCI'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/CCI-v1.0-D?'
   },
   'hcmr': { 
      'name': 'hcmr',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/HCMR-M-AGGSLOW?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'HCMR'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/HCMR-M-AGGSLOW?'
   },
   'pml_annual': { 
      'name': 'pml_annual',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/PML-Y-AGGSLOW?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'providerShortTag': 'PML'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/PML-Y-AGGSLOW?'
   },
   'pml_seasonal': { 
      'name': 'pml_seasonal',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/PML-S-AGGSLOW?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'providerShortTag': 'PML'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/PML-S-AGGSLOW?'
   },
   'pml_monthly': { 
      'name': 'pml_monthly',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/PML-M-AGGSLOW?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'providerShortTag': 'PML'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/PML-M-AGGSLOW?'
   },
   'pml_daily': { 
      'name': 'pml_daily',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/PML-D-AGGSLOW?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'providerShortTag': 'PML'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/PML-D-AGGSLOW?'
   },
   'imsmetu_annual': { 
      'name': 'imsmetu_annual',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/IMSMETU-Y/BIMS0.1_HC_IMSMETU_blacksea_19900101-20090101_ANNUAL.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'IMS-METU'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/IMSMETU-Y/BIMS0.1_HC_IMSMETU_blacksea_19900101-20090101_ANNUAL.nc?'
   },
   'cefas': { 
      'name': 'cefas',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/CEFAS/resoutcut.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'providerShortTag': 'Cefas'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/CEFAS/resoutcut.nc?'
   },
   'dmi_monthy': { 
      'name': 'dmi_monthly',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/DMI_M/DMI_1990_2009_monthly_mean.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'providerShortTag': 'DMI'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/DMI_M/DMI_1990_2009_monthly_mean.nc?'
   },
   'dmi_annual': { 
      'name': 'dmi_annual',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/DMI_Y/DMI_1990_2009_annual_mean.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'providerShortTag': 'DMI'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/DMI_Y/DMI_1990_2009_annual_mean.nc?'
   },
   'dmi_seasonal': { 
      'name': 'dmi_seasonal',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/DMI_S/DMI_1990_2009_seasonal_anomaly.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'providerShortTag': 'DMI'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/DMI_S/DMI_1990_2009_seasonal_anomaly.nc?'
   },
   'ogs_Ammonia': { 
      'name': 'ogs_Ammonia',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_ammonia.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_ammonia.nc?'
   },
   'ogs_CarnZoo': { 
      'name': 'ogs_CarnZoo',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_CarnMesozoo.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_CarnMesozoo.nc?'
   },
   'ogs_C-Diat': { 
      'name': 'ogs_C-Diat',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Cdia.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Cdia.nc?'
   },
   'ogs_Chl-Diat': { 
      'name': 'ogs_Chl-Diat',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_chl-dia.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_chl-dia.nc?'
   },
   'ogs_Chl-LargePhy': { 
      'name': 'ogs_Chl-LargePhy',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_chl-largephy.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_chl-largephy.nc?'
   },
   'ogs_Chl-Nflag': { 
      'name': 'ogs_Chl-Nflag',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_chl-nflag.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_chl-nflag.nc?'
   },
   'ogs_Chl-PicoPhy': { 
      'name': 'ogs_Chl-PicoPhy',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_chl-picophy.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_chl-picophy.nc?'
   },
   'ogs_C-LargePhy': { 
      'name': 'ogs_C-LargePhy',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Clargephy.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Clargephy.nc?'
   },
   'ogs_C-Nflag': { 
      'name': 'ogs_C-Nflag',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Cnflag.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Cnflag.nc?'
   },
   'ogs_C-PicoPhy': { 
      'name': 'ogs_C-PicoPhy',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Cpicophy.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Cpicophy.nc?'
   },
   'ogs_HeteroFlag': { 
      'name': 'ogs_HeteroFlag',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_HeteroFlag.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_HeteroFlag.nc?'
   },
   'ogs_MicroZoo': { 
      'name': 'ogs_MicroZoo',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Microzoo.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Microzoo.nc?'
   },
   'ogs_Nitrate': { 
      'name': 'ogs_Nitrate',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_nitrate.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_nitrate.nc?'
   },
   'ogs_OmniZoo': { 
      'name': 'ogs_OmniZoo',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_OmniMesozoo.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_OmniMesozoo.nc?'
   },
   'ogs_Oxygen': { 
      'name': 'ogs_Oxygen',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_oxygen.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_oxygen.nc?'
   },
   'ogs_pCO2': { 
      'name': 'ogs_pCO2',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_pCO.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_pCO.nc?'
   },
   'ogs_Phosphate': { 
      'name': 'ogs_Phosphate',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_phosphate.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_phosphate.nc?'
   },
   'ogs_NPP': { 
      'name': 'ogs_NPP',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_ppn.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_ppn.nc?'
   },
   'ogs_R_NO3NH4_PO4': { 
      'name': 'ogs_R_NO3NH4_PO4',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_R_NO3NH4_PO4.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_R_NO3NH4_PO4.nc?'
   },
   'ogs_R_NO3_PHOS': { 
      'name': 'ogs_R_NO3_PHOS',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_R_NO3_PO4.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_R_NO3_PO4.nc?'
   },
   'ogs_R_NO3_SIO4': { 
      'name': 'ogs_R_NO3_SIO4',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_R_NO3_SIO4.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_R_NO3_SIO4.nc?'
   },
   'ogs_sal': { 
      'name': 'ogs_sal',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_sal_Anomaly.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_sal_Anomaly.nc?'
   },
   'ogs_sal': { 
      'name': 'ogs_sal',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_sal.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_sal.nc?'
   },
   'ogs_Silicate': { 
      'name': 'ogs_Silicate',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_silicate.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_silicate.nc?'
   },
   'ogs_tem': { 
      'name': 'ogs_tem',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_tem_Anomaly.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_tem_Anomaly.nc?'
   },
   'ogs_temp': { 
      'name': 'ogs_temp',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_temp.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_temp.nc?'
   },
   'ogs_Totchl': { 
      'name': 'ogs_Totchl',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Totalchlorophyll.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Totalchlorophyll.nc?'
   },
   'ogs_TotphytoC': { 
      'name': 'ogs_TotphytoC',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_TotalPhytoC.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_TotalPhytoC.nc?'
   },
   'ogs_Totzoo': { 
      'name': 'ogs_Totzoo',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Totalzooplankton.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Totalzooplankton.nc?'
   },
   'ogs_Wmin_NO3': { 
      'name': 'ogs_Wmin_NO3',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Wmin_nitrate.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Wmin_nitrate.nc?'
   },
   'ogs_Wmin_PO4': { 
      'name': 'ogs_Wmin_PO4',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Wmin_phosphate.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Wmin_phosphate.nc?'
   },
   'ogs_Wmin_SiO2': { 
      'name': 'ogs_Wmin_SiO2',
      'url': 'http://earthserver.pml.ac.uk/thredds/wms/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Wmin_silicate.nc?',
      'params': {
         'SERVICE': 'WMS',
         'request': 'GetCapabilities',
         'version': '1.3.0'
      },
      'options': {
         'positive': 'down',
         'providerShortTag': 'OGS'
      },
      'wcsurl': 'http://earthserver.pml.ac.uk/thredds/wcs/OGS/OPATMBFM3_OGS_HC_Med_19990101_20111231_Wmin_silicate.nc?'
   }
}
