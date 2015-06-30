/*------------------------------------*\
    Selection Tools
    This file is for selecting features
    on the map, such as rectangles etc.
    It is separate from indicatorsPanel
    to make the code more future-proof.
\*------------------------------------*/

/*
Things missing that ol3 doesn't do or I can't work out how to implement:
- mouseover delete button for polygons
- draw regular boxes
- edit the coordinates textbox to add/change the polygon
- specifying polygon height/width/area - seems to be massively out on the area calculation (ol2 seems to be out too incidentally)

*/

gisportal.selectionTools = {};

var draw;

gisportal.selectionTools.init = function()  {
   gisportal.selectionTools.initDOM();

   gisportal.vectorLayer = new ol.layer.Vector({
      source : new ol.source.Vector(),
         style : new ol.style.Style({
            fill : new ol.style.Fill({
            color : 'rgba(47, 163, 11, 0.2)'
         }),
         stroke : new ol.style.Stroke({
            color : '#ffffff',
            width : 2
         }),
         image : new ol.style.Circle({
            radius : 7,
            fill : new ol.style.Fill({
               color : '#ffffff'
            })
         })
      })
   });
   map.addLayer(gisportal.vectorLayer);

   var feature;
   map.on('pointermove', function(evt) {
      feature = null;
      var features = gisportal.vectorLayer.getSource().getFeaturesAtCoordinate(evt.coordinate);
      if (features.length) {
         feature = features[0];

      }
      //console.log('feature')
   });
   map.on('postrender', function(renderEvent) {
      if (feature) {
         console.log(feature)
         //renderEvent.vectorContext.renderFeature(feature, highlightStyle);
      }
   });

   gisportal.wkt = new ol.format.WKT();
};

function cancelDraw() {
   if(draw == null)return;
   
   map.removeInteraction(draw);
}

gisportal.selectionTools.initDOM = function()  {
   $('.js-indicators').on('change', '.js-coordinates', gisportal.selectionTools.updateROI);

   $('.js-indicators').on('click', '.js-draw-box', function()  {
      gisportal.selectionTools.toggleTool('Box');
   });
   $('.js-indicators').on('click', '.js-draw-polygon', function() {
      console.log('clicked th epolygon draw');
      gisportal.selectionTools.toggleTool('Polygon');
   });
   $('.js-indicators').on('click', '.js-draw-line', function() {
      console.log('clicked the line draw');
      gisportal.selectionTools.toggleTool('Line');
   });

   // TODO, perhaps...
   // // map image export - problems with cross origin tainting the canvas are preventing this from working. 
   // // With cross origin set to 'anonymous' it should work but the headers at rsg.pml.ac.uk then prevent the 
   // // country borders from loading
   // $('<button class="js-export-image" title="Download current view as image" download="map.png"><span class="icon-download-10"></span></button>').appendTo('.ol-full-screen');
   // $('.js-export-image').on('click', function(e) {
   //    map.once('postcompose', function(event) {
   //    var canvas = event.context.canvas;
   //       $('.js-export-image').href = canvas.toDataURL('image/png');
   //    });
   //    map.renderSync();
   // })

};

gisportal.selectionTools.toggleBboxDisplay = function() {

   $('.coordinates').disabled();



};

gisportal.selectionTools.getActiveControl = function() {
   activeControl = '';
   for (var key in gisportal.mapControls) {
      if (gisportal.mapControls[key].active) {
         activeControl = key;
      }
   }
   return activeControl;
};

gisportal.selectionTools.toggleTool = function(type)  {
   if (draw != null) {
      cancelDraw();
   }
   
   if (type != 'None') {
      if (type == "Polygon") {
         draw = new ol.interaction.Draw({
            source:gisportal.vectorLayer.getSource(),
            type: type
         });
         map.addInteraction(draw);
      }

      if (type == "Box") {
         draw = new ol.interaction.DrawBox({
            source:gisportal.vectorLayer.getSource(),
            type: type
         });
         map.addInteraction(draw);
      }
      
      draw.on('drawstart',
         function(evt) {
            gisportal.vectorLayer.getSource().clear();
            // set sketch
            sketch = evt.feature;
         }, this);

      draw.on('drawend',
         function(evt) {
            gisportal.selectionTools.ROIAdded(sketch);
            // unset sketch
            sketch = null;

         }, this);      
   }
   map.ROI_Type = type;

};

gisportal.selectionTools.updateROI = function()  {
   // this will all change with the pre-saved area selection options that are coming   
};

