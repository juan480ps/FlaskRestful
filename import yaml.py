import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('/home/juanc/Escritorio/Scripts/FlaskRestful/postgresconfig.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)

for section in data:
    print(section)
    
print(data["mysql"])
print(data["other"])