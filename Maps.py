from items import shop_keeper_items_list
from character import NPC, Enemy

friend = [
    NPC(
        "Belle",
        ["Hello, Gabe!, Here is a recap of what has happened!", "I'm glad you came to visit me."],
        625,
        390,
        [R".\timefantasy_characters\timefantasy_characters\frames\chara\chara5_3"]
    )
]

enemy1 = Enemy(
    name="Phoenix",
    x=1515,
    y=1585,
    level=8,
    hp=200,
    mp=100,
    atk=30,
    dfn=20,
    spd=30,
    inventory={},
    skills=["Strike", "Flame Slash", "Earth Smash"],
    folder_paths=[R"Monsters\Phoenix"]
)
enemy1.sprite.set_animation("down_walk")

enemy2 = Enemy(
    name="Slime",
    x=1615,
    y=1885,
    level=8,
    hp=80,
    mp=40,
    atk=20,
    dfn=20,
    spd=30,
    inventory={},
    folder_paths=[R"Monsters\Slime"]
)
enemy2.sprite.set_animation("down_walk")

enemies = [enemy1, enemy2]

################## Stone Cave ##################
StoneCaveEnemy = Enemy(
    name="Phoenix",
    x=2490,
    y=520,
    level=15,
    hp=300,
    mp=100,
    atk=30,
    dfn=29,
    spd=30,
    inventory={},
    skills=["Strike", "Flame Slash", "Earth Smash"],
    folder_paths=[R"Monsters\Phoenix"]
)
StoneCaveEnemy.sprite.set_animation("down_walk")

StoneCaveEnemylist = [StoneCaveEnemy]
##################################################


###### Initial Village #######

###### Forest ######
forest_npc1 = NPC(
    "Forest Ranger",
    ["Only registered guild adventurers are allowed beyond this point—come back once you've joined the guild."],
    2730,
    1650,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc3_2"],    
)
forest_npc1.sprite.set_animation("up_stand")

forest_npcs = [forest_npc1]
####################

###### Lost Forest #######
lost_forest_npc1 = NPC(
    "Reiya",
    ["This bridge leads to a realm of whispers and shadows. Without the Guardian's blessing, you will never find your way back."],
    1970,
    2560,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_2"],  
)
lost_forest_npc1.sprite.set_animation("up_stand")
lost_forest_npcs = [lost_forest_npc1]
##########################

###### Castle Town ######
Eryndor_npc1 = NPC(
    "Old man",
    ["Welcome to Castle Town Eryndor, travelers! The heart of the kingdom and home to adventurers, merchants, and dreamers alike!"],
    2030,
    3307,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc1_5"],
)

Eryndor_npc2 = NPC(
    "Jason",
    ["You there! You look like you've got adventure in your eyes. If you're looking to make a name for yourself, head to the Adventurer's Guild. They'll set you on the right path."],
    1700,
    3017,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc1_6"],
)
Eryndor_npc3 = NPC(
    "Kaylan",
    ["Hey there, you can head to the Inn to rest and heal up from your travels. The Innkeeper is a good friend of mine."],
    1787,
    2157,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc1_6"],
)

Eryndor_gate_guard1 = NPC(
    "Gate Guard",
    ["The castle is restricted to authorized personnel only. Move along unless you have official business."],
    1710,
    289,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_6"]
)

Eryndor_gate_guard2 = NPC(
    "Gate Guard",
    ["State your business. The castle is off-limits to unauthorized personnel."],
    2039,
    289,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_6"]
)

Eryndor_npc1.sprite.set_animation("left_stand")
Eryndor_npc2.sprite.set_animation("right_stand")
Eryndor_npc3.sprite.set_animation("down_stand")
Eryndor_ncps = [Eryndor_npc1, Eryndor_npc2, Eryndor_gate_guard1, Eryndor_gate_guard2, Eryndor_npc3]
###### Castle 1F ######
Roderick = NPC(
    "Captain Roderick",
    ["Stay vigilant, adventurer. The kingdom's safety depends on those who are willing to stand against the darkness. If you need guidance, don't hesitate to ask."],
    1390,
    1659,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_5"]
)
castle_1F_npcs = [Roderick]

#########################

###### Castle 3F ######
king_npc = NPC(
    "King Aldric",
    [
        "Welcome, brave adventurer. What brings you to my court?",
        "The kingdom is in peril. We need heroes like you to restore peace.",
        "Do not let fear cloud your judgment. The fate of Eryndor rests in your hands."
    ],
    1480,
    509,
    [R"timefantasy_characters\timefantasy_characters\frames\chara\chara8_3"]
)

