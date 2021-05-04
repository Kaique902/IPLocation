# _________ _______  _        _______  _______  _______ __________________ _______  _       
# \__   __/(  ____ )( \      (  ___  )(  ____ \(  ___  )\__   __/\__   __/(  ___  )( (    /|
#    ) (   | (    )|| (      | (   ) || (    \/| (   ) |   ) (      ) (   | (   ) ||  \  ( |
#    | |   | (____)|| |      | |   | || |      | (___) |   | |      | |   | |   | ||   \ | |
#    | |   |  _____)| |      | |   | || |      |  ___  |   | |      | |   | |   | || (\ \) |
#    | |   | (      | |      | |   | || |      | (   ) |   | |      | |   | |   | || | \   |
# ___) (___| )      | (____/\| (___) || (____/\| )   ( |   | |   ___) (___| (___) || )  \  |
# \_______/|/       (_______/(_______)(_______/|/     \|   )_(   \_______/(_______)|/    )_)
#                                                                                           
#  _        _______ _________ _______           _______   _____   _______  _______          
# | \    /\(  ___  )\__   __/(  ___  )|\     /|(  ____ \ / ___ \ (  __   )/ ___   )         
# |  \  / /| (   ) |   ) (   | (   ) || )   ( || (    \/( (   ) )| (  )  |\/   )  |         
# |  (_/ / | (___) |   | |   | |   | || |   | || (__    ( (___) || | /   |    /   )         
# |   _ (  |  ___  |   | |   | |   | || |   | ||  __)    \____  || (/ /) |  _/   /          
# |  ( \ \ | (   ) |   | |   | | /\| || |   | || (            ) ||   / | | /   _/           
# |  /  \ \| )   ( |___) (___| (_\ \ || (___) || (____/\/\____) )|  (__) |(   (__/\         
# |_/    \/|/     \|\_______/(____\/_)(_______)(_______/\______/ (_______)\_______/         
#
# https://github.com/Kaique902
# https://github.com/Kaique902
# kaique902.github.io
from requests import get
import json
import re
import sys

print(''' 
8  8""""8                                             
8  8    8 e     eeeee eeee eeeee eeeee e  eeeee eeeee 
8e 8eeee8 8     8  88 8  8 8   8   8   8  8  88 8   8 
88 88     8e    8   8 8e   8eee8   8e  8e 8   8 8e  8 
88 88     88    8   8 88   88  8   88  88 8   8 88  8 
88 88     88eee 8eee8 88e8 88  8   88  88 8eee8 88  8 
                                                      
8   8                            eeeee eeeeee eeee    
8   8  eeeee e  eeeee e   e eeee 8   8 8    8    8    
8eee8e 8   8 8  8   8 8   8 8    8eee8 8    8    8    
88   8 8eee8 8e 8   8 8e  8 8eee    88 8    8 eee8    
88   8 88  8 88 8 __8 88  8 88      88 8    8 8       
88   8 88  8 88 8e888 88ee8 88ee    88 8eeee8 8eee 

https://github.com/Kaique902
kaique902.github.io

	''')
'''ip = get('https://api.ipify.org').text'''
ip = get('http://meuip.com/api/meuip.php').text
print('My public IP address is: {}'.format(ip))

arg = sys.argv

def main(arg):


	def check(arg):

	    if(re.search("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", arg[1])):
	    	execute(arg)
	    else:
	        helpess()

	def execute(arg):

		detailed = get('http://ip-api.com/json/{}?fields=status,message,query,countryCode,country,regionName,city,lat,lon,org,as'.format(arg[1])).text
		detailed = json.loads(detailed)

		if detailed['status'] == 'fail':
			print('Verification failed\nMessage: {} is a {}'.format(arg[1],detailed['message']))
		else:
			print('Nerd statistics: \n IP: {} \n Country Code: {} \n Country: {} \n Region: {} \n City: {} \n lat: {} \n lon {} \n ISP: {} \n AS: {} \n'.format(detailed['query'], detailed['countryCode'], detailed['country'], detailed['regionName'], detailed['city'], detailed['lat'], detailed['lon'], detailed['org'], detailed['as'][0:7]))

	def helpess():
		print("Sintax usage: \n")
		print(
		'''
			{} IP

			{} 8.8.8.8
		'''.format(arg[0],arg[0]))

	if len(arg) == 1:
		helpess()
	else:
		check(arg)

main(arg)