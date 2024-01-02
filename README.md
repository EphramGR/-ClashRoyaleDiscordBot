There are two separate version of the Clash Royale Clan Manager. One is the discord bot, and the other is the web scraper. 

The web scraper does not make use of API's, and instead uses selenium to go through and get all relevent info pretainting to your clan. It is mean to be run on all war days just before 4am (when the data gets wiped). You can do this by having this run on a raspberry pi and using windows task scheduler to choose when to run. It needs to run every war day since Clash Royale does not store the cumlative amounts, only each day's. 
