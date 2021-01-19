import json
import copy

# TODO: Fix role specificity like how Shaco only goes AP when he supports
# TODO: Add GUI
# TODO: Add chestAcquired to roles.json
# TODO: Add bruiser and enchanter to function in roles.json
# TODO: Allow selection of multiple sub-categories

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
            "2": 'dps',
            "3": 'bruiser',
            "4": 'utility'
        }
    }
    while not criteria_is_valid(search_criteria):
        print("1: Lanes\n\t11: Top\n\t12. Mid\n\t13. Jungle\n\t14. ADC\n\t15. Support")
        print("2. Damage Type\n\t21. AD\n\t22. AP")
        print("3. Tankiness\n\t31. Very Tanky\n\t32. Bruiser")
        print("4. Funcionality\n\t41. Burst\n\t42. DpS\n\t43. Bruiser\n\t44. Utility")

        # Get search criteria
        search_criteria = get_search_criteria()

    roles = get_roles()
    filtered_champions = get_filtered_champions(search_criteria, roles, options)
    print("Options:")
    for champ in filtered_champions:
        print(champ)

def get_filtered_champions(search_criteria, roles, options):
    filtered_champions = None
    for search in search_criteria:
        if search[0] == '1':
            results = roles['lane'][options['1'][search[1]]]
        elif search[0] == '2':
            results = roles['damageType'][options['2'][search[1]]]
        elif search[0] == '3':
            results = roles['tankiness'][options['3'][search[1]]]
        elif search[0] == '4':
            results = roles['function'][options['4'][search[1]]]

        if filtered_champions is None:
            filtered_champions = results
        else:
            filtered_champions = get_shared_values(filtered_champions, results)

    return filtered_champions

def get_shared_values(listA, listB):
    listA.sort()
    listB.sort()
    if min(listA[0], listB[0]) == listA[0]:
        first = copy.deepcopy(listA)
        second = copy.deepcopy(listB)
    else:
        first = copy.deepcopy(listB)
        second = copy.deepcopy(listA)
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

def get_different_values(listA, listB):
    diff = listA + listB
    num_occurances = {}
    for element in diff:
        if element not in num_occurances:
            num_occurances[element] = 1
        else:
            num_occurances[element] += 1
    for key, value in num_occurances.items():
        if value > 1:
            while key in diff:
                diff.remove(key)
    return diff

def get_roles():
    roles_files = champions_file = open("/Users/tannerlarson/Code/lol-champ-picker/roles.json", 'r').read()
    return json.loads(roles_files)


def criteria_is_valid(criteria):
    if criteria is None:
        return False
    for c in criteria:
        subcategory = int(c[1])
        # Check filter category is good
        if not 0 < int(c[0]) < 5:
            return False
        # Lane
        if c[0] == '1' and not is_between(0, subcategory, 6):
            return False
        # Damage type
        if c[0] == '2' and not is_between(0, subcategory, 3):
            return False
        # Tankiness
        if c[0] == '3' and not is_between(0, subcategory, 3):
            return False
        # Functionality
        if c[0] == '4' and not is_between(0, subcategory, 5):
            return False
    return True

def is_between(left, middle, right):
    return left < middle < right


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