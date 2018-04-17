"""All about IO."""


import json
import os
import requests
import inspect
import sys
from bs4 import BeautifulSoup
import time


# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print("Be careful that your relative paths are")
    print("relative to where you think they are")
    print("LOCAL", LOCAL)
    print("CWD", CWD)



def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatenate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indices for lists, and named keys for
         dictionaries.
    """
    json_data = open(LOCAL + "/lazyduck.json").read()
    data = json.loads(json_data)
    lastName = data["results"][0]["name"]["last"]

    password = data["results"][0]["login"]["password"]

    postcode = data["results"][0]["location"]["postcode"]
    id = data["results"][0]["id"]["value"]
    postcodePlusID = int(postcode) + int(id)

    return {"lastName":       lastName,
            "password":       password,
            "postcodePlusID": postcodePlusID
                        }



def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=10&maxLength=10&limit=1
    The arguments that the generator takes is the minLength and maxLength of the word
    as well as the limit, which is the the number of words. 
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep", 3
    "dwine",5
    "tenoner",7
    "ectomeric",8
    "archmonarch",11
    "phlebenterism",13
    "autonephrotoxin",15
    "redifferentiation",17
    "phytosociologically",19
    "theologicohistorical",20
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &minLength=
    """
    url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=3&maxLength=20&limit=1"
    #r = requests.get(url)
    #data = BeautifulSoup(r.content)

    '''result_list = []
    for i in range (9):

        print(i)

        length = 2*i+3
        url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=" + str(length) + "&maxLength=" + str(length) + "&limit=1"
        r = requests.get(url)
        data = BeautifulSoup(r.content)
        #print(data[0]["word"])
        result_list.append(data[0]["word"])'''
    pyramid1 = []
    pyramid2 = []
    url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength={}&maxLength={}&limit=1"
    for length in range(3, 21):
        if length % 2 == 1:
            pyramid1.append(requests.get(url.format(length, length)).json()[0]['word'])
        else:
            pyramid2 = [requests.get(url.format(length, length)).json()[0]['word']] + pyramid2

    return pyramid1 + pyramid2

    ''' 
    for i in range (9):
        length = 20 - i*2
        url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=" + str(length) + "&maxLength=" + str(length) + "&limit=1"
        r = requests.get(url)
        data = BeautifulSoup(r.content)
        #print(data[0]["word"])
        result_list.append(data[0]["word"])
    '''
    return result_list





def wunderground():
    """Find the weather station for Sydney.

    Get some json from a request parse it and extract values.
    Sign up to https://www.wunderground.com/weather/api/ and get an API key
    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    base = "http://api.wunderground.com/api/"
    api_key = "YOUR KEY - REGISTER TO GET ONE"
    country = "AU"
    city = "Sydney"
    template = "{base}/{key}/conditions/q/{country}/{city}.json"
    url = template.format(base=base, key=api_key, country=country, city=city)
    r = requests.get(url)
    the_json = json.loads(r.text)
    obs = the_json['current_observation']

    return {"state":           obs["display_location"]["state"],
            "latitude":        obs["display_location"]["latitude"],
            "longitude":       obs["display_location"]["longitude"],
            "local_tz_offset": obs["local_tz_offset"]}


def diarist():
    
    """Read gcode and find facts about it. 

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the week4 directory.
    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    """

    count = 0
    laser_file = 'Trispokedovetiles(laser).gcode'
    with open(laser_file, 'r') as laser:
        commands = laser.read().split('\n')
        for command in commands:
            if "M10 P1" in command:
                count += 1

    pew_file = 'lasers.pew'
    with open(pew_file, 'w') as pew:
        pew.write(str(count))
    return count
    
    

if __name__ == "__main__":
    functions = [obj for name,obj in inspect.getmembers(sys.modules[__name__]) if (inspect.isfunction(obj))]
    for function in functions:
        try:
            print(function())
        except Exception as e:
            print(e)
    if not os.path.isfile("lasers.pew"):
        print('diarist did not create lasers.pew')
