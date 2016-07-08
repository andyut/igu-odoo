<html>
	<head>
		<link rel="stylesheet" href="//cdn.webix.com/site/webix.css" type="text/css" media="screen" charset="utf-8">
		<script src="//cdn.webix.com/site/webix.js?" type="text/javascript" charset="utf-8"></script>
		<style>
			#areaA, #areaB{
				margin: 50px;
				width:700px; height:100px;
			}
            .blue.webix_menu-x{
                background:#3498DB;
            }
		</style>
		<title>Menu in Toolbar</title>
	</head>
	<body>
<script type="text/javascript" charset="utf-8">
	var menu_data = [
		{ id:"1",value:"Translate...", submenu:[
			"English",
			{ value:"Slavic...", submenu:[
				"Belarusian", "Russian", "Ukrainian"
			]},
			"German"
		]},
		{ id:"2",value:"Post...", submenu:[ "Facebook", "Google+", "Twitter" ]},
		{ id:"3",value:"Info" }
	];
	var menu = {
		view:"menu",
		data: menu_data,
        css:"blue"
	};
	var toolbar = {
		view:"toolbar", paddingY:0,  elements:[
			{},
			{ view:"text" },
			{ view:"button", label:"Search", width:100 }
		]
	};


	webix.ui({
		rows:[
			{ type:"clean", cols:[ menu, toolbar ] },
			{ template:"Some content" }
		]
	});
</script>
	</body>
</html>