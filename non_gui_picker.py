import json

# TODO: Fix role specificity like how Shaco only goes AP when he supports
# TODO: Add GUI
# TODO: add isCarry to roles.json

def main():
    search_criteria = None
    options = {
        "1": {
            "1": "top",
            "2": "mid",
            "3": "jungle",
            "4": "adc",
            "5": "support"
        },
        "2": {
            "1": 'ad',
            "2": 'ap'
        },
        "3": {
            "1": 'fullTank',
            "2": 'tanky'
        },
        "4": {
            "1": 'burst',
            "2": 'dps'
        }
    }
    while not criteria_is_valid(search_criteria):
        print("1: Lanes\n\t1: Top\n\t2. Mid\n\t3. Jungle\n\t4. ADC\n\t5. Support")
        print("2. Damage Type\n\t1. AD\n\t2. AP")
        print("3. Tankiness\n\t1. Very Tanky\n\t2. Bruiser")
        print("4. Burst / DpS\n\t1. Burst\n\t2. DpS")

        # Get search criteria
        search_criteria = get_search_criteria()

    roles = get_roles()
    filtered_champions = None
    for search in search_criteria:
        if search[0] == '1':
            results = roles['lane'][options['1'][search[1]]]
        elif search[0] == '2':
            results = roles['damageType'][options['2'][search[1]]]
        elif search[0] == '3':
            results = roles['tankiness'][options['3'][search[1]]]
        elif search[0] == '4':
            results = roles['carryType'][options['4'][search[1]]]

        if filtered_champions is None:
            filtered_champions = results
        else:
            filtered_champions = get_shared_values(filtered_champions, results)
    print(filtered_champions)

def get_shared_values(listA, listB):
    listA.sort()
    listB.sort()
    if min(listA[0], listB[0]) == listA[0]:
        first = listA
        second = listB
    else:
        first = listB
        second = listA
    i = 0 # Follows first
    j = 0 # Follows second
    while i < len(first) and j < len(second):
        # Keep elements if they are the same
        if first[i] == second[j]:
            i += 1
            j += 1
        # Remove element that is higher in the alphabet
        elif min(first[i], second[j]) == first[i]:
            del first[i]
        else:
            del second[j]
    # Return the list that has gotten to the end
    if i == len(first):
        return first
    else:
        return second


def get_roles():
    roles_files = champions_file = open("/Users/tannerlarson/Code/lol-champ-picker/roles.json", 'r').read()
    return json.loads(roles_files)


def criteria_is_valid(criteria):
    filters_used = set()
    if criteria is None:
        return False
    for c in criteria:
        print(c)
        # Ensure only one of each filter is used
        if c[0] in filters_used:
            return False
        filters_used.add(c[0])

        # Check filter category is good
        if not 0 < int(c[0]) < 5:
            return False
        # Check damage type, tankiness, and burst/dps is good
        if c[0] != '1' and not 0 < int(c[1]) < 3:
            return False
        # Check lanes is good
        if c[0] == '1' and not 0 < int(c[1]) < 6:
            return False
    return True


def get_search_criteria():
    search_criteria = None
    while not search_criteria:
        try:
            search_criteria = int(input("Input search criteria:\ni.e. Top, AD, DpS = 112142\n>"))
            print()
            if len(str(search_criteria)) % 2 != 0:
                search_criteria = None
                raise ValueError
        except ValueError:
            print()
            print("ONLY NUMBERS | NO SPACES | EVEN # DIGITS")
    search_criteria = str(search_criteria)
    split_length = 2
    search_criteria = [search_criteria[i:i+split_length] for i in range(0, len(search_criteria), split_length)]
    return search_criteria

if __name__ == "__main__":
    main()