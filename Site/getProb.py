import pickle
import sklearn
import random
from sklearn import linear_model
import os
def makeHeroArray(heros):
	rar = [0]*117
	for h in heros:
		rar[h] = 1
	return rar
def getProbability(teams):
    #sample [['Lucian', 'Gragas', 'Pantheon', 'Renekton', 'Soraka'], ['Riven', 'LeBlanc', 'Leona', 'Caitlyn', 'Lee Sin']]
    #print os.getcwd()
    clf = pickle.load( open( "Site/clf.p", "rb" ) )
    dics = pickle.load( open( "Site/dics.p", "rb" ) )
    mto = dics[1]
    invChamps = dics[0]
    championTypes = dics[2]
    
    left = teams[0]
    right = teams[1]
    leftStuns = 0
    rightStuns = 0
    for champion in left:
        if(champion in championTypes['Stun_champion']):
            leftStuns+=1
    for champion in right:
        if(champion in championTypes['Stun_champion']):
            rightStuns+=1
    for k,t in enumerate(teams):
        for i,c in enumerate(t):
            teams[k][i] = teams[k][i].replace(" ","")
            if(c=="LeBlanc"):
                teams[k][i] = "Leblanc"
            if(c=="KhaZix"):
                teams[k][i] = "Khazix"
            if(c=="Wukong"):
                teams[k][i] = "MonkeyKing"
            if(c=="Fiddlesticks"):
                teams[k][i] = "FiddleSticks"
            teams[k][i] = mto[invChamps[teams[k][i]]]
    m = makeHeroArray(teams[0])+makeHeroArray(teams[1])+[leftStuns+rightStuns]
    
    return 100.00*(1.0-(5.0+(clf.decision_function(m)[0]))/10.0)