princess_npc = NPC(
    "Seraphina",
    ["If you ever need anything, don't hesitate to ask."],
    1550,
    699,
    [R"timefantasy_characters\timefantasy_characters\frames\chara\chara8_4"]
)

Guard_npc1 = NPC(
    "Guard",
    [
        "Halt! State your business in the castle.",
        "The king is busy, but I might let you through if you have a good reason.",
        "Stay vigilant. The kingdom's safety depends on all of us."
    ],
    1350,
    599,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_8"]
)

Guard_npc2 = NPC(
    "Guard",
    [
        "Only those with royal permission may enter the throne room.",
        "The castle is secure, but we must remain on high alert.",
        "If you're here to see the king, you'd better have a good reason."
    ],
    1601,
    599,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_8"]
)

Guard_npc3 = NPC(
    "Guard",
    [
        "The corridors are off-limits to unauthorized personnel.",
        "Keep moving, citizen. This area is restricted.",
        "The king's safety is our top priority. Do not cause trouble."
    ],
    1330,
    850,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_7"]
)
Guard_npc3.sprite.set_animation("right_stand")

Guard_npc4 = NPC(
    "Guard",
    [
        "Stay out of trouble, and we'll have no issues.",
        "The castle is no place for idle wanderers.",
        "If you have questions, speak to Captain Roderick."
    ],
    1620,
    850,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_7"]
)
Guard_npc4.sprite.set_animation("left_stand")

Guard_npc5 = NPC(
    "Guard",
    [
        "The royal treasury is off-limits. Move along.",
        "Do not test my patience, traveler.",
        "The king values loyalty and bravery above all else."
    ],
    1330,
    1000,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_7"]
)
Guard_npc5.sprite.set_animation("right_stand")

Guard_npc6 = NPC(
    "Guard",
    [
        "The castle gates are heavily guarded. No one gets in without clearance.",
        "If you're lost, I suggest heading back to the town.",
        "The kingdom's safety is our duty. Do not interfere."
    ],
    1620,
    1000,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_7"]
)
Guard_npc6.sprite.set_animation("left_stand")

Guard_npc7 = NPC(
    "Guard",
    [
        "The king is wise and just. Show him the respect he deserves.",
        "We stand ready to defend the kingdom at all costs.",
        "Do not loiter here. The castle is a place of business."
    ],
    1210,
    559,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_8"]
)

Guard_npc8 = NPC(
    "Guard",
    [
        "The throne room is ahead. Behave yourself.",
        "The king has many matters to attend to. Do not waste his time.",
        "If you seek an audience with the king, speak with the captain first."
    ],
    1740,
    559,
    [R"timefantasy_characters\timefantasy_characters\frames\military\military1_8"]
)

castle_3f_npcs = [king_npc, princess_npc, Guard_npc1, Guard_npc2, Guard_npc3, Guard_npc4, Guard_npc5, Guard_npc6, Guard_npc7, Guard_npc8]
#######################

###### Guild ######
reception_npc = NPC(
    "Reception girl",
    ["Welcome to the Adventurer's Guild! How can I assist you today?"],
    2157,
    1827,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc2_1"],
    guild=True
)

guild_npc = [reception_npc]

#####################

###### Item Shop ######
shop_keeper = NPC(
    "Shopkeeper",
    ["Welcome to my shop!  I sell potions and weapons."],
    970,
    600,
    [R".\timefantasy_characters\timefantasy_characters\frames\npc\npc1_2"],
    shop_keeper_items_list(),
)

itemshop_npcs = [shop_keeper]

##########################

##### Inn 1F ######
inn_owner = NPC(
    "Inn Owner",
    ["Welcome to my Inn! We've got warm beds, hot meals, and the best ale in town. Your HP and MP have been fully restored!"],
    1120,
    819,
    [R".\timefantasy_characters\timefantasy_characters\frames\npc\npc1_5"],
    inn=True
)

inn_1f_npcs = [inn_owner]

###############################################

###### House NPCs ######
house1_npc = NPC(
    "Miller Aldwin",
    ["The flour mill's been busy with the harvest. Good grain this season!", 
     "Watch yourself around the castle guards. They've been on edge since rumors of dark magic spread.",
     "My cousin works the fields north of town. Says the soil's not what it used to be."],
    400,
    300,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc1_7"]
)

house2_npc = NPC(
    "Seamstress Elspeth",
    ["I'm working on a new tapestry for the castle. The royal colors are quite particular.",
     "Imported silk costs a fortune these days! The merchant caravans barely make it through the mountain pass.",
     "Need a garment mended? I charge fair prices, not like that swindler in the marketplace."],
    460,
    780,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc2_3"]
)

