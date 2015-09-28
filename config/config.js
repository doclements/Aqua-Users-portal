/*------------------------------------*\
   Configuration
   This file is for the configuration
   of the GIS Portal.

   browseCategories - Used to define
   which categories to be shown in the
   browse panel. This is currently
   limited to 2.
\*------------------------------------*/


gisportal.config = {
   siteMode: "development", //(development|production)
   browseCategories : {
      "Ecosystem_Element" : "Ecosystem",
      "region": "Region",
      "MSFD" : "EU MSFD"
   },
   browseMode : 'selectlist',                       // (tabs|selectlist) tabs (default) = original method of 3 tabs; selectlist = makes all available categories selectable from a drop down list
   defaultCategory: '',                     // only used when browseMode = selectlist; any key value from browseCategories
   autoScale: true,
   paths: {
    graphServer: '/plotting',
    middlewarePath: '/service'
   },
   popularIndicators : [
      "Heterotrophic flagellates biomass", "Net Primary Production", "Oxygen", "Temperature"
   ],
   defaultStates: [
     
   ],
};
