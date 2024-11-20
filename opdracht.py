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
time.sleep(random.randint(1, 3))
#patterns voor responses/dictionary

patterns = {
  "Ik heb last van (.*)":"Als je last heb van {} is het beste wat je kan doen, of zelf een oplossing zoeken op het internet, ik zou zorgvisie.nl aanbevelen, of als u veel last heeft de huisarts bellen.", 
  "Ik zou hulp willen met (.*)": "Hoe kan ik je helpen met {}.",
  "Ik voel me (.*)": "hoelang voel je je {}?",
  "Al (.*) lang": "{} is een lange tijd, als je een van de volgende klachten heb zou ik een dokter raadplegen: benauwd zijn, suf voelen, verward zijn of steeds zieker worden ",
  "Ik zou hulp willen met (.*)": "Hoe kan ik je helpen met {}.",
  "De pijn komt van (.*)": "Oke je hebt dus pijn aan je {} dan zou ik even gaan kijken op het internet wat je er aan kan doen.",
  "(.*)kattenfeitje(.*)": get_cat_fact()
}

#dictionary
responses = {
  "Hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "Bedankt": ["Geen probleem, word snel beter!"],
  "Het gaat beter": ["Goed om te horen!", "Wat fijn!"],
  "Het gaat goed": ["Mooi!"],
  "Ik heb pijn": ["oei, waar komt die pijn vandaan?"]
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