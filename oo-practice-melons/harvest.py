############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing: list):
        """Add a food pairing to the instance's pairings list."""
        # self.pairings.append(pairing)
        self.pairings.extend(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    muskmelon = MelonType('musk', 1998, 'green', 'seedless', True, 'Muskmelon')
    muskmelon.add_pairing(["mint"])

    casaba = MelonType('cas', 2003, 'orange', 'seeds', False, 'Casaba')
    casaba.add_pairing(["mint", "strawberry"])

    crenshaw = MelonType("cren", 1996, "green", "seeds", False, "Crenshaw")
    crenshaw.add_pairing(["prosciutto"])

    yellow_watermelon = MelonType("yw", 2013, "yellow", "seeds", True, "Yellow Watermelon")
    yellow_watermelon.add_pairing(["ice cream"])
    
    return [muskmelon, casaba, crenshaw, yellow_watermelon]


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with ")
        for pairing in melon.pairings:
            print(f"-{pairing}")
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon
    return melon_dict


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(
        self, melon_type, shape_rating, color_rating, field, harvester
    ):
        """Initialize a melon."""
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
    
    def is_sellable(self, melon, min_color, min_shape, bad_fields: list):
        # if melon.color_rating > min_color and melon.shape_rating > min_shape and melon.field not in bad_fields:
        #     return True
        # return False

        if melon.color_rating > min_color and melon.shape_rating > min_shape and melon.field not in bad_fields:
            return "Is Sellable"
        return "Not Sellable"
        


def make_melons():
    """Returns a list of Melon objects."""
    
    # Fill in the rest
    melon1 = Melon('yw', 8, 7, 2, 'Sheila')
   

    
    return [melon1]


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        sellable = melon.is_sellable(melon, 5,8,[3])
        print(f'Harvested by {melon.harvester} from Field {melon.field}, Sellable: {sellable}')