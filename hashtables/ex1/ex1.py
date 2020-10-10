def get_indices_of_item_weights(weights, length, limit):
    # Create empty hashtable 
    table = {}

    # Enumerate weight list 
    for index, value in enumerate(weights):

        # If hashtable contains an entry for the weight limit - the current weight value 
        if limit - value in table: 

            # Get the index of that second value 
            pair = table.get(limit-value), index 
            return tuple(sorted(pair, reverse=True))

        # If not in hashtable 
        else: 

            # Create entry 
            table[value] = index

    return None