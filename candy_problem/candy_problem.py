'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def get_friends_favorite_candy_count(favorites):
    candy_count = {}
    candy_index = 1
    for friend in favorites:
        candy_list = friend[candy_index]
        for candy in candy_list:
            if candy not in candy_count:
                candy_count[candy] = 1
            else:
                candy_count[candy] += 1
    return candy_count


'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_new_candy_data_structure(data):
    candy_people = {}
    for friend in data:
        friend_name = friend[0]
        candies = friend[1]
        for candy in candies:
            if candy not in candy_people:
                candy_people[candy] = []
            candy_people[candy].append(friend_name)
    return candy_people


'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
'''
def get_friends_who_like_specific_candy(data, candy_name):
    candies = create_new_candy_data_structure(data)
    return tuple(candies[candy_name])


'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.
'''
def create_candy_set(data):
    candies_dict = create_new_candy_data_structure(data)
    all_candies = []
    for candy in candies_dict:
        all_candies.append(candy)
    return set(all_candies)


'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''
