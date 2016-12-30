from urllib.request import urlopen           # Imports the library for fetching the html page using URL
from bs4 import BeautifulSoup                # Imports the library for scraping the html page
import pandas

# Using the URL for the player, fetch the html page for the player from footballdb.com, and then convert it to bs format
playerUrl       = "http://www.footballdb.com/players/antonio-brown-brownan05/gamelogs/2016"
playerHtmlPage  = urlopen(playerUrl)
playerSoup      = BeautifulSoup(playerHtmlPage, "html.parser")
playerTables    = playerSoup.find_all('table')

# With the player tables in bs format, make a dataframe for each table
playerRecStats  = playerTables[0]
playerDataFrame = pandas.read_html(str(playerRecStats))[0]

print(playerDataFrame.info())