import json


def main():
    champions_file = open("/Users/tannerlarson/Code/lol-champ-picker/champions.json", 'r').read()
    champions_json = json.loads(champions_file)
    print(champions_json[1])
    champions_organized = {}
    for champion in champions_json:
        print(champion['id'])
        champions_organized[champion['id']] = {
            'key': champion['key'],
            'name': champion['name'],
            'title': champion['title'],
            'tags': champion['tags'],
            'positions': champion['positions'],
            'stats':  champion['stats'],
            'icon': champion['icon'],
            'sprite': champion['sprite'],
            'description': champion['description'],
        }
    champions_organized_json = json.dumps(champions_organized)
    new_champions_file = open("json-nicer.json", 'w')
    new_champions_file.write(champions_organized_json)
    new_champions_file.close()

if __name__ == "__main__":
    main()