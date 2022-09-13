import requests


fixtures = "https://fantasy.premierleague.com/api/fixtures/"
teams = "https://fantasy.premierleague.com/api/teams/"
player = "https://fantasy.premierleague.com/api/element-summary/{}/"
# Get data from api endpoint
def get_data():
    r = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    return r.json()


# Get fixtures data for a week
def get_fixtures(week):
    r = requests.get(fixtures + "?event={}".format(week))
    return r.json()


# Get expected points for all players in a function
def get_expected_points():
    data = get_data()
    for player in data['elements']:
        print(player['web_name'], player['ep_next'])


# Get all points a given week for elemeent 283
def get_points(week, element):
    data = get_fixtures(week)
    for fixture in data:
        if fixture['element'] == element:
            return fixture['total_points']


# Get player data for eleeemeent 283
def get_player_data(element):
    r = requests.get(player.format(element))
    return r.json()

#data['elements'].sort(key=lambda x: x['total_points'], reverse=True)
#for player in data['elements']:
#    print(player['web_name'], player['total_points'], player['form'])

def main():
    #data = get_fixtures(1)
    #print(data['teams'])

    #print(len(data))
    #print(data[0]['stats'])

    pl = get_player_data(283)

    for match in pl['history']:
        print(match['round'], 
              match['minutes'], 
              match['was_home'], 
              match['opponent_team'], 
              match['total_points'])


if __name__ == "__main__":
    main()
