import json

with open('cfg.json','r') as file:
    config = json.load(file)

config['Graphic'] = 'High'
config['Sound']['BGM'] = 0.5

with open('cfg.json','w') as file:
    json.dump(config,file)