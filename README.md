There are two separate versions of the Clash Royale Clan Manager. One is the discord bot, and the other is the old web scraper. 

The web scraper does not make use of APIs, and instead uses selenium to go through and get all relevant info about your clan. It is meant to be run on all war days just before 4am (when the data gets wiped). You can do this by having this run on a Raspberry Pi and using Windows task scheduler to choose when to run. It needs to run every war day since Clash Royale does not store the cumulative amounts, only each day's data. It is stored in the localWithWebAutomation folder.

The new version, which uses the discord bot, and the Clash Royale API is everything outside of the folder. This includes relevant jsons to store past days, and the requesting and formating code.

