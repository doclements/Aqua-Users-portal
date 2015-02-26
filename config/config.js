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
   browseCategories: {
      "Ecosystem_Element": "Ecosystem <br> Indicators",
      "region": "Regional <br> Seas",
      "MSFD": "EU MSFD <br> Descriptors"
   },
   paths: {
      graphServer: 'http://my-portal-aqua.co.uk:3001',
      middlewarePath: '/service'
   },
   countryBorder: {
      'defaultLayer': 'rsg:full_10m_borders', // (countries_all_white|countries_all_black|countries_all_blue)
      'alwaysVisible': true // (true|false)  > If true the defaultLayer will be visible at page load
   },
   // Should layers auto scale by default
   autoScale: true,

   requiresTermsAndCondictions: false,

   homepageSlides: [
      "img/homepage-slides/opec1.jpg",
      "img/homepage-slides/opec2.jpg",
      "img/homepage-slides/opec3.jpg",
      "img/homepage-slides/opec4.jpg",
      "img/homepage-slides/opec5.jpg",
      "img/homepage-slides/opec6.jpg",
      "img/homepage-slides/opec7.jpg"
   ]
};