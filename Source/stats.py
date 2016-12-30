from datetime import datetime
from Source.enums import EFootballTeams
from Source.enums import EGameResult

# stats_base is the base class type for all the statistics that will be scraped from football db
# The members are
# .... date         - the date of the game
# .... team         - the team the player belongs to
# .... opp          - the opposition the team played against
# .... home         - the place where the game was played
# .... res          - the result of the game
# .... teamscore    - points scored by team
# .... oppscore     - points scored by opposition
class stats_base:
    def __init__(self):
        self.date = datetime.now()
        self.team = EFootballTeams.NUM
        self.opp  = EFootballTeams.NUM
        self.home = False
        self.res  = EGameResult.T
        self.teamscore = 0
        self.oppscore = 0