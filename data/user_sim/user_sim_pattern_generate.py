import json

utt_gen_dict = \
{
	"categories":[
				{ 
				"slots":["categories"],
				"nl":"I need $categories$ food",
				},
				{ 
				"slots":["categories"],
				"nl":"I want $categories$ food",
				},
				{ 
				"slots":["categories"],
				"nl":"Find me $categories$ food",
				},	
				{ 
				"slots":["categories"],
				"nl":"I'm looking for $categories$ food",
				},
				{ 
				"slots":["categories"],
				"nl":"I need $categories$ restaurants",
				},
				{ 
				"slots":["categories"],
				"nl":"I want $categories$ restaurants",
				},
				{ 
				"slots":["categories"],
				"nl":"Find me $categories$ restaurants",
				},	
				{ 
				"slots":["categories"],
				"nl":"I'm looking for $categories$ restaurants",
				},		
				{ 
				"slots":["categories"],
				"nl":"$categories$",
				},
				{ 
				"slots":["categories"],
				"nl":"$categories$ food",
				},
				{ 
				"slots":["categories"],
				"nl":"$categories$ restaurants",
				},
				],
	"state":[
				{ 
				"slots":["state"],
				"nl":"$state$",
				},	
				{ 
				"slots":["state"],
				"nl":"In $state$",
				},	
			],
	"city":[
				{ 
				"slots":["city"],
				"nl":"$city$",
				},	
				{ 
				"slots":["city"],
				"nl":"In $city$",
				},		
			],
	"price":[
				{ 
				"slots":["price"],
				"nl":"$price$ price",
				},	
				{ 
				"slots":["price"],
				"nl":"$price$ pricing",
				},		
				{ 
				"slots":["price"],
				"nl":"$price$",
				},				
			],
	"stars":[
				{ 
				"slots":["stars"],
				"nl":"$stars$",
				},	
				{ 
				"slots":["stars"],
				"nl":"$stars$ stars",
				},		
			]
}

with open('utt_gen_dict.json', 'w') as f:
    json.dump(utt_gen_dict, f, indent=4)