import json

config = None

def loadConfig():
  with open('../config.json') as f:
    global config
    config = json.load(f)

def getConfig(key):
    global config
    api_key = config.get(key)
    return api_key