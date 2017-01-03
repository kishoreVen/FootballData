from urllib.request import urlopen           # Imports the library for fetching the html page using URL
from bs4 import BeautifulSoup                # Imports the library for scraping the html page
import pandas
import numpy
from Source.enums import EFootballTeams
from Source.enums import EGameLoc
from Source.enums import EGameResult

# Using the URL for the player, fetch the html page for the player from footballdb.com, and then convert it to bs format
playerUrl       = "http://www.footballdb.com/players/antonio-brown-brownan05/gamelogs/2016"
playerHtmlPage  = urlopen(playerUrl)
playerSoup      = BeautifulSoup(playerHtmlPage, "html.parser")
playerTables    = playerSoup.find_all('table')

# With the player tables in bs format, make a dataframe for each table
playerRecStats  = playerTables[0]
playerDataFrame = pandas.read_html(str(playerRecStats))[0]

# Iterate over player data frame and place the data in respective stats table
newteamnames = []
newoppnames = []
newgameloc = []
newteamscores = []
newoppscores = []
newresults = []

for row in range(0, playerDataFrame.shape[0]):
    # Convert the team name from 'Xxx' string to Enum for processing later
    teamname = playerDataFrame.iloc[row]["Team"]
    teamname = EFootballTeams.find(teamname)
    newteamnames.append(teamname)

    # Convert the opp name from '<@> Xxx' string to Enum for processing later and find out if it is home or away game
    # away games have format @ teamname
    oppdetails = playerDataFrame.iloc[row]["Opp"].split()
    oppname = oppdetails[0] if len(oppdetails) == 1 else oppdetails[1]
    oppname = EFootballTeams.find(oppname)
    newoppnames.append(oppname)
    gameloc = EGameLoc.HOME if len(oppdetails) == 1 else EGameLoc.AWAY
    newgameloc.append(gameloc)

    # Convert result string into game result, team score, and opposition score
    # Result string has format, for example, W, 32 - 14
    resultstring = playerDataFrame.iloc[row]["Result"].split(", ")
    result = EGameResult.find(resultstring[0])
    scorestring = resultstring[1].split("-")
    teamscore = 0
    oppscore  = 0
    if result == EGameResult.W or result == EGameResult.D:
        teamscore = int(scorestring[0])
        oppscore = int(scorestring[1])
    else:
        teamscore = int(scorestring[1])
        oppscore = int(scorestring[0])
    newteamscores.append(teamscore)
    newoppscores.append(oppscore)
    newresults.append(result)


playerDataFrame['Team'] = pandas.Series(newteamnames)
playerDataFrame['Opp'] = pandas.Series(newoppnames)
playerDataFrame['Loc'] = pandas.Series(newgameloc)
playerDataFrame['Result'] = pandas.Series(newresults)
playerDataFrame['TeamScore'] = pandas.Series(newteamscores)
playerDataFrame['OppScore'] = pandas.Series(newoppscores)

for row in playerDataFrame.itertuples():
    print(row)
