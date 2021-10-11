import yaml;

f = open('./details.yaml');
data = yaml.load(f, Loader=yaml.FullLoader)
print(data)


file = open(r'./feed.yaml');
fruits_list = yaml.load(file, Loader=yaml.FullLoader)

print(fruits_list)

dict_file = [{'sports' : ['hockey', 'rugby', 'tennis', 'ping pong', 'football', 'badminton']},
{'countries' : ['Jamaica', 'England', 'Nepal', 'Netherlands', 'South Africa', 'Bolivia', 'Portugal']}]

with open(r'C:\data.yaml', 'w') as file: #create a new yaml file 
    data = yaml.dump(dict_file, file)