# data/roles.py

CDN = "https://cdn.discordapp.com/emojis/"

def emoji_url(emoji_id: int):
    return f"{CDN}/{emoji_id}.png?size=96&quality=lossless"

ROLE_DATA = {
    1440783102711562260: {
        "name": "Animals",
        "emoji": emoji_url(1440781781342093423),
        "colour": "3d9db6"},
    1440778289986670746: {
        "name": "Ancient Terror",
        "emoji": emoji_url(1440782784191926344),
        "colour": "9fb948"},
    1441791745737232384: {
        "name": "Ashen Winds",
        "emoji": None,
        "colour": "a43c41"},
    1441793409286406174: {
        "name": "Athena's Fortune",
        "emoji": None,
        "colour": "3db6a3"},
    1441791762749460601: {
        "name": "Barnacled Dread",
        "emoji": None,
        "colour": "83d4f5"},
    1441792692190187691: {
        "name": "Barnacle Chests",
        "emoji": None,
        "colour": "3d9a8f"},
    1441791511489417378: {
        "name": "Bilge Rats",
        "emoji": None,
        "colour": "915b3e"},
    1441793277236875304: {
        "name": "Boar Tusks",
        "emoji": None,
        "colour": "947e6d"},
    1441791898997231798: {
        "name": "Bone Callers",
        "emoji": None,
        "colour": "bfd257"},
    1441791781636280351: {
        "name": "Burning Blade",
        "emoji": emoji_url(1441902687976427690),
        "colour": "fc6868"},
    1441792858943393925: {
        "name": "Cannonball Crate",
        "emoji": None,
        "colour": "7c7b7b"},
    1441792878803288084: {
        "name": "Cargo",
        "emoji": None,
        "colour": "70b955"},
    1441792604135100497: {
        "name": "Chest of Bones",
        "emoji": None,
        "colour": "994444"},
    1441791987123622019: {
        "name": "Chest of Fortune",
        "emoji": None,
        "colour": "d3a164"},
    1441792712054669413: {
        "name": "Chests of Sorrow",
        "emoji": None,
        "colour": "3974b3"},
    1441792738814066759: {
        "name": "Chests of a Thousand Grogs",
        "emoji": None,
        "colour": "d38844"},
    1441792894682927294: {
        "name": "Commodities",
        "emoji": None,
        "colour": "4178b8"},
    1441793472008032310: {
        "name": "Crested Queen",
        "emoji": emoji_url(1441902764711088179),
        "colour": "6759c9"},
    1441791931356156037: {
        "name": "Cursed Iron",
        "emoji": None,
        "colour": "4cba7c"},
    1441793187340619867: {
        "name": "Cursed Crews",
        "emoji": None,
        "colour": "b269f0"},
    1441792913813143686: {
        "name": "Devil's Roar Cargo",
        "emoji": None,
        "colour": "995c66"},
    1441792545746321570: {
        "name": "Emissary Flags",
        "emoji": emoji_url(1441902717332099232),
        "colour": "b668ad"},
    1441793790938448014: {
        "name": "Emissary Grades",
        "emoji": None,
        "colour": "b6689b"},
    1441794009621332048: {
        "name": "Faction Hero Treasure",
        "emoji": None,
        "colour": "50acc4"},
    1441791800900714648: {
        "name": "Feared Redmaw",
        "emoji": emoji_url(1441902709472231444),
        "colour": "f38382"},
    1441792940795232266: {
        "name": "Fruit Crate",
        "emoji": None,
        "colour": "e4ee69"},
    1441792009370337340: {
        "name": "Gifts",
        "emoji": None,
        "colour": "e09b5a"},
    1441792668983365682: {
        "name": "Gold Hoarder",
        "emoji": None,
        "colour": "e4c856"},
    1441793210828460153: {
        "name": "Ghost Ships",
        "emoji": None,
        "colour": "45c292"},
    1441793360330490060: {
        "name": "Guardians of Fortune",
        "emoji": None,
        "colour": "3db68f"},
    1441792961951305728: {
        "name": "Gunpowder Barrels",
        "emoji": None,
        "colour": "e4b956"},
    1441792025589710939: {
        "name": "Horn of Fair Winds",
        "emoji": None,
        "colour": "5c5bc9"},
    1441793455054651565: {
        "name": "Hungering One",
        "emoji": emoji_url(1441902756729323723),
        "colour": "466bce"},
    1441793258698313748: {
        "name": "Hunter's Call",
        "emoji": None,
        "colour": "60c2d7"},
    1441794111534403584: {
        "name": "Insider Activities",
        "emoji": None,
        "colour": "ffffff"},
    1441792052063895602: {
        "name": "Kingly Treasure",
        "emoji": emoji_url(1441902725347541103),
        "colour": "ba68de"},
    1441791824128638976: {
        "name": "Krakens",
        "emoji": None,
        "colour": "866957"},
    1441793431679537173: {
        "name": "Legend of the Veil",
        "emoji": None,
        "colour": "029a8f"},
    1441794033109303416: {
        "name": "Limited Time Events",
        "emoji": None,
        "colour": "919191"},
    1441792987507068979: {
        "name": "Lost Shipments",
        "emoji": None,
        "colour": "3a79b8"},
    1441792827133526210: {
        "name": "Merchant Alliance",
        "emoji": None,
        "colour": "3180b1"},
    1441793295435956285: {
        "name": "Megalodon Scales",
        "emoji": None,
        "colour": "ddad5e"},
    1441793318185996428: {
        "name": "Megalodon Teeth",
        "emoji": None,
        "colour": "c55e5c"},
    1441794089291878422: {
        "name": "Nautical Miles",
        "emoji": None,
        "colour": "3dadb6"},
    1441792074100768959: {
        "name": "Orb of Secrets",
        "emoji": None,
        "colour": "fc3737"},
    1441793159184121919: {
        "name": "Order of Souls",
        "emoji": None,
        "colour": "9567fc"},
    1441792094279565393: {
        "name": "Rag & Bone Crates",
        "emoji": None,
        "colour": "948981"},
    1441792507515240488: {
        "name": "Reaper's Bones",
        "emoji": None,
        "colour": "994444"},
    1441792564293275808: {
        "name": "Reaper's Chests",
        "emoji": None,
        "colour": "994040"},
    1441792172587483379: {
        "name": "Reaper Fortresses",
        "emoji": None}, #------------------------------------------------------------------------
    1441792624318218292: {
        "name": "Reaper Urn",
        "emoji": None,
        "colour": "994444"},
    1441791958476652614: {
        "name": "Scattershots",
        "emoji": None,
        "colour": "727171"},
    1441791845138038824: {
        "name": "Sea Fortresses",
        "emoji": None,
        "colour": "45b692"},
    1441794132547866634: {
        "name": "Sea of Thieves Drama",
        "emoji": None}, #------------------------------------------------------------------------
    1441793383776387213: {
        "name": "Servants of the Flame",
        "emoji": emoji_url(1441902748147908689),
        "colour": "993838"},
    1441793491540906116: {
        "name": "Shadowmaw",
        "emoji": None,
        "colour": "6b6969"},
    1441793507844165733: {
        "name": "Shrouded Ghost",
        "emoji": None,
        "colour": "ffe8e8"},
    1441793228885065808: {
        "name": "Skeleton Forts",
        "emoji": None,
        "colour": "a368b6"},
    1441793545068482754: {
        "name": "Skeleton Ships",
        "emoji": None,
        "colour": "94735a"},
    1441792583498989568: {
        "name": "Skull of Banished",
        "emoji": None,
        "colour": "c27c0e"},
    1441792120091316386: {
        "name": "Skull of Siren's Song",
        "emoji": None,
        "colour": "70b6c9"},
    1441792145789812827: {
        "name": "Smuggler's Chronicles",
        "emoji": None}, #------------------------------------------------------------------------
    1441793567986159789: {
        "name": "Stronghold Treasures",
        "emoji": None,
        "colour": "c6c6c6"},
    1441791865991987230: {
        "name": "Sunken Kingdom",
        "emoji": None,
        "colour": "4192b8"},
    1441794053652877364: {
        "name": "Tall Tales",
        "emoji": None,
        "colour": "5ea168"},
    1441792780270567505: {
        "name": "Vaults of the Ancients",
        "emoji": None,
        "colour": "e4a556"},
    1441794069419524228: {
        "name": "Voyage Completions",
        "emoji": None,
        "colour": "ae6c47"},
    1441793007262109767: {
        "name": "Wood Crate",
        "emoji": None,
        "colour": "7b5940"},
}

ALLOWED_ITEM_ROLES = list(ROLE_DATA.keys())

ROLE_EMOJI_MAP = {
    rid: data.get("emoji")
    for rid, data in ROLE_DATA.items()
}