house3_npc = NPC(
    "Herbalist Thaddeus",
    ["These herbs ward off the plague, or so the old wisdom says.",
     "The forest mushrooms have strange properties this season. I wouldn't forage without knowledge.",
     "The apothecary guild keeps their best remedies secret. Shameful, when people suffer!"],
    400,
    320,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc3_4"]
)

house4_npc = NPC(
    "Blacksmith Sarah",
    ["Forged a dozen horseshoes yesterday. My arms still ache!",
     "The knights demand the finest steel. Common folk make do with iron.",
     "My grandfather taught me to read the metal's glow. Too hot and it weakens, too cool and it won't take shape."],
    1340,
    580,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc4_5"]
)

house5_npc = NPC(
    "Widow Matilda",
    ["I've seen sixty winters come and go. The last one took my husband.",
     "In my youth, I served in the castle kitchens. The lord was fond of venison pie.",
     "Children these days know nothing of respect. In my day, we stood when elders entered the room!"],
    460,
    780,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc2_8"]
)

house6_npc = NPC(
    "Bard Cedric",
    ["I compose ballads of heroes and monsters. Care to hear my latest?",
     "The minstrel competition is next full moon. I aim to win the silver lyre this year.",
     "Tales travel faster than horsemen in these lands. Have you heard of the dragon in the northern peaks?"],
    830,
    670,
    [R"timefantasy_characters\timefantasy_characters\frames\npc\npc1_3"]
)
###############################################

