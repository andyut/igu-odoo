    <head>
    <link rel="stylesheet" href="http://cdn.webix.com/edge/webix.css" type="text/css">
    <script src="http://cdn.webix.com/edge/webix.js" type="text/javascript"></script>
    </head>
    <body>test<div id="areaA"></div>
        <script type="text/javascript" charset="utf-8">
		var form1 = [
			{ view:"text", value:"dummy@email.com", label:"Email" },
			{ view:"text", type:"password", value:"123", label:"Password"},
            { view:"button", value:"Login" , type:"form" },
            { view:"button", value:"Cancel" }
		    ];
		webix.ui({
			container:"areaA",
			cols:[
				{ rows:[
					{ view:"form", scroll:false,elements: form1 },
				]}
			]
		    });
            </script>
            </body>