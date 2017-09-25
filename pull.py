import json
import api
import datab
import utils
import time

players = utils.local_players()

year = 2015

datab.cur.execute("""
    INSERT INTO teams (teams) values (:teams)
""", {"teams": json.dumps(api.teams())})

datab.conn.commit()

for idx, player in enumerate(players):

    print player['player_name']
    print str((int(idx) + 1)) + ' of ' + str(len(players))

    player['player'] = json.dumps(player)
    player['stats'] = json.dumps(api.stats(player['player_id'], year))
    time.sleep(.5)
    player['four_factor'] = json.dumps(api.four_factor(player['player_id'], year))
    time.sleep(.5)
    player['advanced_stats'] = json.dumps(api.adv_stats(player['player_id'], year))
    time.sleep(.5)
    player['shots'] = json.dumps(api.shots(player['player_id'], year))
    time.sleep(.5)
    player['usage'] = json.dumps(api.usage(player['player_id'], year))
    time.sleep(.5)
    player['misc'] = json.dumps(api.misc(player['player_id'], year))
    time.sleep(.5)

    datab.cur.execute("""
    INSERT INTO stats (
        player,
        stats,
        usage,
        four_factor,
        advanced_stats,
        shots,
        player_name,
        misc,
        birth_date,
        player_id,
        team_id,
        draftkings_id,
        position)
    VALUES (
        :player,
        :stats,
        :usage,
        :four_factor,
        :advanced_stats,
        :shots,
        :player_name,
        :misc,
        :birth_date,
        :player_id,
        :team_id,
        :draftkings_id,
        :position)
    """, player)

    datab.conn.commit()
