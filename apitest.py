import json
import requests
import discord
from datetime import datetime, time



#url = 'https://api.clashroyale.com/v1/clans/%23LRPCRP92/riverracelog'
log = 'log.txt'
key = 'replace with your own clash royale developer key'
url = 'https://api.clashroyale.com/v1/clans/%23LRPCRP92/currentriverrace'
headers = {'Authorization': f'Bearer {key}'}
page = requests.get(url, headers=headers)

# Dictionary with clash royale data
warDic = page.json()

# Write clash royale dictionary to json file
with open('clashroyalewar.json', 'w') as f:
	json.dump(warDic, f, indent=2)

clanStats = warDic["clan"]

with open('clanStats.json', 'w') as f:
	json.dump(clanStats, f, indent=2)

participants = clanStats['participants']

#print(participants)

url = 'https://api.clashroyale.com/v1/clans/%23LRPCRP92/members'#can change %23LRPCRP92 to your clan id
headers = {'Authorization': f'Bearer {key}'}
page = requests.get(url, headers=headers)

# Dictionary with clash royale data
memberDic = page.json()['items']

with open('members.json', 'w') as f:
	json.dump(memberDic, f, indent=2)

activeMembers = []

for i in range(len(memberDic)):
	for n in range(len(participants)):
		if memberDic[i]['tag'] == participants[n]['tag']:
			activeMembers.append(participants[n])

#print(activeMembers)
text = ''
def moreText(string):
	global text

	text += string

def returnTime():
	return datetime.time(datetime.now())

def sort(arr, sortBy):

	n = len(arr)
	
	for i in range(n):
	    for j in range(0, n - i - 1):
	        # Swap the elements if the element found is greater than the adjacent element
	        if arr[j][sortBy] > arr[j + 1][sortBy]:
	            arr[j], arr[j + 1] = arr[j + 1], arr[j]

def secondarySortByMedals(arr):
	four = []
	three = []
	two = []
	one = []
	zero = []

	for i in range(len(arr)):
		if arr[i]['decksUsedToday'] == 4:
			four.append(arr[i])
		elif arr[i]['decksUsedToday'] == 3:
			three.append(arr[i])
		elif arr[i]['decksUsedToday'] == 2:
			two.append(arr[i])
		elif arr[i]['decksUsedToday'] == 1:
			one.append(arr[i])
		else:
			zero.append(arr[i])

	sort(four, 'fame')
	sort(three, 'fame')
	sort(two, 'fame')
	sort(one, 'fame')
	sort(zero, 'fame')

	return zero + one + two + three + four


def invert(arr):
	n = len(arr)
	tempArr = [None] * n

	for i in range(n):
		tempArr[n-i-1] = arr[i]

	return tempArr	

def timeCheck(day = datetime.now().weekday(), hour = int(returnTime().strftime('%H')), minute = int(returnTime().strftime('%M'))):

	if day >= 3:
		if day == 3:
			if hour > 4:
				ongoingWar(day)
			elif hour == 4:
				if minute >= 50:
					ongoingWar(day)
				else:
					waitUntilWar()
			else:
				waitUntilWar()
		else:
			ongoingWar(day)
	else:
		waitUntilWar()

def waitUntilWar():
	global text
	text = 'There is no war yet.'

def ongoingWar(day):
	global activeMembers

	#potential problem if running at 4am on fri, and havent run before
	if day == 3:
		training = activeMembers

		#print(activeMembers)
		#print('\n\n\n\n')

		for i in range(len(training)):
			if training[i]['name'] == 'G.U.L.L.I.X':
				print(training[i]['decksUsed'], training[i]['decksUsedToday'], training[i]['decksUsed'] - training[i]['decksUsedToday'])
			training[i]['decksUsed'] = training[i]['decksUsed'] - training[i]['decksUsedToday']
			activeMembers[i]['decksUsed'] -= training[i]['decksUsed']

		for i in range(len(training)):
			if training[i]['name'] == 'G.U.L.L.I.X':
				print(training[i]['decksUsed'], training[i]['decksUsedToday'])

		#print(training)
		#print('\n\n\n\n')
		#print(activeMembers)
		#print(training)

		with open('training.json', 'w') as f:
			json.dump(training, f, indent=2)

	else:
		with open('training.json') as f:
			training = json.load(f)

		for i in range(len(training)):
			activeMembers[i]['decksUsed'] -= training[i]['decksUsed']


timeCheck(day = 3, hour = 4, minute = 50)

sort(activeMembers, 'decksUsedToday')

activeMembers = secondarySortByMedals(activeMembers)

activeMembers = invert(activeMembers)




if text != "There is no war yet.":
	for i in range(len(activeMembers)):
		moreText(activeMembers[i]['name'].ljust(16,' ') + f"| Attacks: {str(activeMembers[i]['decksUsed']).rjust(2,' ')} Today: {str(activeMembers[i]['decksUsedToday']).rjust(2,' ')} Medals: {str(activeMembers[i]['fame']).rjust(4, ' ')}\n")


moreText('\n')
'''moreText("Illigals: ")

for i in range(len(activeMembers)):
	if activeMembers[i]['decksUsed'] - activeMembers[i]['decksUsedToday'] < 4:
		moreText(f"{activeMembers[i]['name']}, ")'''

print(text)

with open(log, 'w', encoding='utf8') as f:
	f.write(text)

timeCheck()

#posts text file to discord
def discordLog(log):
	import discord
	from discord.ext import commands

	activity = discord.Activity(name='bot stuff', type=discord.ActivityType.watching)
	bot = discord.Client(activity=activity, intents=discord.Intents.default())

	@bot.event
	async def on_ready():
	    channel = bot.get_channel(1047351847314272256)
	    await channel.send(file=discord.File(log))

	bot.run("replace with your discord bot key")

#discordLog(log)

