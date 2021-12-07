"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices, melons


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


print(melons.items())
for att, val in melons.items():
    print(att)
    for att, val in val.items():
        print(f"    {att}: {val}")
        
    

    