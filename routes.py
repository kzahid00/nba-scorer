from flask import *
import requests

app = Flask(__name__)

headers = {
        "X-RapidAPI-Key": "f76a5c6f73msha9d149310824ac6p1f4adbjsn15900c09e38d",
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

@app.route('/', methods=('GET', 'POST'))
def index():
    url = "https://api-nba-v1.p.rapidapi.com/standings"

    querystring = {"league":"standard","season":"2023"}    

    newresponse = requests.get(url, headers=headers, params=querystring)

    json = newresponse.json()
    response_list = json['response']
    eastteams = []
    westteams = []
    for team in response_list:
        # if team['conference']['name'] == 'east':
        dic = {}
        dic['logo'] = team['team']['logo']
        dic['name'] = team['team']['name']
        dic['rank'] = team['conference']['rank']
        dic['win'] = team['conference']['win']
        dic['loss'] = team['conference']['loss']
        dic['percentage'] = team['win']['percentage']
        if  team['gamesBehind'] == None:
            dic['gb'] = 0
        else:
            dic['gb'] = team['gamesBehind']
        if team['winStreak'] == True:
            dic['worlstreak'] = 'W'
        elif team['winStreak'] == False:
            dic['worlstreak'] = 'L'
        dic['strk'] = team['streak']
        dic['last10'] = f"{team['win']['lastTen']}-{team['loss']['lastTen']}"
            
        if team['conference']['name'] == 'east':
            eastteams.append(dic)
        elif team['conference']['name'] == 'west':
            westteams.append(dic)        
        
    eastranked = sorted(eastteams, key=lambda x: x['rank'])
    westranked = sorted(westteams, key=lambda x: x['rank'])
    
    return render_template('index.html', teams=eastranked, wteams=westranked)
 
 
if __name__ == '__main__':
    app.run(debug=True)