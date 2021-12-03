"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # species = set()

    # TODO: replace this with your code
    my_list = list(filename)
    
    species_list = []
    for item in my_list:
      index = item.split("|")
      species_list.append(index[1])
    
    species_set = set(species_list)
    print(species_set)
    # species = set(filename)
    # print(species)
    return species_set

# all_species(open("villagers.csv"))


def get_villagers_by_species(filename, species="All"):
    """Return a list of villagers' names by species.

    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list[list]: a list of lists
    """

    villagers = []

    # TODO: replace this with your code
    my_list = list(filename)
    for villager in my_list:
      index = villager.split("|")
      if species == "All":
        villagers.append(index[0])
      elif species == index[1]:
        villagers.append(index[0])
    print(sorted(villagers))
    return sorted(villagers)

# get_villagers_by_species(open("villagers.csv"), "Bear")

def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    # TODO: replace this with your code
    Hobbies = []
    Fitness = []
    Nature = []
    Education = []
    Music = []
    Fashion = []
    Play = []

    my_list = list(filename)
    for villager in my_list:
      index = villager.split("|")
      if index[3] == "Fitness":
        Fitness.append(index[0])
      elif index[3] == "Nature":
        Nature.append(index[0])
      elif index[3] == "Education":
        Education.append(index[0])
      elif index[3] == "Music":
        Music.append(index[0])
      elif index[3] == "Fashion":
        Fashion.append(index[0])
      elif index[3] == "Play":
        Play.append(index[0])
    Hobbies.append(sorted(Fitness))
    Hobbies.append(sorted(Nature))
    Hobbies.append(sorted(Education))
    Hobbies.append(sorted(Music))
    Hobbies.append(sorted(Fashion))
    Hobbies.append(sorted(Play))
    print(Music)
    return sorted(Hobbies)

all_names_by_hobby(open("villagers.csv"))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, name):
    """Return a set of villagers with the same personality as the given villager."""

    # TODO: replace this with your code

