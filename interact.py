### interact.py takes the command and makes a request to an api for a relevant reaction GIF then returns it to be sent as a response in Discord.
import discord
import requests
import json
from discord.ext import commands

def get_kiss():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=kiss")
  json_data = json.loads(response.text)
  kiss = str(json_data)
  kiss = kiss.replace("'url': ",'')
  kiss = kiss.replace('{','')
  kiss = kiss.replace('}','')
  kiss = kiss.replace("'",'')
  print (kiss)
  return kiss

def get_wave():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=wave")
  json_data = json.loads(response.text)
  wave = str(json_data)
  wave = wave.replace("'url': ",'')
  wave = wave.replace('{','')
  wave = wave.replace('}','')
  wave = wave.replace("'",'')
  print (wave)
  return wave

def get_poke():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=poke")
  json_data = json.loads(response.text)
  poke = str(json_data)
  poke = poke.replace("'url': ",'')
  poke = poke.replace('{','')
  poke = poke.replace('}','')
  poke = poke.replace("'",'')
  print (poke)
  return poke

def get_pat():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=pat")
  json_data = json.loads(response.text)
  pat = str(json_data)
  pat = pat.replace("'url': ",'')
  pat = pat.replace('{','')
  pat = pat.replace('}','')
  pat = pat.replace("'",'')
  print (pat)
  return pat
  
def get_wink():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=wink")
  json_data = json.loads(response.text)
  wink = str(json_data)
  wink = wink.replace("'url': ",'')
  wink = wink.replace('{','')
  wink = wink.replace('}','')
  wink = wink.replace("'",'')
  print (wink)
  return wink
  
def get_handhold():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=handhold")
  json_data = json.loads(response.text)
  handhold = str(json_data)
  handhold = handhold.replace("'url': ",'')
  handhold = handhold.replace('{','')
  handhold = handhold.replace('}','')
  handhold = handhold.replace("'",'')
  print (handhold)
  return handhold
  
def get_hug():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=hug")
  json_data = json.loads(response.text)
  hug = str(json_data)
  hug = hug.replace("'url': ",'')
  hug = hug.replace('{','')
  hug = hug.replace('}','')
  hug = hug.replace("'",'')
  print (hug)
  return hug
  
def get_nuzzle():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=nuzzle")
  json_data = json.loads(response.text)
  nuzzle = str(json_data)
  nuzzle = nuzzle.replace("'url': ",'')
  nuzzle = nuzzle.replace('{','')
  nuzzle = nuzzle.replace('}','')
  nuzzle = nuzzle.replace("'",'')
  print (nuzzle)
  return nuzzle
  
def get_cuddle():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=cuddle")
  json_data = json.loads(response.text)
  cuddle = str(json_data)
  cuddle = cuddle.replace("'url': ",'')
  cuddle = cuddle.replace('{','')
  cuddle = cuddle.replace('}','')
  cuddle = cuddle.replace("'",'')
  print (cuddle)
  return cuddle
  
def get_dance():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=dance")
  json_data = json.loads(response.text)
  dance = str(json_data)
  dance = dance.replace("'url': ",'')
  dance = dance.replace('{','')
  dance = dance.replace('}','')
  dance = dance.replace("'",'')
  print (dance)
  return dance
  
def get_celebrate():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=celebrate")
  json_data = json.loads(response.text)
  celebrate = str(json_data)
  celebrate = celebrate.replace("'url': ",'')
  celebrate = celebrate.replace('{','')
  celebrate = celebrate.replace('}','')
  celebrate = celebrate.replace("'",'')
  print (celebrate)
  return celebrate
  
def get_airkiss():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=airkiss")
  json_data = json.loads(response.text)
  airkiss = str(json_data)
  airkiss = airkiss.replace("'url': ",'')
  airkiss = airkiss.replace('{','')
  airkiss = airkiss.replace('}','')
  airkiss = airkiss.replace("'",'')
  print (airkiss)
  return airkiss
  
def get_lick():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=lick")
  json_data = json.loads(response.text)
  lick = str(json_data)
  lick = lick.replace("'url': ",'')
  lick = lick.replace('{','')
  lick = lick.replace('}','')
  lick = lick.replace("'",'')
  print (lick)
  return lick
  
def get_slap():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=slap")
  json_data = json.loads(response.text)
  slap = str(json_data)
  slap = slap.replace("'url': ",'')
  slap = slap.replace('{','')
  slap = slap.replace('}','')
  slap = slap.replace("'",'')
  print (slap)
  return slap
  
def get_smack():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=smack")
  json_data = json.loads(response.text)
  smack = str(json_data)
  smack = smack.replace("'url': ",'')
  smack = smack.replace('{','')
  smack = smack.replace('}','')
  smack = smack.replace("'",'')
  print (smack)
  return smack
  
def get_punch():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=punch")
  json_data = json.loads(response.text)
  punch = str(json_data)
  punch = punch.replace("'url': ",'')
  punch = punch.replace('{','')
  punch = punch.replace('}','')
  punch = punch.replace("'",'')
  print (punch)
  return punch
def get_pout():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=pout")
  json_data = json.loads(response.text)
  pout = str(json_data)
  pout = pout.replace("'url': ",'')
  pout = pout.replace('{','')
  pout = pout.replace('}','')
  pout = pout.replace("'",'')
  print (pout)
  return pout
def get_blush():
  response = requests.get("https://api.otakugifs.xyz/gif?reaction=blush")
  json_data = json.loads(response.text)
  blush = str(json_data)
  blush = blush.replace("'url': ",'')
  blush = blush.replace('{','')
  blush = blush.replace('}','')
  blush = blush.replace("'",'')
  print (blush)
  return blush
