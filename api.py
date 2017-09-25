import config
import requests

requests.packages.urllib3.disable_warnings()

def api_buld(key):
    return config.BASE_URL + '/' + str(key) + config.API_QUERY

def players():
    url = api_buld('players')
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e

def player(player_id, season):
    url = api_buld('player') + '&player_id=' + str(player_id) + '&season=' + str(season)
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e

def usage(player_id, season):
    url = api_buld('usage/player') + '&player_id=' + str(player_id) + '&season=' + str(season)
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e

def four_factor(player_id, season):
    url = api_buld('four_factor/player') + '&player_id=' + str(player_id) + '&season=' + str(season)
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e

def adv_stats(player_id, season):
    url = api_buld('advanced/player') + '&player_id=' + str(player_id) + '&season=' + str(season)
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e

def shots(player_id, season):
    url = api_buld('shots') + '&player_id=' + str(player_id) + '&season=' + str(season)
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e

def misc(player_id, season):
    url = api_buld('misc/player') + '&player_id=' + str(player_id) + '&season=' + str(season)
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e

def box_score(player_id, season):
    url = api_buld('boxscore/player') + '&player_id=' + str(player_id) + '&season=' + str(season)
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e

def teams():
    url = api_buld('team')
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e

def stats(player_id, season):
    url = 'https://probasketballapi.com/stats/players' + config.API_QUERY + '&player_id=' + str(player_id) + '&season=' + str(season)
    try:
        return requests.post(url, verify=False).json()
    except Exception as e:
        print e