gisportal.currentSelectedRegion = "";
gisportal.selectionTools.ROIAdded = function(feature)  {
   var feature_type = map.ROI_Type;

   // Get the geometry of the drawn feature
   var geom = new ol.Feature();
   geom = feature.getGeometry();

   //var bounds;
   if (feature_type === "Polygon") {
      var wkt_feature = gisportal.wkt.writeGeometry(geom);
      
      wkt_feature = wkt_feature.replace(/[\d\.]+/g, function(num){
         return Math.round(num * 1000 ) / 1000;
      });

      gisportal.currentSelectedRegion = wkt_feature;
      $('.js-coordinates').val(wkt_feature);
      //$('.bbox-info').toggleClass('hidden', false);
      $('.js-edit-polygon').attr('disabled', false);
   }
   else if(feature_type === 'Line') {
      var wkt_feature = gisportal.wkt.writeGeometry(geom);
      
      wkt_feature = wkt_feature.replace(/[\d\.]+/g, function(num){
         return Math.round(num * 1000 ) / 1000;
      });

      gisportal.currentSelectedRegion = wkt_feature;
      $('.js-coordinates').val(wkt_feature);
      //$('.bbox-info').toggleClass('hidden', false);
      $('.js-edit-polygon').attr('disabled', false);
   } else {
      bounds = feature.getGeometry().getExtent();
      var coords = "";
      if (bounds) {
         coords += bounds[0] + ",";
         coords += bounds[1] + ",";
         coords += bounds[2] + ",";
         coords += bounds[3];
         
         coords = coords.replace(/[\d\.]+/g, function(num){
            return Math.round(num * 1000 ) / 1000;
         });
      
         gisportal.currentSelectedRegion = coords;
         $('.js-coordinates').val(coords);
         //$('.bbox-info').toggleClass('hidden', false);
         $('.js-edit-polygon').attr('disabled', false);
      }
   }
   this.toggleTool('None'); // So that people don't misclick

  
   
// TODO: The whole size and area calculation is a bit screwy and doesn't seem to give anything like
// accurate figures so it needs re-visiting at some point, or removing completely.

   // var area_deg, area_km, height_deg, width_deg, height_km, width_km, radius_deg, ctrLat, ctrLon = 0;

   // if(feature_type !== '' && feature_type != 'point' && bounds) {
   //    area_deg = geom.getArea();
   //    area_km = (geom.getGeodesicArea()*1e-6);
   //    height_deg = bounds.getHeight();
   //    width_deg = bounds.getWidth();
   //    // Note - to get values in true ellipsoidal distances, we need to use Vincenty functions for measuring ellipsoidal
   //    // distances instead of planar distances (http://www.movable-type.co.uk/scripts/latlong-vincenty.html)
   //    ctrLon = geom.getCentroid().x;
   //    ctrLat = geom.getCentroid().y;
   //    height_km = OpenLayers.Util.distVincenty(new OpenLayers.LonLat(ctrLon,bounds.top),new OpenLayers.LonLat(ctrLon,bounds.bottom));
   //    width_km = OpenLayers.Util.distVincenty(new OpenLayers.LonLat(bounds.left,ctrLat),new OpenLayers.LonLat(bounds.right,ctrLat));
   //    radius_deg = ((bounds.getWidth() + bounds.getHeight())/4);

   //    var pretty_height_km, pretty_width_km, pretty_area_km
   //    // because not all browsers support Intl.NumberFormat ...
   //    try {
   //       pretty_height_km = new Intl.NumberFormat("en-GB", { maximumFractionDigits: 2}).format(height_km);
   //    } catch(e) {
   //       pretty_height_km = height_km.toPrecision(4);
   //    }
   //    try {
   //       pretty_width_km = new Intl.NumberFormat("en-GB", { maximumFractionDigits: 2}).format(width_km);
   //    } catch(e) {
   //       pretty_width_km = width_km.toPrecision(4);
   //    }
   //    try {
   //       pretty_area_km = new Intl.NumberFormat("en-GB", { maximumFractionDigits: 0}).format(area_km);
   //    } catch(e) {
   //       pretty_area_km = area_km.toPrecision(4);
   //    }
      
   // }
  
   // switch(feature_type) {
   //    case 'box': 
   //       $('.js-bbox-width').html(pretty_width_km+' km');
   //       $('.js-bbox-height').html(pretty_height_km +' km');
   //       $('.js-bbox-area').html(pretty_area_km +' km<sup>2</sup>');
   //       break;
   //    case 'point':
   //       // set the .bbox-info div to show lat/long
   //       break;
   //    case 'circle':
   //       // set the .bbox-info div to show lat/long of the centre, the radius, width, height and area
   //       break;
   //    case 'polygon':
   //       // set the .bbox-info div to show the centroid lat/long and area
   //       $('.js-bbox-width').html('');
   //       $('.js-bbox-height').html('');
   //       $('.js-bbox-area').html(pretty_area_km + ' km<sup>2</sup>');
   //       break;
   // }
 
   this.setVectorLayerToTop();
};

gisportal.selectionTools.setVectorLayerToTop = function() {
   map.removeLayer(gisportal.vectorLayer);
   map.addLayer(gisportal.vectorLayer);
};
