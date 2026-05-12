from tl_system import lindenmayer_translation
from turtle_engine import draw_thing
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
    
    branch_count = 50

    all_axioms = []

    # Create l-systems for each branch
    for _ in range(branch_count):
        my_axiom = ['A']
        # Generate an l-system with 10 iterations

        for __ in range(10):
            # Update the axiom
            my_axiom = lindenmayer_translation(random.choice(my_rules_table), my_axiom)

        all_axioms.append(my_axiom)

    draw_thing(all_axioms, branch_count)

if __name__ == "__main__":
    main()