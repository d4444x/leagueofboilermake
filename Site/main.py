import os
from flask import Flask, render_template, send_from_directory, request, session, redirect, url_for
#import leagueofdata
from bs4 import BeautifulSoup
import seleen

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
    page = seleen.lolKing(summoner, seleen.getBrowser())
    soup = BeautifulSoup(page)
    bluetxt = soup.find('table',{'class':'blue-team'})
    bluelinks = bluetxt.find_all('a')
    champlinks = []
    for link in bluelinks:
        if '/champions/' in str(link):
            champlinks.append(str(link))
    blueChamps = []
    for link in champlinks:
        startp = link.find('/champions/') + 11
        endp = link.find('"',startp)
        if link[startp:endp] not in blueChamps:
            blueChamps.append(link[startp:endp])

    purpletxt = soup.find('table',{'class':'purple-team'})
    purplelinks = purpletxt.find_all('a')
    champlinks = []
    for link in purplelinks:
        if '/champions/' in str(link):
            champlinks.append(str(link))
    purpleChamps = []
    for link in champlinks:
        startp = link.find('/champions/') + 11
        endp = link.find('"',startp)
        if link[startp:endp] not in purpleChamps:
            purpleChamps.append(link[startp:endp])
    if '' in blueChamps:
        blueChamps.remove('')
        blueChamps.append('Yasuo')
    if '' in purpleChamps:
        purpleChamps.remove('')
        purpleChamps.append('Yasuo')
    return str(blueChamps) + str(purpleChamps)

    #Call team calc here
    #return render_template('results.html',results="")

@app.route('/simulate/')
def simulate():
    return render_template('simulate.html')

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

    #Call the team calc here

    return render_template('results.html',results="")

@app.route('/about/')
def about():
    return render_template('leagueabout.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
