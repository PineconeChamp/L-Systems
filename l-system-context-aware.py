import random

def main():

    my_rules = {
        (('A',), 'B', ('C',)): ['A', 'A', 'B'],
        (('A',), 'A', ('B',)): ['B', 'C', 'D'],
        (('B',), 'C', ('D',)): ['D', 'C', 'A', 'B']
    }

    my_axiom = ['A', 'B', 'C']

    # Generate an l-system with 10 iterations
    for i in range(10):

        # Update the axiom
        my_axiom = lindenmayer_translation(my_rules, my_axiom)
    print(my_axiom)


def lindenmayer_translation(rules: dict, axiom: list):
    '''
    Rewrite the symbols within the axiom according to the rules
    '''

    # Create a nested list containing each symbol within the axiom
    translation = [[symbol] for symbol in axiom]

    # Iterate over the axiom
    for i, symbol in enumerate(axiom):

        # Iterate over the keys
        for key in rules:

            # Create contexts to the left and right of the current symbol
            left_context = axiom[i - len(key[0]): i]
            right_context = axiom[i + 1: i + 1 + len(key[-1])]

            # Check whether the current symbol and its contexts match the key
            if (tuple(left_context), symbol, tuple(right_context)) == key:

                # Rewrite the symbol
                translation[i] = rules[key]

    # Return flattened list
    return(sum(translation, []))

if __name__ == "__main__":
    main()