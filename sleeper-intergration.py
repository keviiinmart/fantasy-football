import requests
import json
import secrets


#secerts.py data
username = secrets.username
avatar = secrets.avatar_id
user_id = secrets.user_id
dynasty = secrets.dynasty_degenerates


#--------------------USER FUNCTIONS----------------------
#FUNCTION TO GET USER INFORMATION (I.E USERNAME, DISPLAY NAME, USER ID, AVATAR)
def getUserJSON(user_id):
	userInfo = f'https://api.sleeper.app/v1/user/{user_id}'
	user = requests.get(userInfo)
	if user.status_code == 200:
		user_json = user.json()
		username = user_json['username']
		user_id = user_json['user_id']
		display_name = user_json['display_name']
		avatar = user_json['avatar']
	return username,user_id,display_name,avatar

#--------------------LEAGUES FUNCTIONS--------------------

#FUNCTIONS TO GET ALL LEAGUES FOR USER
def getLeaguesForUser(user_id):
	return user_id

#GET SPECIFIC LEAGUE
def getSpecificLeague(leagueID):
	getLeague = f'https://api.sleeper.app/v1/league/{leagueID}'
	league = requests.get(getLeague)
	if league.status_code == 200:
		json1 = league.json()
		teams = json1['total_rosters']
		status = json1['status']
		setting = json1['settings']
		sport = json1['sport']
		seasonType = json1['season_type']
		season = json1['season']
		scoringSetting = json1['scoring_settings']
		rosterSetting = json1['roster_positions']
		leagueName = json1['name']
		leagueID = json1['league_id']
		draftID = json1['draft_id']
		avi = json1['avatar']
	return teams,status,setting,sport,seasonType,season,scoringSetting,rosterSetting,leagueName,leagueID,draftID,avi

#GET ROSTERS
def getRosters(leagueID):
	getLeague = f'https://api.sleeper.app/v1/league/{leagueID}/rosters' 
	league = requests.get(getLeague)
	if league.status_code == 200:
		teams = league.json()
		return teams
	
#GET USERS
def getUsers(leagueID):
	getLeague = f'https://api.sleeper.app/v1/league/{leagueID}/users'
	league = requests.get(getLeague)
	if league.status_code == 200:
		users = league.json()
		print(users)
		return users

getUsers(dynasty)
