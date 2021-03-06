import game
import jsonpickle
import copy
import simplejson
import re
#this is a helper file that manages saving the in-game data in JSON SI frame format

def save_data(LogicEngine, file_name="frames.json"):
    """this function saves game data in JSON form to the file"""

    # monsters_list = LogicEngine.monsters
    # final_monsters_dict = {"MONSTERS": monsters_list}
    #
    # player = LogicEngine.player
    # final_player_dict = {"PLAYER": player}

    map_tiles = LogicEngine.map.tiles_data
    final_tiles_dict = {"TILES": map_tiles}

    # mixtures_list = LogicEngine.mixtures
    # final_mixtures_dict = {"MIXTURES" : mixtures_list}

    jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)
    #final_JSON = jsonpickle.encode([final_player_dict, final_monsters_dict, final_tiles_dict, final_mixtures_dict], unpicklable=False)
    final_JSON = jsonpickle.encode([final_tiles_dict], unpicklable=False)
    re.sub("logic", "gono", final_JSON, re.MULTILINE)
    print(final_JSON)
    __save_to_file__(final_JSON, file_name)

def __save_to_file__(JSON, file_name, newFile=True):
    """this function rewrites the file with data in JSON form"""
    if(newFile):
        mode = 'w'
    else:
        mode = 'a+'
    with open(str(file_name), mode) as f:
        f.writelines(JSON)
