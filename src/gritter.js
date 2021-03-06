/**
 * Gritter
 * @namespace
 */
gisportal.gritter = {};
gisportal.gritter._notifications = [];

// The unique id of the last tutorial message
gisportal.gritter.tutUID = null;

/**
 * Setup the options for the gritter and create opening
 * welcome message.
 */
gisportal.gritter.setup = function() {
   $.extend($.gritter.options, { 
      position: 'bottom-right',
      fade_in_speed: 'medium',
      fade_out_speed: 800,
      time: 6000
   });
   
   // Create the help messages to be used by the gritter
   createHelpMessages();
   
   // Set and display the welcome message
   createWelcomeMessage();
   
   gisportal.gritter.gritterLayerHelper();
};

/**
 * Adds a type of notification
 * 
 * @param {string} id - The identifier of the message
 * @param {Object} params - The makeup of the message
 */
gisportal.gritter.addNotification = function(id, params) {
   gisportal.gritter._notifications[id] = params;
};

/**
 * Shows a gritter message with the message details provided.
 * 
 * @param {string} nN - The identifier for the notification name.
 * @param {Object} data - Any data needed for the message.
 * 
 * @return {number} Returns the unique ID of the message created. 
 */
gisportal.gritter.showNotification = function(nN, data) {
   var uid;
   
   var message = gisportal.gritter._notifications[nN];
   // Check for a title
   if(typeof message.title === 'undefined')
      message.title = function() {
         return 'Sorry, No Help Message Found';
      };
   // Check for some text
   if(typeof message.text === 'undefined')
      message.text = function() {
         return 'Sorry, we could not find a help message for your problem. Please refer to any help documentation you have.'; 
      };
   // Check for an afterOpen method
   if(typeof message.afterOpen === 'undefined')
      message.afterOpen = function() {};
      
   if(typeof message.max === 'undefined')
      message.max = 1;

   // Add the gritter message
   uid = $.gritter.add({
      title: message.title(data),
      text: message.text(data),
      after_open: function() {
         message.afterOpen(data);
      },
      //image: 'img/OpEc_small.png',
      class_name: 'gritter-light',
      sticky: true, 
      group: nN,
      max: message.max
   });
   
   return uid;  
};

/**
 * Hides a notification based of the information provided. A uid
 * can be provided to hide a single message. A notification type 
 * can be provided to hide all messages of a certain type.
 * 
 * @param {Object} params - params for the notification to hide.
 * @param {string} [params.uid] - unique identifier of the notification to hide.
 * @param {string} [params.type] - The type of the notification to hide.
 */
gisportal.gritter.hideNotification = function(params) {  
   if(typeof params.uid !== 'undefined') {
      $.gritter.remove(params.uid, {
         fade: false,
         speed: 'fast'
      });  
   }
   
   if(typeof params.type !== 'undefined') {
      // TODO: remove all notifications of a type.
   }
};

/**
 * Create the opening message that the user will see.
 */
function createWelcomeMessage()
{
   //gisportal.gritter.tutUID = gisportal.gritter.showNotification('welcomeTutorial', null);
}

/**
 * Displays errors as gritter messages.
 * 
 * @param {Object} data - Data object containing info regarding the error
 * @param {Object} [data.layer] - The OpenLayers.Layer object, can be null.
 * @param {string} data.type - A short string describing the object that has error'd.
 * @param {Object} data.request - The request object generated by the error.
 * @param {Object} data.errorType - The errorType object generated by the error.
 * @param {Object} data.exception - The exception object generated by the error.
 */
function gritterErrorHandler(data)
{  
   if(data.request.status == 400) {
      gisportal.gritter.showNotification('error400', data);
      return;
   }
   else if (data.request.status == 500) {
      gisportal.gritter.showNotification('error500', data);
      return;
   }
   else if (data.request.status == 502) {
      gisportal.gritter.showNotification('error502');
      return;
   }
   else if (data.errorType == 'parsererror') {
      gisportal.gritter.showNotification('errorParserError', data);
      return;
   }
     
   if(data.layer) {
      $.gritter.add({
         title: data.errorType.toUpperCase() + ': ' + data.request.status + ' (' + data.exception + ')',
         text: 'Could not get the ' + data.type + ' from the server for ' + data.layer.name + '. Try refreshing the page',
         //image: 'img/OpEc_small.png',
         class_name: 'gritter-light',
         sticky: true
      });
   }
   else {
      $.gritter.add({
         title: data.errorType.toUpperCase() + ': ' + data.request.status + ' (' + data.exception + ')',
         text: 'Could not get the ' + data.type + ' from the server. Try refreshing the page',
         //image: 'img/OpEc_small.png',
         class_name: 'gritter-light',
         sticky: true
      });
   }
}

