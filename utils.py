import json
import datab

def local_players():
    with open('players.json') as p:
        players = json.load(p)
    return players


def get_player_data():
    datab.cur.execute("""
        SELECT * FROM stats
        WHERE stats.stats != "[]"
        AND stats.advanced_stats != "[]"
    """)
    return datab.cur.fetchall()

def get_team_data():
    datab.cur.execute("""
        SELECT * FROM teams
    """)

    return json.loads(datab.cur.fetchone()[1])


def avg_data(data):

    data = json.loads(data)
    keys = data[0].keys()
    agg = {}

    for key in keys:
        agg[key] = round(sum(float(c[key]) for c in data) / len(data), 3)
    return agg


def max_data(data):
    data = json.loads(data)
    keys = data[0].keys()
    agg = {}

    for key in keys:
        agg[key] = round(max(float(c[key]) for c in data) / len(data), 3)
    return agg


def calc_conversion(data, maxes):

    data['converted'] = {}

    # FREE THROWS
    if data['avg']['box_fta'] != 0 and data['avg']['box_ftm'] != 0:
        data['converted']['ft'] = int(round((float(data['avg']['box_ftm']) / float(maxes['box_ftm'])) * 100))
    else:
        #print data['player_name']
        data['converted']['ft'] = 0

    # SPEED
    if data['avg']['trk_speed'] != 0:
        data['converted']['spd'] = int(round((data['avg']['trk_speed'] / maxes['trk_speed']) * 100))
    else:
        data['converted']['spd'] = 0
    # ENDURANCE
    trk_dist_norm =  data['avg']['trk_dist'] / maxes['trk_dist']
    trk_box_min_norm =  data['avg']['box_minutes'] / maxes['box_minutes']
    data['converted']['endu'] =  int(round(((trk_dist_norm + trk_box_min_norm) / 2) * 100))

    # JUMP, REBOUND
    adv_dreb_pct = data['avg']['adv_dreb_pct'] / maxes['adv_dreb_pct'] * 100
    adv_oreb_pct = data['avg']['adv_oreb_pct'] / maxes['adv_oreb_pct'] * 100
    box_dreb = data['avg']['box_dreb'] / maxes['box_dreb'] * 100
    box_oreb = data['avg']['box_oreb'] / maxes['box_oreb'] * 100
    adv_treb_pct = data['avg']['adv_treb_pct'] / maxes['adv_treb_pct'] * 100

    data['converted']['reb'] = int(round((adv_dreb_pct + adv_oreb_pct + box_dreb + box_oreb) / 4))
    data['converted']['jmp'] = int(round((adv_dreb_pct + adv_oreb_pct + box_dreb + box_oreb + adv_treb_pct) / 5))

    # HEIGHT
    adv_off_rating = int(round(data['avg']['adv_off_rating'] / maxes['adv_off_rating'] * 100))
    adv_def_rating = int(round(data['avg']['adv_def_rating'] / maxes['adv_def_rating'] * 100))
    print int(round((adv_off_rating + adv_def_rating + adv_dreb_pct + adv_oreb_pct + box_dreb + box_oreb + adv_treb_pct) / 7))
    data['converted']['hgt'] = int(round((adv_off_rating + adv_def_rating + adv_dreb_pct + adv_oreb_pct + box_dreb + box_oreb + adv_treb_pct) / 7))

    # HEIGHT
    adv_usg_pct = int(round(data['avg']['adv_usg_pct'] / maxes['adv_usg_pct'] * 100))
    trk_touches = int(round(data['avg']['trk_touches'] / maxes['trk_touches'] * 100))
    data['converted']['drb'] = int(round((adv_usg_pct + trk_touches) / 2))

    # Blocks
    data['converted']['blk'] = int(round(data['avg']['box_blk'] / maxes['box_blk'] * 100))

    # Inside
    data['converted']['ins'] = int(round(data['avg']['misc_pts_paint'] / maxes['misc_pts_paint'] * 100))

    # DUNK
    data['converted']['dnk'] = int(round((data['converted']['hgt'] + data['converted']['ins']) / 2))

    # Field Goalds
    data['converted']['fg'] = int(round(data['avg']['box_fgm'] / maxes['box_fgm'] * 100))

    # Three Pointers
    data['converted']['tp'] =  20 + int(round(data['avg']['box_fg3m'] / maxes['box_fg3m'] * 100))

    # Steals
    data['converted']['stl'] = int(round(data['avg']['box_stl'] / maxes['box_stl'] * 100))

    # Potential
    adv_off_rating = int(round(data['avg']['adv_off_rating'] / maxes['adv_off_rating'] * 100))
    adv_def_rating = int(round(data['avg']['adv_def_rating'] / maxes['adv_def_rating'] * 100))
    data['converted']['pot'] = int(round((adv_off_rating + adv_def_rating) / 2))

    # Assist
    box_ast = int(round(data['avg']['box_ast'] / maxes['box_ast'] * 100))
    trk_sast = int(round(data['avg']['trk_sast'] / maxes['trk_sast'] * 100))
    data['converted']['pss'] = int(round((box_ast + trk_sast) / 2))

    # Strength
    adv_def_rating = int(round(data['avg']['adv_def_rating'] / maxes['adv_def_rating'] * 100))
    trk_speed = int(round(data['avg']['trk_speed'] / maxes['trk_speed'] * 100))
    data['converted']['stre'] = int(round((adv_def_rating + trk_speed) / 2))
    data['converted']['skills'] = []

    data.pop('stats', None)
    data.pop('normal', None)
    data.pop('avg', None)

    return data