map_configs = {
    "Map002": {
        "map_image_path": R"Backgrounds/Map002.png",
        "npcs": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": True,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds/Map002.json",
        "transitions": [
        ]
    },
    "Forest" : {
        "map_image_path": R"Backgrounds/forest.png",
        "npcs": forest_npcs,
        "map_scale_factor": 4,
        "bgm": None,
        "allow_encounters": True,
        "random_encounter_enemies": ["Slime", "Bat", "Snake(Green)"],
        "encounter_rate": 0.005,
        "layer_json_path": R"Backgrounds/forest/forest.json",
        "transitions": [
            {"zone": (1175, 2749, 1425, 2820), "target": "Hearthaven Village", "player_x": 3550, "player_y": 1150},
            {"zone": (1170, 35, 1420, 40), "target": "Eryndor", "player_x": 1860, "player_y": 3619},
            {"zone": (2840, 1340, 2870, 1600), "target": "Lost Forest", "player_x": 80, "player_y": 1650}
        ],
        "battle_background_image": ".\craftpix-net-270096-free-forest-battle-backgrounds\PNG\game_background_4\game_background_4.png"
    },
    "Lost Forest": {
        "map_image_path": R"Backgrounds/lost_forest.png",
        "npcs": lost_forest_npcs,
        "map_scale_factor": 4,
        "bgm": None,
        "allow_encounters": True,
        "random_encounter_enemies": ["Bee", "Mouse", "Spider", "Scorpion", "Snake(Pink)"],
        "encounter_rate": 0.005,
        "layer_json_path": R"Backgrounds/lost_forest/lost_forest.json",
        "transitions": [
            {"zone": (0, 1510, 40, 1780), "target": "Forest", "player_x": 2800, "player_y": 1450},
            {"zone": (2140, 2180, 2200, 2260), "target": "stone_cave", "player_x": 1120, "player_y": 1970}
        ],
        "battle_background_image": ".\craftpix-net-270096-free-forest-battle-backgrounds\PNG\game_background_4\game_background_4.png"
    },
    "stone_cave": {
        "map_image_path": R"Backgrounds/stone_cave.png",
        "npcs": [],
        'enemies': StoneCaveEnemylist,
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": True,
        "random_encounter_enemies": ["Alligator", "Armagiro", "Crub", "Turtle"],
        "encounter_rate": 0.005,
        "layer_json_path": R"Backgrounds/stone_cave/stone_cave.json",
        "transitions": [
            {"zone": (1080, 2040, 1150, 2110), "target": "Lost Forest", "player_x": 2160, "player_y": 2290},
            {"zone": (880, 1040, 1020, 1170), "target": "stone_cave", "player_x": 530, "player_y": 820},
        ],
        "battle_background_image": "Backgrounds/cave_battle.png"
    },
    "Eryndor": {
        "map_image_path": R"Backgrounds/Eryndor.png",
        "npcs": Eryndor_ncps,
        "map_scale_factor": 4,
        "bgm": None,
        "allow_encounters": True,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds/Eryndor/Eryndor.json",
        "transitions": [
            {"zone": (1750, 3749, 1990, 3800), "target": "Forest", "player_x": 1280, "player_y": 200},
            {"zone": (1770, 0, 2000, 95), "target": "Eryndor Castle", "player_x": 2060, "player_y": 3960},
            {"zone": (980, 2789, 1030, 2829), "target": "Guild", "player_x": 1467, "player_y": 2637},
            {"zone": (2510, 1900, 2570, 1970), "target": "Eryndor Shop", "player_x": 750, "player_y": 1080},
            {"zone": (867, 1687, 957, 1787), "target": "Inn 1F", "player_x": 1040, "player_y": 1360},
            {"zone": (2217, 2937, 2297, 3037), "target": "House1", "player_x": 620, "player_y": 575},
            {"zone": (2597, 2937, 2687, 3037), "target": "House2", "player_x": 620, "player_y": 575},
            {"zone": (2787, 627, 2877, 717), "target": "House3", "player_x": 620, "player_y": 575},
            {"zone": (2980, 2739, 3070, 2829), "target": "House4", "player_x": 900, "player_y": 1160},
            {"zone": (3457, 1427, 3547, 1487), "target": "House5", "player_x": 900, "player_y": 1160},
            {"zone": (977, 657, 1047, 727), "target": "House6", "player_x": 830, "player_y": 1070}
        ]
    },
    "Eryndor Castle": {
        "map_image_path": R"Backgrounds/castle.png",
        "npcs": [],
        "map_scale_factor": 4,
        "bgm": None,
        "allow_encounters": True,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds/castle/castle.json",
        "transitions": [
            {"zone": (1860, 4000, 2250, 4080), "target": "Eryndor", "player_x": 1870, "player_y": 229},
            {"zone": (2040, 1820, 2100, 1870), "target": "Eryndor Castle 1F", "player_x": 1480, "player_y": 2599},
        ]
    },
    "Eryndor Castle 1F": {
        "map_image_path": R"Backgrounds/castle1F.png",
        "npcs": castle_1F_npcs,
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": True,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds/castle1F/castle1F.json",
        "transitions": [
            {"zone": (1370, 2699, 1580, 2829), "target": "Eryndor Castle", "player_x": 2070, "player_y": 1929},
            {"zone": (1370, 1399, 1580, 1549), "target": "Eryndor Castle 3F", "player_x": 1480, "player_y": 1549},
            
        ]
    },
    "Eryndor Castle 3F": {
        "map_image_path": R"Backgrounds/castle3F.png",
        "npcs": castle_3f_npcs,
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": True,
        "encounter_rate": 0,
        "layer_json_path": "Backgrounds/castle3F/castle3F.json",
        "transitions": [
            {"zone": (1370, 1609, 1580, 1679), "target": "Eryndor Castle 1F", "player_x": 1480, "player_y": 1619},
            {"zone": (1370, 1129, 1580, 1269), "target": "Eryndor Castle 3F", "player_x": 1480, "player_y": 1619},
        ]
    },
    "Guild": {
        "map_image_path": R"Backgrounds/guild.png",
        "npcs": guild_npc,
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": True,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds/guild/guild.json",
        "transitions": [
            {"zone": (1327, 2727, 1627, 2827), "target": "Eryndor", "player_x": 997, "player_y": 2857},
        ]
    },
    "Eryndor Shop": {
        "map_image_path": R"Backgrounds/itemshop.png",
        "npcs": itemshop_npcs,
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": True,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds/itemshop/itemshop.json",
        "transitions": [
            {"zone": (720, 1120, 790, 1170), "target": "Eryndor", "player_x": 2547, "player_y": 1997},
        ]
    },
    "Inn 1F": {
        "map_image_path": R"Backgrounds/inn_1F.png",
        "npcs": inn_1f_npcs,
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": True,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds/inn1F/inn1F.json",
        "transitions": [
            {"zone": (1010, 1420, 1070, 1460), "target": "Eryndor", "player_x": 917, "player_y": 1817},
        ]
    },

    "dungeon_map": {
        "map_image_path": R".\Backgrounds\Map-L.png",
        "npcs": [],
        "enemies": enemies,
        "map_scale_factor": 0.3,
        "bgm": R"music\CaveTheme.mp3",
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": None,
        "transitions": []  
    },
  
    "Hearthaven Village": {
        "map_image_path": R".\Backgrounds\TownMapv1.png",
        "npcs": [],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\TownMapV1\TownMapV1.json",
        "transitions": [
            {"zone": (2020, 340, 2060, 400), "target": "playerhouse", "player_x": 620, "player_y": 575},
            {"zone": (1730, 340, 1775, 380), "target": "friendshouse", "player_x": 620, "player_y": 575},
            {"zone": (480, 1210, 520, 1240), "target": "House A", "player_x": 620, "player_y": 575},
            {"zone": (2160, 1250, 2200, 1290), "target": "House B", "player_x": 620, "player_y": 575},
            {"zone": (3600, 1090, 3640, 1200), "target": "Forest", "player_x": 1275, "player_y": 2649},
            {"zone": (580, 490, 620, 520), "target": "Hearthaven Shop", "player_x": 750, "player_y": 1080},
        ]
    },
    "playerhouse": {
        "map_image_path": R".\Backgrounds\playerhouse.png",
        "npcs": [],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\PlayerHouse\PlayerHouse.json",
        "transitions": [
            {"zone": (590, 600, 685, 653), "target": "Hearthaven Village", "player_x": 2030, "player_y": 450}
        ]
    },
    "casino_map": {
        "map_image_path": R".\Backgrounds\casino.png",
        "npcs": [],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": None,
        "transitions": []
    },
    "friendshouse": {
        "map_image_path": R".\Backgrounds\FriendsHouse.png",
        "npcs": friend,
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\FriendsHouse\FriendsHouse.json",
        "transitions": [
            {"zone": (590, 600, 685, 653), "target": "Hearthaven Village", "player_x": 1750, "player_y": 440}
        ]
    },

    "House A" : {
        "map_image_path": R".\Backgrounds\playerhouse.png",
        "npcs": [],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\PlayerHouse\PlayerHouse.json",
        "transitions": [
            {"zone": (590, 600, 685, 653), "target": "Hearthaven Village", "player_x": 500, "player_y": 1270}
        ]
    },

    "House B": {
        "map_image_path": R".\Backgrounds\FriendsHouse.png",
        "npcs": [],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\FriendsHouse\FriendsHouse.json",
        "transitions": [
            {"zone": (590, 600, 685, 653), "target": "Hearthaven Village", "player_x": 2190, "player_y": 1320}
        ]
    },

    "Hearthaven Shop": {
        "map_image_path": R"Backgrounds/itemshop.png",
        "npcs": itemshop_npcs,
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": True,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds/itemshop/itemshop.json",
        "transitions": [
            {"zone": (720, 1120, 790, 1170), "target": "Hearthaven Village", "player_x": 600, "player_y": 540},
        ]
    },

    "House1": {
        "map_image_path": R".\Backgrounds\playerhouse.png",
        "npcs": [house1_npc],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\PlayerHouse\PlayerHouse.json",
        "transitions": [
            {"zone": (590, 600, 685, 653), "target": "Eryndor", "player_x": 2257, "player_y": 3067}
        ]
    },

    "House2": {
        "map_image_path": R".\Backgrounds\FriendsHouse.png",
        "npcs": [house2_npc],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\FriendsHouse\FriendsHouse.json",
        "transitions": [
            {"zone": (590, 600, 685, 653), "target": "Eryndor", "player_x": 2637, "player_y": 3057}
        ]
    },

    "House3": {
        "map_image_path": R".\Backgrounds\FriendsHouse.png",
        "npcs": [house3_npc],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\FriendsHouse\FriendsHouse.json",
        "transitions": [
            {"zone": (590, 600, 685, 653), "target": "Eryndor", "player_x": 2837, "player_y": 767}
        ]
    },
    "House4": {
        "map_image_path": R".\Backgrounds\house2.png",
        "npcs": [house4_npc],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\house2\house2.json",
        "transitions": [
            {"zone": (870, 1265, 930, 1315), "target": "Eryndor", "player_x": 3020, "player_y": 2869}
        ]
    },
    "House5": {
        "map_image_path": R".\Backgrounds\house2.png",
        "npcs": [house5_npc],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\house2\house2.json",
        "transitions": [
            {"zone": (870, 1265, 930, 1315), "target": "Eryndor", "player_x": 3507, "player_y": 1537}
        ]
    },
    "House6": {
        "map_image_path": R".\Backgrounds\house1.png",
        "npcs": [house6_npc],
        "enemies": [],
        "map_scale_factor": 3,
        "bgm": None,
        "allow_encounters": False,
        "encounter_rate": 0,
        "layer_json_path": R"Backgrounds\house1\house1.json",
        "transitions": [
            {"zone": (800, 1120, 860, 1170), "target": "Eryndor", "player_x": 1007, "player_y": 757}
        ]
 
   },
}