import re

class Team: 
    def __init__(self, owner:str, wins:int, losses:int, division:str, scores:list, opponents:list):
        self.owner = owner 
        self.wins = wins 
        self.losses = losses 
        self.division = division
        self.scores = scores 
        self.opponents = opponents 

def teamBuilder(name, division, file):
    wins = 0 
    losses = 0 
    scores = []
    opponents = []
    with open(file, 'r', newline='\n') as f: 
        f = f.read()
        games = [' '.join(x.split('\n')).strip() for x in re.split('NFL Week \d{1,2}', f)]
        games.pop(0) # first element of list is empty 
        for game in games:
            if bool(re.search('^[W|L]', game)) == True: #If first value is W or L game complete, else not played
                m = re.match('(?P<result>[W|L])\s(?P<score>\d{2,3}\.\d{1,2})-\d{2,3}\.\d{1,2}[\s|@]+.+\(\d{1,2}-\d{1,2}-\d{1,2}\)\s(?P<opponent>\w+\s\w+)', game)
                scores.append(float(m.group('score')))
                opponents.append(m.group('opponent'))
                if m.group('result') == 'W': 
                    wins += 1 
                elif m.group('result') == 'L': 
                    losses += 1 
                else: 
                    raise ValueError('Result is not "W" or "L". ')
            else: 
                m = re.search('(?P<opponent>[\w\s]+)$', game)
                opponents.append(m.group('opponent'))

    return Team(name, wins, losses, division, scores, opponents)