from urllib.request import urlopen           # Imports the library for fetching the html page using URL
from bs4 import BeautifulSoup                # Imports the library for scraping the html page
import pandas
import numpy
from Source.enums import EFootballTeams
from Source.enums import EGameLoc

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
for row in range(0, playerDataFrame.shape[0]):
    teamname = playerDataFrame.iloc[row]["Team"]
    teamname = EFootballTeams.find(teamname)
    newteamnames.append(teamname)
    oppdetails = playerDataFrame.iloc[row]["Opp"].split()
    oppname = oppdetails[0] if len(oppdetails) == 1 else oppdetails[1]
    oppname = EFootballTeams.find(oppname)
    newoppnames.append(oppname)
    gameloc = EGameLoc.HOME if len(oppdetails) == 1 else EGameLoc.AWAY
    newgameloc.append(gameloc)


playerDataFrame['Team'] = pandas.Series(newteamnames)
playerDataFrame['Opp'] = pandas.Series(newoppnames)
playerDataFrame['Loc'] = pandas.Series(newgameloc)

for row in playerDataFrame.itertuples():
    print(row)
