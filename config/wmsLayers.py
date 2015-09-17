layers = [
{
    "name": "socio_test:south_west_wgs84",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "http://localhost:8080/geoserver/socio_test/wms?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/SST_RRC_8D?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "socio_test:south_west_wgs84": {
          "Confidence": "High",
            "Ecosystem_Element": "Scoio",
            "MSFD": [
               ""
            ],
            "interval": "",
            "niceName": "Social Deprivatin index",
            "region": "Cornwall"
         }
      }
   },{
      "name": "sstp",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/SST_RRC_8D?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/SST_RRC_8D?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "sstp": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "8 Day",
            "niceName": "Sea Surface Temperature - 8 day",
            "region": "Cornwall"
         }
      }
   },
   {
      "name": "sstp2",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/SST_RRA_8D?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/SST_RRA_8D?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "sstp": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "8 Day",
            "niceName": "Sea Surface Temperature - 8 day",
            "region": "Algarve"
         }
      }
   },
   {
      "name": "sstp3",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/SST_RRS_8D?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/SST_RRS_8D?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "sstp": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "8 Day",
            "niceName": "Sea Surface Temperature - 8 day",
            "region": "Scotland"
         }
      }
   },
   {
      "name": "sstp4",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/SST_RRI_8D?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/SST_RRI_8D?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "sstp": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "8 Day",
            "niceName": "Sea Surface Temperature - 8 day",
            "region": "Iberia"
         }
      }
   },
   {
      "name": "sstp5",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/SST_RRI_M?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/SST_RRI_M?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "sstp": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Sea Surface Temperature - Monthly",
            "region": "Iberia"
         }
      }
   },
   {
      "name": "sstp6",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/SST_RRA_M?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/SST_RRA_M?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "sstp": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Sea Surface Temperature - Monthly",
            "region": "Algarve"
         }
      }
   },
   {
      "name": "sstp7",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/SST_RRS_M?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/SST_RRS_M?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "sstp": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Sea Surface Temperature - Monthly",
            "region": "Scotland"
         }
      }
   },
   {
      "name": "sstp8",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/SST_RRC_M?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/SST_RRC_M?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "sstp": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Sea Surface Temperature - Monthly",
            "region": "Cornwall"
         }
      }
   },
   {
      "name": "meris-cornwall",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/MERIS_COMP_RRC?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/MERIS_COMP_RRC?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "adg_443_qaa": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "adg_443_qaa true",
            "region": "Cornwall"
         },
         "chl_oc5": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Chlorophyll-a concentration in sea water using the OC5 algorithm",
            "region": "Cornwall"
         },
         "chlor_a": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Case 1 surface layer chlorophyll-a concentration",
            "region": "Cornwall"
         },
         "Kd_490": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Mean Diffuse Attenuation Coefficient at 490nm",
            "region": "Cornwall"
         },
         "spmi": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Inorganic suspended particulate matter in sea water using the algorithm of Gohin (c.f. OC5).",
            "region": "Cornwall"
         }

      }
   },
   {
      "name": "meris-scotland",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/MERIS_COMP_RRS?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/MERIS_COMP_RRS?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "adg_443_qaa": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "adg_443_qaa true",
            "region": "Scotland"
         },
         "chl_oc5": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Chlorophyll-a concentration in sea water using the OC5 algorithm",
            "region": "Scotland"
         },
         "chlor_a": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Case 1 surface layer chlorophyll-a concentration",
            "region": "Scotland"
         },
         "Kd_490": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Mean Diffuse Attenuation Coefficient at 490nm",
            "region": "Scotland"
         },
         "spmi": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Inorganic suspended particulate matter in sea water using the algorithm of Gohin (c.f. OC5).",
            "region": "Scotland"
         }

      }
   },
   {
      "name": "meris-iberia",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/MERIS_COMP_RRI?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/MERIS_COMP_RRI?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "adg_443_qaa": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "adg_443_qaa true",
            "region": "Iberia"
         },
         "chl_oc5": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Chlorophyll-a concentration in sea water using the OC5 algorithm",
            "region": "Iberia"
         },
         "chlor_a": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Case 1 surface layer chlorophyll-a concentration",
            "region": "Iberia"
         },
         "Kd_490": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Mean Diffuse Attenuation Coefficient at 490nm",
            "region": "Iberia"
         },
         "spmi": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Inorganic suspended particulate matter in sea water using the algorithm of Gohin (c.f. OC5).",
            "region": "Iberia"
         }

      }
   },
   {
      "name": "meris-algarve",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/MERIS_COMP_RRA?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/MERIS_COMP_RRA?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "adg_443_qaa": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "adg_443_qaa true",
            "region": "Algarve"
         },
         "chl_oc5": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Chlorophyll-a concentration in sea water using the OC5 algorithm",
            "region": "Algarve"
         },
         "chlor_a": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Case 1 surface layer chlorophyll-a concentration",
            "region": "Algarve"
         },
         "Kd_490": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Mean Diffuse Attenuation Coefficient at 490nm",
            "region": "Algarve"
         },
         "spmi": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Monthly",
            "niceName": "Inorganic suspended particulate matter in sea water using the algorithm of Gohin (c.f. OC5).",
            "region": "Algarve"
         }

      }
   },
     {
      "name": "dhi",
      "options": {
         "providerShortTag": "DHI-GRAS"
      },
      "services": {
         "wms": {
            "url": "http://aquausers.dhi-gras.com/thredds/wms/GHRSST_L4_MUR?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "http://aquausers.dhi-gras.com/thredds/wcs/GHRSST_L4_MUR?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "analysed_sst": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "Temperature"
            ],
            "interval": "Daily",
            "niceName": "Sea Surface Temperature",
            "region": "Denmark"
         }
      }
   },
     {
      "name": "dhi-kd490",
      "options": {
         "providerShortTag": "DHI-GRAS"
      },
      "services": {
         "wms": {
            "url": "http://aquausers.dhi-gras.com/thredds/wms/GRAS_KD490?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "http://aquausers.dhi-gras.com/thredds/wcs/GRAS_KD490?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Kd_490": {
          "Confidence": "High",
            "Ecosystem_Element": "Physical",
            "MSFD": [
               "KD"
            ],
            "interval": "Daily",
            "niceName": "masked adjusted Kd490",
            "region": "Denmark"
         }
      }
   },
     {
      "name": "pseudo_cornwall_monthly",
      "options": {
         "providerShortTag": "PML"
      },
      "services": {
         "wms": {
            "url": "http://localhost:8080/thredds/wms/HAB_MONTHLY_C_pseudo?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "http://localhost:8080/thredds/wcs/HAB_MONTHLY_C_pseudo?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "harmful_un": {
          "Confidence": "High",
            "Ecosystem_Element": "Harmful Algal Bloom",
            "MSFD": [
               "KD"
            ],
            "interval": "Mnthly",
            "niceName": "Monthly HAB risk (pseudo) Cornwall",
            "region": "Cornwall"
         }
      }
   }
]
