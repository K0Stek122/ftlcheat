from pymem import Pymem

"""
player_base:
    hull
    scrap
    fuel
    missiles
    weapon_inventory
    weapon_fire_status

entity_list
    Increments every 0x4 starting from offset 0.
    health

crew_count is a base addres.
"""

offsets = {
    "player_base" : 0x0051348C,
    "hull" : 0xCC,
    "scrap" : 0x4D4,
    "fuel" : 0x494,
    "missiles" : [0x48, 0x1E8],
    "entity_list" : 0x00514E4C,
    "health" : 0x28,
    "crew_count" : 0x514E40,
    "weapon_inventory" : [0x48, 0x1C8],
    "weapon_fire_status" : 0x62C
}
def get_player_base():
    return pm.read_int(pm.base_address + offsets["player_base"])

def get_entity_list():
    return pm.read_int(pm.base_address + offsets["entity_list"])

def is_ingame():
    if get_player_base():
        return True
    return False

def get_hull():
    return pm.read_int(get_player_base() + offsets["hull"])

def set_hull(val : int):
    pm.write_int(get_player_base() + offsets["hull"], val)

def get_scrap():
    return pm.read_int(get_player_base() + offsets["scrap"])

def set_scrap(val : int):
    pm.write_int(get_player_base() + offsets["scrap"], val)

def get_fuel():
    return pm.read_int(get_player_base() + offsets["fuel"])

def set_fuel(val : int):
    pm.write_int(get_player_base() + offsets["fuel"], val)

def get_missiles():
    addr = pm.read_int(get_player_base() + offsets["missiles"][0])
    return pm.read_int(addr + offsets["missiles"][1])

def set_missiles(val : int):
    addr = pm.read_int(get_player_base() + offsets["missiles"][0])
    pm.write_int(addr + offsets["missiles"][1], val)

def get_crew_count():
    return pm.read_int(pm.base_address + offsets["crew_count"])

def get_health(entity):
    return pm.read_float(entity + offsets["health"])

def set_health(entity, val : float):
    pm.write_float(entity + offsets["health"], val)

def get_entity_at(i):
    return pm.read_long(get_entity_list() + i * 0x4)

def get_weapon_inventory():
    addr = pm.read_long(get_player_base() + offsets["weapon_inventory"][0])
    return pm.read_long(addr + offsets["weapon_inventory"][1])

def get_weapon_at(i):
    return pm.read_long(get_weapon_inventory() + i * 0x4)

def get_weapon_status(weapon):
    return pm.read_int(weapon + offsets["weapon_fire_status"])

def set_weapon_status(weapon, val):
    pm.write_int(weapon + offsets["weapon_fire_status"], val)

# DRONES
def get_drone_part_subtract_instr():
    return pm.pattern_scan_module(b"\x83\xAB\xCC\x01\x00\x00\x01\x89\xF1", pm.process_base)
def disable_drone_part_subtract_instr():
    pm.write_bytes(drone_part_subtract_instruction, b"\x90\x90\x90\x90\x90\x90\x90", 7)
def enable_drone_part_subtract_instr():
    pm.write_bytes(drone_part_subtract_instruction, b"\x83\xAB\xCC\x01\x00\x00\x01", 7)

pm = Pymem("FTLGame.exe")
drone_part_subtract_instruction = get_drone_part_subtract_instr()