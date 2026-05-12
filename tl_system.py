import random

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
