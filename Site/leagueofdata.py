import pandas as pd

games = pd.read_csv('league.csv',dtype={'champ101': object,'champ102': object,'champ103': object,'champ104': object,'champ105': object,'champ201': object,'champ202': object,'champ203': object,'champ204': object,'champ205': object},index_col=0,names=['champ101','champ102','champ103','champ104','champ105','winner','map','champ201','champ202','champ203','champ204','champ205','date'])
games['blue'] = games.champ101 + "," + games.champ102 + "," + games.champ103 +"," + games.champ104 +","+ games.champ105
games['purple'] = games.champ201 + "," + games.champ202 + "," + games.champ203 +"," + games.champ204 +","+ games.champ205

champNameToID = {u'Wukong': 62, u'Jax': 24, u'Shaco': 35, u'Warwick': 19, u'Nidalee': 76, u'Zyra': 143, u'Brand': 63, u'Rammus': 33, u'Corki': 42, u'Anivia': 34, u'Tryndamere': 23, u'MissFortune': 21, u'Yorick': 83, u'Xerath': 101, u'Sivir': 15, u'Riven': 92, u'Orianna': 61, u'Gangplank': 41, u'Malphite': 54, u'Poppy': 78, u'Karthus': 30, u'Jayce': 126, u'Blitzcrank': 53, u'Trundle': 48, u'Sejuani': 113, u'Graves': 104, u'Lucian': 236, u'Nocturne': 56, u'Lux': 99, u'Shyvana': 102, u'Renekton': 58, u'Fiora': 114, u'Jinx': 222, u'Fizz': 105, u'Kassadin': 38, u'Sona': 37, u'Vladimir': 8, u'Viktor': 112, u'Cassiopeia': 69, u'Maokai': 57, u'Thresh': 412, u'Kayle': 10, u'Hecarim': 120, u'Khazix': 121, u'Olaf': 2, u'Ziggs': 115, u'Syndra': 134, u'DrMundo': 36, u'Karma': 43, u'Annie': 1, u'Akali': 84, u'Leona': 89, u'Yasuo': 157, u'Kennen': 85, u'Rengar': 107, u'Ryze': 13, u'Shen': 98, u'Zac': 154, u'Pantheon': 80, u'Swain': 50, u'Sion': 14, u'Vayne': 67, u'Nasus': 75, u'TwistedFate': 4, u'Chogath': 31, u'Udyr': 77, u'Morgana': 25, u'Volibear': 106, u'Caitlyn': 51, u'Darius': 122, u'Zilean': 26, u'Rumble': 68, u'Skarner': 72, u'Teemo': 17, u'Urgot': 6, u'Amumu': 32, u'Galio': 3, u'Heimerdinger': 74, u'Ashe': 22, u'Singed': 27, u'Varus': 110, u'Twitch': 29, u'Garen': 86, u'Nunu': 20, u'MasterYi': 11, u'Elise': 60, u'Alistar': 12, u'Katarina': 55, u'Mordekaiser': 82, u'KogMaw': 96, u'Aatrox': 266, u'Draven': 119, u'FiddleSticks': 9, u'Talon': 91, u'XinZhao': 5, u'LeeSin': 64, u'Taric': 44, u'Malzahar': 90, u'Lissandra': 127, u'Diana': 131, u'Tristana': 18, u'Irelia': 39, u'JarvanIV': 59, u'Nami': 267, u'Soraka': 16, u'Veigar': 45, u'Janna': 40, u'Nautilus': 111, u'Evelynn': 28, u'Gragas': 79, u'Zed': 238, u'Vi': 254, u'Lulu': 117, u'Ahri': 103, u'Quinn': 133, u'Leblanc': 7, u'Ezreal': 81}
champIDToName = {1: u'Annie', 2: u'Olaf', 3: u'Galio', 4: u'TwistedFate', 5: u'XinZhao', 6: u'Urgot', 7: u'Leblanc', 8: u'Vladimir', 9: u'FiddleSticks', 10: u'Kayle', 11: u'MasterYi', 12: u'Alistar', 13: u'Ryze', 14: u'Sion', 15: u'Sivir', 16: u'Soraka', 17: u'Teemo', 18: u'Tristana', 19: u'Warwick', 20: u'Nunu', 21: u'MissFortune', 22: u'Ashe', 23: u'Tryndamere', 24: u'Jax', 25: u'Morgana', 26: u'Zilean', 27: u'Singed', 28: u'Evelynn', 29: u'Twitch', 30: u'Karthus', 31: u'Chogath', 32: u'Amumu', 33: u'Rammus', 34: u'Anivia', 35: u'Shaco', 36: u'DrMundo', 37: u'Sona', 38: u'Kassadin', 39: u'Irelia', 40: u'Janna', 41: u'Gangplank', 42: u'Corki', 43: u'Karma', 44: u'Taric', 45: u'Veigar', 48: u'Trundle', 50: u'Swain', 51: u'Caitlyn', 53: u'Blitzcrank', 54: u'Malphite', 55: u'Katarina', 56: u'Nocturne', 57: u'Maokai', 58: u'Renekton', 59: u'JarvanIV', 60: u'Elise', 61: u'Orianna', 62: u'Wukong', 63: u'Brand', 64: u'LeeSin', 67: u'Vayne', 68: u'Rumble', 69: u'Cassiopeia', 72: u'Skarner', 74: u'Heimerdinger', 75: u'Nasus', 76: u'Nidalee', 77: u'Udyr', 78: u'Poppy', 79: u'Gragas', 80: u'Pantheon', 81: u'Ezreal', 82: u'Mordekaiser', 83: u'Yorick', 84: u'Akali', 85: u'Kennen', 86: u'Garen', 89: u'Leona', 90: u'Malzahar', 91: u'Talon', 92: u'Riven', 96: u'KogMaw', 98: u'Shen', 99: u'Lux', 101: u'Xerath', 102: u'Shyvana', 103: u'Ahri', 104: u'Graves', 105: u'Fizz', 106: u'Volibear', 107: u'Rengar', 110: u'Varus', 111: u'Nautilus', 112: u'Viktor', 113: u'Sejuani', 114: u'Fiora', 115: u'Ziggs', 117: u'Lulu', 119: u'Draven', 120: u'Hecarim', 121: u'Khazix', 122: u'Darius', 126: u'Jayce', 127: u'Lissandra', 131: u'Diana', 133: u'Quinn', 134: u'Syndra', 143: u'Zyra', 154: u'Zac', 157: u'Yasuo', 222: u'Jinx', 236: u'Lucian', 238: u'Zed', 254: u'Vi', 266: u'Aatrox', 267: u'Nami', 412: u'Thresh'}



blue = '59,67,76,89,254'
purple = '7,36,62,236,412'
team = blue

def findMatches(blue,purple):
    potentials = games[games.blue == blue]
    matches = potentials[potentials.purple == purple]
    return matches

def teamWinRate(team):
    blues = games[games.blue == team]
    purples = games[games.purple == team]
    wins = len(blues[blues.winner == 100]) + len(purples[purples.winner == 200])
    total = len(blues) + len(purples)
    return 100.00 * wins/total


matches = findMatches(blue,purple)
blues = matches[matches.winner == 100]
if len(matches):
    rate = 100.00*len(blues)/len(matches)