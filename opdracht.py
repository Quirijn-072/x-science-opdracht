#imports om bepaalde dingen te doen.
import re 
import random
import time
import json
import urllib.request

#catfact
def get_cat_fact():
  url = 'https://meowfacts.herokuapp.com/'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  cat_facts = result["data"]
  cat_fact = cat_facts[0]
  
  return cat_fact

#verschillende tijden voor antwoorden.
time.sleep(random.randint(2, 4, 3))
#patterns voor responses/dictionary

patterns = { 
   "Ik wil (.*)":"Waarom wil je dat doen? Kan ik je daarbij helpen, met {}", 
   "Ik voel me (.*)":"Waarom voel jij je {}, als je je zo voelt kan ik je opvrolijken met een kattenfeitje!",
   "Ik zou hulp willen met (.*)": "Hoe kan ik je helpen met {}.",
    "(.*)kattenfeitje(.*)": get_cat_fact()
    " (.*)"
    
    
}
#dictionary
responses = {
  "Hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "Het gaat goed": ["Goed om te horen!", "toppie!"]
  "Het gaat slecht":["ohh dat is niet zo fijn, hoe kan ik je oprvrolijken, waarom is dat zo?"]
  

}


def get_response(message):


  for pattern in patterns: 
    match = re.search(pattern, message) 
    if match:
      return patterns[pattern].format(match.group(1))

  if message in responses: 
    return random.choice(responses[message]) 
  else:
    return "Ik begrijp je niet."

while True:
  message = input("U: ")
  response = get_response(message)
  print("Bot: " + response)