/**
 * A logic function that tries to diagnose any problems 
 * with layers and show the correct help message.
 */ 
gisportal.gritter.gritterLayerHelper = function() {
   $(document).on('click', 'img[src="img/exclamation_small.png"]', function() {
      var layerID = $(this).parent().parent().attr('id');
      var layer = gisportal.getLayerByID(layerID);
      var helpMessage = 'none';
      
      // Is the layer temporal?
      if(layer.temporal) {     
         var inst = $('#viewDate').datepicker('getDate'); // Get the selected date
        
         // If the date is set...
         if(inst !== null) { 
            var thedate = new Date(inst.selectedYear, inst.selectedMonth, inst.selectedDay);
            var uidate = gisportal.utils.ISODateString(thedate);
            var mDate = layer.matchDate(uidate);

            // Can the layer display the selected date?
            if(mDate === null) {
               helpMessage = 'dateNotInRange';
            }
         }
         // If the date is not set...
         else if(inst === null) {
            helpMessage = 'noDate';
         }
      }

      var data = { layer: layer };
      gisportal.gritter.showNotification(helpMessage, data);

      return false;
   });
};

/**
 * Creates all the help messages to be used.
 */
function createHelpMessages()
{
   // Opening welcome message
   gisportal.gritter._notifications['welcomeTutorial'] = {
      title: function() {
         return 'Welcome to the Opec Portal';
      },
      text: function(layer) { 
         return '<p>It\'s great to have you here! First thing you need to do is decide which layers you want to use. You can do that from the ' +
         '<a id="wtHelp-layerSelectionPanel" href="#">layer selection panel</a>.</p><br>' +
         ' <p>If you have any trouble, you can always just hit the ' + 
         '<a id="wtHelp-questionMark" href="#">question mark</a>' + 
         ' at the top of most windows.</p><br>' +
         '<p>When you are ready for the next step just click ' +
         '<a id="wtHelp-next" href="#">next</a>.</p>';    
      },
      afterOpen: function(layer) {       
         $('#wtHelp-layerSelectionPanel').click(function(e) {
            if($('#gisportal-layerSelection').extendedDialog('isOpen')) {
               $('#gisportal-layerSelection').parent('div').fadeTo('slow', 0.3, function() { $(this).fadeTo('slow', 1); });
            }
            else {
               $('#layerPreloader').fadeTo('slow', 0.3, function() { $(this).fadeTo('slow', 1); });
            }
            
            return false;
         });
         
         $('#wtHelp-questionMark').click(function(e) {
            $('.ui-dialog-titlebar-help:visible').effect("highlight", {}, 3000);  
            return false;
         });

         $('#wtHelp-next').click(function(e) {
            var params = {uid: gisportal.gritter.tutUID};
            gisportal.gritter.hideNotification(params);
            gisportal.gritter.tutUID = gisportal.gritter.showNotification('layerTutorial', null);

            return false;
         });
      },
      max: 1
   };
   
   // Layer panels
   gisportal.gritter._notifications['layerTutorial'] = {
      title: function() {
         return 'Viewing Layers';
      },
      text: function() {
         return '<p>To view the layers you just selected, you need to use the ' +
         '<a id="ltHelp-layersPanel" href="#">layers panel</a>.<p><br>' +
         '<p>If you want to see a layer displayed on the map you need to select it\'s checkbox ' +
         'and then select a date (We will cover dates next).<p><br><p>When you are done with a layer just uncheck it. ' +
         'You can also right click on layers for further options.<p><br><p>When you are ready for the next step just click ' +
         '<a id="wtHelp-next" href="#">next</a>.<p>';
      },
      afterOpen: function() {
         $('#ltHelp-layersPanel').click(function() {
            $('.triggerL').trigger('click');
            return false;
         });
         
         $('#wtHelp-next').click(function(e) {
            var params = {uid: gisportal.gritter.tutUID};
            gisportal.gritter.hideNotification(params);
            gisportal.gritter.tutUID = gisportal.gritter.showNotification('dateTutorial', null);

            return false;
         });
      },
      max: 1
   };
   
   // Date Tutorial
   gisportal.gritter._notifications['dateTutorial'] = {
      title: function() {
         return 'Selecting Dates';
      },
      text: function() {
         return 'To select a date to be used by temporal layers, click on the ' +
            '<a id="dtDatepickerBtn" href="#">datepicker</a>' +
            ' at the top of the screen. Then use the left and right arrows to ' +
            'change the month or use the dropdown boxes. You can also type a date into the textbox. ' +
            '<a id="dtNext" href="#">Next</a>.';
      },
      afterOpen: function() {
         $('#dtNext').click(function(e) {
            var params = {uid: gisportal.gritter.tutUID};
            gisportal.gritter.hideNotification(params);
            gisportal.gritter.tutUID = gisportal.gritter.showNotification('tbdTutorial', null);

            return false;
         });

         $('#dtDatepickerBtn').click(function() {
            $('#viewDate').datepicker("show").datepicker("show").effect("highlight", {}, 3000);
            return false;
         });
      },
      max: 1
   };

   // To be Continued
   gisportal.gritter._notifications['tbdTutorial'] = {
      title: function() {
         return 'To Be Continued';
      },
      text: function() {
         return 'Be sure to provide any feedback about these tutorials ' +
         '<a id="give-some-feedback" href="http://trac.marinegisportal.eu/wiki" target="_blank">here</a>. ' +
         'Are they useful? Easy to follow? Too long? Too short?';
      },
      max: 1
   };

   // No date selected on date picker
   gisportal.gritter._notifications['noDate'] = {
      title: function() {
         return 'You need to select a date';
      },
      text: function(data) { 
         return 'This layer is a temporal layer and requires a date to be selected. ' +
            'To select a date use the ' +
            '<a id="datepickerBtn" href="#">datepicker</a>' +
            ' at the top of the screen.';
      },
      afterOpen: function(data) {
         $('#datepickerBtn').click(function() {
            var date = $.datepicker.parseDate('dd-mm-yy', data.layer.lastDate);
            $('#viewDate').datepicker("option", "defaultDate", date).datepicker("show").effect("highlight", {}, 3000);
            return false;
         });
      },
      max: 1
   };

   // The selected date is not supported by this layer
   gisportal.gritter._notifications['dateNotInRange'] = {
      title: function() {
         return 'Select another date';
      },
      text: function(data) {
         return 'The date you have selected is not avaliable for this layer. ' +
            'This layer supports dates between ' +
            data.layer.firstDate + ' and ' + data.layer.lastDate + '.' +
            ' Try selecting another date that all layers share.';
      },
      max: 3
   };
   
   // Layer Selector Tutorial
   gisportal.gritter._notifications['layerSelector'] = {
      title: function() {
         return 'Layer Selection Tutorial';
      },
      text: function() {
         return 'The layer selector is made up of two parts. The ' +
            '<a id="help-availableLayers" href="#">available layers</a>' +
            ' panel and the ' +
            '<a id="help-tag-menu" href="#">tag menu</a>' +        
            ' which can be used to limit or filter the avaliable layers. To select a layer, you can click the plus sign at the ' +
            'end of a layer. ' +
            'To deselect a layer you can click the minus sign at the end of ' +
            'the layer.';
      },
      afterOpen: function(data) {
         $('#help-availableLayers').click(function() {
            $('#gisportal-layerSelection .gisportal-selectable').fadeTo('slow', 0.3, function() { $(this).fadeTo('slow', 1); });
            return false;
         });
         
         $('#help-tag-menu').click(function() {
            $('#layerPreloader').fadeTo('slow', 0.3, function() { 
               $(this).fadeTo('slow', 1).fadeTo('slow', 0.3, function() { 
                  $(this).fadeTo('slow', 1); 
               }); 
            });
            return false;
         });
      },
      max: 1
   };
  
   // History Tutorial
   gisportal.gritter._notifications['history'] = {
      title: function() {
         return 'History Tutorial';
      },
      text: function() {
         return 'The history window is a way of seeing your previous actions such as graphs and saved states.';
      }
   };
   
   // Graph Creator Tutorial
   gisportal.gritter._notifications['graphCreatorTutorial'] = {
      title: function() {
         return 'Lets Create A Graph!';
      },
      text: function() {
         return 'To create a graph we need three things. The wcs server ' +
         'to query (Base URL), the coverage to get and the type of graph ' +
         'we want to create. You can also provide a bbox and/or a time range. ' +
         'If you\'re creating a histogram you can also provide some bins, but ' +
         'if you don\'t some will be created for you.';
      },
      max: 1
   };
   
   // Scalebar Tutorial
   gisportal.gritter._notifications['scalebarTutorial'] = {
      title: function() {
         return 'Scalebar Tutorial';
      },
      text: function() {
        return 'The scalebar allows you to change the range of values used using ' +
        'the slider or if you prefer the min and max boxes. If you need to increase ' +
        'the range just enter a bigger number in any of the text boxes.';
      },
      max: 1
   };
   
   // Bounding box selection for graphs
   gisportal.gritter._notifications['bbox'] = {
      title: function(){
         return 'Select a bounding box';         
      },
      text: function(){
         return   'Now select a bouding box on the map using the '+
                  '<a id="rect-bbox" href="#">rectangular bounding box drawing tool</a>.';
      },
      afterOpen: function(data) {
         $('#rect-bbox').click(function() {
            $('#box').next().effect("highlight", {}, 3000);
            return false;
         });
      },
      max: 1
   };
   
   gisportal.gritter._notifications['badRequestHelp'] = {
      title: function() {
         return 'Dealing With Bad Requests';
      },
      text: function() {
         return 'Some things to try when dealing with bad requests:' + 
         '<ol>' +
            '<li>Check the parameters are valid. Layer, Type, etc..</li>' +
            '<li>Using a Bbox? Is it inside the area covered by the layer? Have you tried it in a different spot?</li>' + 
            '<li>Using a date? Is it correctly formated? Does the layer have data for that time?</li>' + 
            '<li>Is the baseURL the correct one for that layer?</li>' + 
            '<li>View the query yourself in a browser, it may have more information as to what is wrong.</li>' + 
         '</ol>';
      },
      max: 1
   };
   
   gisportal.gritter._notifications['3DTutorial'] = {
      title: function() {
         return 'Welcome to 3D mode!';
      },
      text: function() {
         return '<p>Things are a little different here. Left click and drag will rotate the planet. ' +
         'Right click and drag up or down will zoom in or out (You can use the mouse wheel too!). ' +
         'Middle click and drag will rotate the camera.</p>' +
         '<br> <p><a id="tDT-Not-Working" href="#">Not working?</a></p>';
      },
      afterOpen: function(data) {
         $('#tDT-Not-Working').click(function() {
            gisportal.gritter.showNotification('3DNotWorking', null);
            return false;
         });
      },
      max: 1
   };
   
   gisportal.gritter._notifications['3DNotWorking'] = {
      title: function() {
         return 'Try this...';
      },
      text: function() {
         return 'Check that your browser and hardware support webGL <a id="tDNW-webglCheck" href="http://get.webgl.org/" target="_blank">here</a> .';
      },
      max: 1
   };
   
   gisportal.gritter._notifications['error400'] = {
      title: function() {
         return 'Sorry what was that? Could you say that again?';         
      },
      text: function(data) {
         return 'We had a little trouble understanding what you wanted as not all of the data was provided. ' + 
         'You can view the request for yourself ' + 
         '<a id="url400" href="' + data.url + '" target="_blank">here</a>' + '. ' +
         'Make sure you have entered all the required parameters (layer and type of graph) ' +
         'and that each of them is valid before trying again. If you still have trouble it may be ' + 
         'that there is no data available for your selection. Do you need some further help? ' +
         '<a id="error400-next" href="#">Yes</a>';
      },
      afterOpen: function(data) {
         $('#error400-next').click(function(e) {
            gisportal.gritter.showNotification('badRequestHelp', null);
            return false;
         });
      },
      max: 1
   };
   
   gisportal.gritter._notifications['error500'] = {
      title: function() {
         return 'We\'re Sorry...Something Went Wrong';         
      },
      text: function(data) {
         return 'The server had some trouble while performing your query. You can view the query ' + 
         '<a id="url500" href="' + data.url + '" target="_blank">here</a>. ' + 
         'This is a server-side error meaning the problem is not with your computer or ' +
         'Internet connection, but with the server. We apologise for the inconvenience. ' +
         'While we fix this maybe you would like to try a different query?';
      },
      max: 1
   };
   
   gisportal.gritter._notifications['error502'] = {
      title: function() {
         return 'Well That Wasn\'t Supposed To Happen';
      },
      text: function(data) {
         return 'Sorry, looks like we had some trouble talking to one of our ' +
         'servers. It was a \"Bad Gateway\", if that means anything to anyone? ' +
         'This in most cases is a temporary error, so you can keep trying or come back and try later. ' +
         'The problem could be on your end, so you may need to contact your local administrator or if at home, ' +
         'just check that other sites work.'; 
      },
      max: 1
   };
   
   gisportal.gritter._notifications['errorParserError'] = {
      title: function() {
         return 'Parse Error: Unexpected character';         
      },
      text: function(data) {
         return 'An unexpected character was received from "' + 
         '<a id="urlParserError" href="' + data.url + '" target="_blank">this</a>' +
         '" address.';
      },
      max: 1
   };
   
   gisportal.gritter._notifications['dataNotSelected'] = {
      title: function() {
         return 'No Data Selected';         
      },
      text: function(data) {
         return 'Please make sure to select a layer from the dropdown list and then press the generate graph button again.';
      },
      max: 1
   };
   
   gisportal.gritter._notifications['graphError'] = {
      title: function() {
         return 'Sorry, we failed to create a graph';
      },
      text: function(data) {
         return 'The server informed us that it failed to make a graph for your selection with the message "' +
         data.error + '".';
      }
   };

   gisportal.gritter._notifications['graphData'] = {
      title: function() {
         return 'Sorry, that is too much data';
      },
      text: function(data) {
         return 'I\'m afraid we are not currently able to plot that amount of data on this type of graph.'
      }
   };
}
