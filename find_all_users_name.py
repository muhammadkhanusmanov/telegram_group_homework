from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    a=[]
    for i in data['messages']:
        if 'actor' in i.keys():
            a.append(i['actor'])

    return list(set(a))
d=read_data('data/result.json')
print(find_all_users_name(d))
