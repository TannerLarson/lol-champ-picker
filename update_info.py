import json


# TODO: Add AD/AP to json file
# TODO: Make JSON of Good Champions


def main():
    champions_file = open("/Users/tannerlarson/Code/lol-champ-picker/champions.json", 'r').read()
    champions_json = json.loads(champions_file)
    champ_dict = make_nice_dictionary_by_name(champions_json)
    champions_organized_json = json.dumps(champ_dict)
    export_dictionary(champions_organized_json, "champions-dict.json")


def export_dictionary(dict_to_export, file_to_write):
    new_champions_file = open(file_to_write, 'w')
    new_champions_file.write(dict_to_export)
    new_champions_file.close()


def make_nice_dictionary_by_name(champions):
    nice_dict = {}
    for champion in champions:
        nice_dict[champion['id']] = {
            'key': champion['key'],
            'name': champion['name'],
            'title': champion['title'],
            'tags': champion['tags'],
            'stats': champion['stats'],
            'icon': champion['icon'],
            'sprite': champion['sprite'],
            'description': champion['description']
        }
    return nice_dict


if __name__ == "__main__":
    main()
