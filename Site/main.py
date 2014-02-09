import os
from flask import Flask, render_template, send_from_directory, request, session, redirect, url_for
#import leagueofdata
from bs4 import BeautifulSoup
import seleen
import getProb

app = Flask(__name__)
app.config.update(DEBUG = True,)
#app.secret_key = 'A1Zz98j/3yX R~XHH!?1N!AZX/,?RT'  #Temp secret


@app.route('/')
@app.route('/index/')
def index():
    return render_template('leagueofdata.html')

@app.route('/current/')
def current():
    return render_template('leaguecurrent.html')

@app.route('/current/',methods=['POST'])
def currentPost():
    summoner = request.form['summoner']
    if not summoner:
        return render_template('leaguecurrent.html',error="Please provide a summoner")
    #page = open('tayler.txt','r').read()
    page = seleen.lolKing(summoner, seleen.getBrowser())
    soup = BeautifulSoup(page)
    champrows = soup.find_all('td',{'class':'champion'})
    champs = []
    for champ in champrows:
        start = str(champ).find('<span') + 6
        end = str(champ).find('(',start)
        champs.append(str(champ)[start:end].strip())
    for i in range(0,len(champs)):
        champs[i] = champs[i].replace(' ','')
        champs[i] = champs[i].replace('\'','')
        champs[i] = champs[i].replace('.','')
    #return "Blue: " + str(champs[:5]) + "<br>Purple: " + str(champs[5:])
    team1 = soup.find('div',{'class':'team-1'})
    blueLinks = []
    for row in team1.find_all('td',{'class':'name'}):
        blueLinks.append('<a href="' + str(row.find('a')['href']) + '">' + str(row.find('span').text) + '</a>')
    
    team2 = soup.find('div',{'class':'team-2'})
    purpleLinks = []
    for row in team2.find_all('td',{'class':'name'}):
        purpleLinks.append('<a href="' + str(row.find('a')['href']) + '">' + str(row.find('span').text) + '</a>')
    blue = round(getProb.getProbability([champs[:5],champs[5:]]))
    purple=100.00-blue
    return render_template('results.html',blueLinks=enumerate(blueLinks),blueChamps=champs[:5],purpleLinks=enumerate(purpleLinks),purpleChamps=champs[5:],blue=blue,purple=purple)

@app.route('/simulate/')
def simulate():
    return render_template('simulate.html')

@app.route('/results/')
def simulae():
    return render_template('results.html')

@app.route('/simulate/',methods=['POST'])
def simulatePost():
    team1 = []
    team2 = []
    error = ""

    for i in range(1,6):
        if len(request.form['champ'+str(i)]) == 0 or len(request.form['champ'+str(i)+"2"]) == 0:
            error = "All champions must be entered"

    if error:
        return render_template('simulate.html',error=error)

    for i in range(1,6):
        team1.append(request.form['champ'+str(i)])
        team2.append(request.form['champ'+str(i)+"2"])

    blue = 60
    blue = round(getProb.getProbability([champs[:5],champs[5:]]))
    purple=100-blue
    return render_template('results.html',blueLinks=enumerate(team1),blueChamps=team1,purpleLinks=enumerate(team2),purpleChamps=team2,blue=blue,purple=purple)

@app.route('/about/')
def about():
    return render_template('leagueabout.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
