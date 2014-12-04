	
		

		function createEditor(newEditor, editorID, html) {
			if ( newEditor)
				return;

			// Create a new editor inside the <div id="editor">, setting its value to html
			var config = {};
			//alert("HTML: " + html);
			alert(editorID)
			newEditor = CKEDITOR.replace(editorID, config, html);
	
			newEditor.setData(html);
			//alert("successfully created new editor");
			return newEditor;
		}

		function removeEditor(newEditor, editorID, ID, path) {
			
			if ( !newEditor )
				return;

			// Retrieve the editor contents. In an Ajax application, this data would be
			// sent to the server or used in any other way.
			document.getElementById(editorID).innerHTML = html = newEditor.getData();
			//document.getElementById(contentsID).style.display = '';
			//save the data when removing the editor
			
			//need to have the id of the editor and the data as json
				 var jsonArray  = {};
				 var id = "ID";
				 var data = "DATA";
				 jsonArray[id] = ID;
				 jsonArray[data] = newEditor.getSnapshot();
				 var json = JSON.stringify(jsonArray);
				
				 json = "["+json+"]";
				 alert(json);
			
				
			
					
					var data = newEditor.getSnapshot()
							$.ajax({
							 type: 'POST',
							 url:path,
							 data: json,
							 dataType: 'json',
							 contentType:'application/json; charset=utf-8',
							 success: function(response) {
								alert("Success" + response)
								//alert('redirecting...');
								window.location('/'+path)
							 },error: function(response){
								alert("Error with ck editor post" + response);
							 
							}
				
				
						});

			
			
			
			
			// Destroy the editor.
			newEditor.destroy();
			newEditor = null;
			return newEditor;
		}

	
		// Uncomment the following code to test the "Timeout Loading Method".
		// CKEDITOR.loadFullCoreTimeout = 5;

		window.onload = function() {
			// Listen to the double click event.
			if ( window.addEventListener )
				document.body.addEventListener( 'dblclick', onDoubleClick, false );
			else if ( window.attachEvent )
				document.body.attachEvent( 'ondblclick', onDoubleClick );

		};

		function onDoubleClick( ev ) {
			// Get the element which fired the event. This is not necessarily the
			// element to which the event has been attached.
			var element = ev.target || ev.srcElement;

			// Find out the div that holds this element.
			var name;

			do {
				element = element.parentNode;
			}
			while ( element && ( name = element.nodeName.toLowerCase() ) &&
				( name != 'div' || element.className.indexOf( 'editable' ) == -1 ) && name != 'body' );

			if ( name == 'div' && element.className.indexOf( 'editable' ) != -1 )
				replaceDiv( element );
		}

		var editor;

		function replaceDiv( div ) {
			if ( editor )
				editor.destroy();
				
				

			editor = CKEDITOR.replace( div );
		}
		
		
		
		function getMyInstances(){
				var myinstances = [];

				//this is the foreach loop
				for(var i in CKEDITOR.instances) {

				   /* this  returns each instance as object try it with alert(CKEDITOR.instances[i]) */
					CKEDITOR.instances[i]; 
				    alert(CKEDITOR.instances[i])
					/* this returns the names of the textareas/id of the instances. */
					CKEDITOR.instances[i].name;
					alert("Name: " + CKEDITOR.instances[i].name);
					/* returns the initial value of the textarea */
					CKEDITOR.instances[i].value;  
					alert("Value: " + CKEDITOR.instances[i].value);
				   /* this updates the value of the textarea from the CK instances.. */
				   CKEDITOR.instances[i].updateElement();

				   /* this retrieve the data of each instances and store it into an associative array with
					   the names of the textareas as keys... */
				   myinstances[CKEDITOR.instances[i].name] = CKEDITOR.instances[i].getData(); 

				}
				return myinstances;
				
			}
	
			$(document).ready(function() {
			
			
				var newEditor = null
				var html = '';
				
				$("#createEditor1").on("click",  function (event) {
						alert("creating editor1")
						html = $("#editorcontents1").html()
						//alert("html: " + html);
						newEditor = createEditor(newEditor,'editor1', html);
				});
				
				$("#removeEditor1").on("click",  function (event) {
						//sets the newEditor to null
						newEditor = removeEditor(newEditor, 'editorcontents1', 'contents1');
						
				});
				
				var newEditor2 = null;
				$("#createEditor2").on("click",  function (event) {
						alert("creating editor2")
						html = $("#editorcontents2").html()
						//alert("html: " + html);
						newEditor2 = createEditor(newEditor2,'editor2', html);
				});
				
				$("#removeEditor2").on("click",  function (event) {
						//sets the newEditor to null
						//pass in the editor, two divs
						newEditor2 = removeEditor(newEditor2, 'editorcontents2', 'contents2');
						
				});
				
				
				/*Resources CK Editor buttons*/
				$(".createResourceEditor").on("click",  function (event) {
						//need to have 'editor-' to prepend to the id
						var editorID = 'editor-'+$(this).parent().parent().attr("id");
						//alert("EDITOR ID: " + editorID);
						html = $("#"+editorID).html()
						
						newEditor = createEditor(newEditor,editorID, html);
				});
				
				$(".removeResourceEditor").on("click",  function (event) {
						
						//sets the newEditor to null
						//get parent 
						//need to have 'editor-' to prepend to the id
						var editorID = 'editor-'+$(this).parent().parent().attr("id");
						var id = $(this).parent().parent().attr("id")
						//alert("EDITOR ID: " + editorID);
						newEditor = removeEditor(newEditor, editorID, id, '/resources');
						
				});
				
				
				/*Lessons*/
			/*
				$(".createLessonEditor").on("click",  function (event) {
						//need to have 'editor-' to prepend to the id
						var editorID = 'editor-'+$(this).parent().parent().attr("id");
						//alert("EDITOR ID: " + editorID);
						html = $("#"+editorID).html()
						
						newEditor = createEditor(newEditor,editorID, html);
				});
				
				$(".removeLessonEditor").on("click",  function (event) {
						
						//sets the newEditor to null
						//get parent 
						//need to have 'editor-' to prepend to the id
						var editorID = 'editor-'+$(this).parent().attr("id");
						var id = $(this).parent().attr("id");
						alert("EDITOR ID: " + editorID);
						newEditor = removeEditor(newEditor, editorID, id, '/adminLessons');
						
				});
				
				
				
				
				/*
					var myinstances = getMyInstances();
					
					event.preventDefault();
					//get the editor for the saving
					
					
					alert("EDITOR CREATE: " + editor.getSnapshot());
					var data = CKEDITOR.instances.editor.getSnapshot()
							$.ajax({
							 type: 'POST',
							 url:'/ckeditor',
							 data: data,
							
							 success: function(response) {
								alert("Success" + response)
								//alert('redirecting...');
								
							 },error: function(response){
								alert("Error with ck editor post" + response);
							 
							}
				
				
						});
						return false;	
				
				});
				
				*/
			});
		