import random

def main():

    my_rules = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A']
    }
    my_rules2 = {
        'A': ['C'],
        'B': ['A', 'C'],
        'C': ['B']
    }

    my_rules_table = [my_rules, my_rules2]
    my_axiom = ['A']

    # Generate an l-system with 10 iterations
    for i in range(10):

        # Update the axiom
        my_axiom = lindenmayer_translation(random.choice(my_rules_table), my_axiom)
    print(my_axiom)


def lindenmayer_translation(rules: dict, axiom: list):
    '''
    Rewrite the symbols within the axiom according to the rules
    '''

    # Create a nested list containing each symbol within the axiom
    translation = [[symbol] for symbol in axiom]

    # Iterate over the axiom
    for i, symbol in enumerate(axiom):

        # Check whether there is a rule for the symbol
        if symbol in rules.keys():

            # Rewrite the symbol
            translation[i] = rules[symbol]

    # Return flattened list
    return(sum(translation, []))

if __name__ == "__main__":
    main()