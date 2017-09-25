import utils
import json
import pprint
import random

players = utils.get_player_data()
teams = utils.get_team_data()

newList = []
for player in players:
    newPlayer = {}
    avgs = utils.avg_data(player['stats'])
    newPlayer.update(json.loads(player['player']))
    newPlayer['stats'] = json.loads(player['stats'])
    newPlayer['avg'] = avgs
    newList.append(newPlayer)

maxes = {}
for key in newList[0]['avg'].keys():
    maxes[key] = max(l['avg'][key] for l in newList)

mins = {}
for key in newList[0]['avg'].keys():
    mins[key] = min(l['avg'][key] for l in newList)

normalList = []
keys = maxes.keys()
for player in newList:
    player['normal'] = dict((k, int(round(player['avg'][k] / maxes[k] * 100))) for k in keys)
    normalList.append(player)

converted = []
for player in normalList:
    converted.append(utils.calc_conversion(player, maxes))

complete = []
team_count = 0
team_max = 30
for idx, player in enumerate(converted):

    if team_count < 30:
        tid = team_count
    else:
        tid = -1

    complete_player = {}
    complete_player['name'] = player['player_name']
    complete_player['contract'] = {"amount":2100,"exp":2018 }
    complete_player['draft'] = {"round": 1,"pick": 1,"tid": 4,"originalTid": 4,"year": 2008}
    complete_player['college'] = 'Memphis'
    complete_player['pos'] = "PG"
    complete_player['hgt'] = player['converted']['hgt']
    complete_player['weight'] = 190
    complete_player['tid'] = tid
    complete_player['injury'] =  {"type": "Healthy", "gamesRemaining": 0}
    complete_player['awards'] = []
    complete_player['born'] = {"year":1988,"loc":"Chicago, IL"}
    complete_player['imgURL'] = "http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/3456.png"
    complete_player['ratings'] = [player['converted']]
    complete.append(complete_player)

    if idx != 0 and (idx % 10) == 0:
        team_count = team_count + 1


out = {}
out['players'] = complete
out["version"] = 24

with open('roster.txt', 'w') as outfile:
    json.dump(out, outfile, indent=2, sort_keys=True)

pick = random.randint(0, len(out['players']))
print out['players'][pick]['name']
print pprint.pprint(out['players'][pick])
