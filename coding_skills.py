import json


def read_json():
    dic = {'C++': ['', 0], 'PHP': ['', 0], 'Python': ['', 0], 'C#': ['', 0], 'Haskell': ['', 0], 'Java': ['', 0], 'JavaScript': ['', 0], 'Ruby': ['', 0],'CSS': ['', 0],'C': ['', 0]}
    with open('data.json', 'r') as f:
        data = json.load(f)
        for dude in data['people']:
            ime = dude['first_name']
            lastime = dude['last_name']
            for item in dude['skills']:
                if item['level'] > dic[item['name']][1]:
                    dic[item['name']][0] = ime + " " + lastime
                    dic[item['name']][1] = item['level']

    return dic



print(read_json())
