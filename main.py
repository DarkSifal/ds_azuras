from dico import COUNTRY_LIST, EMAIL_DOMAIN_LIST
import os
from tabulate import tabulate
import json
from datetime import datetime
from datetime import date
import random
import urllib.request
from urllib.request import urlopen
from PIL import Image

def clear():
    os.system('clear')

colors = {
    'red': "\033[1;31;48m",
    'yellow': "\033[1;33;48m",
    'white': "\033[1;37;48m",
}

class Profile():
    firstname = ''
    lastname = ''
    gender = ''
    title =''
    address_number = ''
    address_street = ''
    address_city = ''
    address_state = ''
    address_country = ''
    address_postcode = ''
    email = ''
    username = ''
    password = ''
    birthdate = ''
    phone_number = ''
    cell_number = ''
    photo = ''

    def getFullName(self):
        return self.title+' '+self.firstname+' '+self.lastname
    
    def getFullAddress(self):
        address = str(self.address_number)+' '+self.address_street+'\n'+str(self.address_postcode)+', '+self.address_city+'\n'+self.address_state+', '+self.address_country
        return address
    
    def getBirthdate(self):
        realDate = self.birthdate[0:10]
        realDate = datetime.strptime(realDate, '%Y-%m-%d')
        return realDate.strftime("%d/%m/%Y")
    
    def getRealEmailAddress(self):
        newEmailAddress = self.email.replace('example', random.choice(EMAIL_DOMAIN_LIST))
        return newEmailAddress
    
    def displayProfile(self):
        print(colors['yellow']+'HERE IS YOUR FAKE ID !'+colors['white'])
        print('------------------------------------------------------------')
        print(colors['yellow']+'Gender : '+colors['white']+self.gender)
        print(colors['yellow']+'Full name : '+colors['white']+self.getFullName())
        print(colors['yellow']+'Date of birth : '+colors['white']+self.getBirthdate())
        print(colors['yellow']+'Email address : '+colors['white']+self.getRealEmailAddress())
        print(colors['yellow']+'Username : '+colors['white']+self.username)
        print(colors['yellow']+'Password to use : '+colors['white']+self.password)
        print(colors['yellow']+'Phone number : '+colors['white']+self.phone_number)
        print(colors['yellow']+'Cell phone number : '+colors['white']+self.cell_number)
        print(colors['yellow']+'Address : \n'+colors['white']+self.getFullAddress())
        print('------------------------------------------------------------')
        print('The photo is available in the current directory --> '+colors['yellow']+'profile_picture.png'+colors['white'])
        urllib.request.urlretrieve(self.photo, "profile_picture.png")

def mainTitle():
    print(colors['yellow'])
    print('--------------------------------------------------------')
    print('─█▀▀█ ░█▀▀▀█ ░█─░█ ░█▀▀█ ─█▀▀█ ░█▀▀▀█ ')
    print('░█▄▄█ ─▄▄▄▀▀ ░█─░█ ░█▄▄▀ ░█▄▄█ ─▀▀▀▄▄ ')
    print('░█─░█ ░█▄▄▄█ ─▀▄▄▀ ░█─░█ ░█─░█ ░█▄▄▄█')
    print('--------------------------------------------------------')
    print('Fake ID Generator - created by DARK SIFAL')
    print(colors['white'])


def countrySelection():
    print('Please select a country :')
    countryData = []
    allCountryIds = range(0, int(len(COUNTRY_LIST)-1))
    strCountryIds = []
    for w in allCountryIds:
        strCountryIds.append(str(w))
        countryData.append([str(w), COUNTRY_LIST[str(w)]['name']])
    print (tabulate(countryData, headers=["ID", "Code", "Country"], tablefmt='psql'))
    countryId = input('Your choice : ')
    while countryId not in strCountryIds:
        print(colors['red']+'Error ! This country doesn\'t exist !')
        countryId = input(colors['white']+'Please selet another one : ')
    return countryId

def generateFakeId(countryId):
    print(colors['yellow'])
    print('**********************************')
    print('> GENERATING FAKE ID')
    print('**********************************')
    print(colors['white'])

    countryCode = COUNTRY_LIST[countryId]['code']
    apiUrl = 'https://randomuser.me/api/?nat='+countryCode
    
    response = urlopen(apiUrl)
    jsonData = json.loads(response.read())
    results = jsonData['results'][0]
    
    p = Profile()
    p.gender = results['gender']
    p.firstname = results['name']['first']
    p.lastname = results['name']['last']
    p.title = results['name']['title']
    p.address_number = results['location']['street']['number']
    p.address_street = results['location']['street']['name']
    p.address_city = results['location']['city']
    p.address_state = results['location']['state']
    p.address_country = results['location']['country']
    p.address_postcode = results['location']['postcode']
    p.email = results['email']
    p.username = results['login']['username']
    p.password = results['login']['password']
    p.birthdate = results['dob']['date']
    p.phone_number = results['phone']
    p.cell_number = results['cell']
    p.photo = results['picture']['large']
    clear()
    p.displayProfile()

def main():
    clear()
    mainTitle()
    countryId = countrySelection()
    generateFakeId(countryId)
    print('\n')
    restart = input('Would you like to generate another fake ID ? (y/n) : ')
    while restart not in ['y','Y','n','N']:
        print(colors['red']+'Error ! This choice is not accepted !')
        restart = input(colors['white']+'Would you like to generate another fake ID ? (y/n) : ')
    return restart

restart = main()

while restart in ['y','Y']:
    restart = main()
clear()