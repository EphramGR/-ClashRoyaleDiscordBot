import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options

import time

from selenium.webdriver.common.action_chains import ActionChains

import sys

import argparse
import os

import datetime #import date

import socket

import sys, string, os, calendar, datetime, traceback
#from arcpy import env


def is_connected():
	while True:
		try:
			# connect to the host -- tells us if the host is actually
			# reachable
			socket.create_connection(("1.1.1.1", 53))
			break
		except OSError:
			pass


is_connected()

#import pyautogui

options = Options()
driver = webdriver.Chrome(executable_path='C:\\Users\\ephra\\Downloads\\test\\chromedriver.exe') 

weekday = datetime.datetime.now().weekday()
#weekday = 3

#0 monday 6 sunday
#2 wed, 3 thrs, 4 fri, 5 sat, 6 sun

#print(weekday)

important = ["War Decks Used Today", "War Decks Used", "Boat Attacks", "Medals"]

email = ''#put your own
password = ''

NOTE = ''

def goTo():
	driver.get("https://royaleapi.com/clan/LRPCRP92/war/race")
	#driver.set_window_size(1600, 900)

	time.sleep(1)


def getPlayers(names):
	time.sleep(1)
	#print("Getting info")
	for x in range(100):
		try:
			if driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[4]/div[3]/table/tbody/tr[{x+1}]/td[2]/div[1]/div').text == '--':
				#print("return1")
				return names
			names.append(driver.find_element(By.XPATH, f"//*[@id='page_content']/div[4]/div[3]/table/tbody/tr[{x+1}]/td[2]/div[1]/a").text)
			names.append(driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[4]/div[3]/table/tbody/tr[{x+1}]/td[2]/div[2]/div[{2}]').text)

		except:
			#print("return2")
			return names

	return names

#resets at 4:45 am

def writeToFile(file, array):
	with open(file, "w", encoding="utf-8") as f:
		f.write('\n'.join(array))


def read(file):
	num1 = []
	name1 = []


	with open(file,'r',encoding='utf-8') as f:
		string = f.read().splitlines() 
	
	for x in range(len(string)):
		if x % 2 == 0:
			name1.append(string[x])
		else:
			num1.append(string[x])

	#print(name1)
	#print(num1)

	return name1, num1

def merge(name1, num1):
	string = ''
	for x in range(len(name1)):
		string += name1[x]
		string += '\n'
		string += num1[x]
		string += '\n'
	return string

		
def checkNewPeople():
	newPlayers = []

	for x in range(len(nameNew)):
		test = True
		for y in range(len(wedName)):
			if wedName[y] == nameNew[x]:
				test = False

		if test:
			newPlayers.append(nameNew[x])

	return newPlayers

def difference(newPlayers, currentName, currentNum, pastNum, pastName):
	newNames = []

	for x in range(len(currentName)):
		for y in range(len(pastName)):
			if currentName[x] == pastName[y]:
				newNames.append(currentName[x])
				newNames.append(str(int(currentNum[x])-int(pastNum[y])))

		for y in range(len(newPlayers)):
			if newPlayers[y] == currentName[x]:
				newNames.append(currentName[x] + '*NEW*')
				newNames.append('N/A')

	return newNames

def docUpdate():
	driver.get("https://discord.com/login?redirect_to=%2Fchannels%2F%40me")
	time.sleep(1)

	try:
		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/input'))
			
		)
		element.send_keys(email)
	except:
		pass
	try:
		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[2]/div/input'))
			
		)
		element.send_keys(password)
	except:
		pass
	try:
		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]/div'))
			
		)
		element.click()
	except:
		pass
	
	try:
		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/nav/ul/div[2]/div[3]/div'))
			
		)
		element.click()
	except:
		pass

	time.sleep(1)
	try:
		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[5]'))
			
		)
		element.click()
	except:
		pass

	with open('dif.txt','r',encoding='utf-8') as f:
		s = f.read()
		s = '```' + datetime.datetime.now().strftime("%A, %B %d, %Y \n|%X EST|") + '\n' + s + '```' + NOTE + '\n'

	try:
		element = WebDriverWait(driver, 3).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div'))
			
		)
		element.send_keys(s)
	except:
		pass

	time.sleep(15)
	
try:
	goTo()

	names = []

	if weekday == 3:
		names = getPlayers(names)

		writeToFile('read.txt', names)

	else:
		wedName, wedNum = read('read.txt')
		
		##name, num = read('read.txt')

		names = getPlayers(names)

		writeToFile('read.txt', names)

		nameNew, numNew = read('read.txt')

		newP = checkNewPeople()
		#print(newP)
		
		writeToFile('dif.txt', difference(newP, nameNew, numNew, wedNum, wedName))

		docUpdate()


	#print('done')
except:
	d = datetime.datetime.now()
	with open("log.txt", "a") as log:
		log.write("------------------------------------------------------------------" + "\n")
		log.write("Log: " + str(d) + "\n")
		log.write("\n")

		tb = sys.exc_info()[2]
		tbinfo = traceback.format_tb(tb)[0]

		pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])

		log.write("" + pymsg + "\n")

	print("Potential issue, check log\n" + tbinfo)

driver.quit()

print('Finished')