def intersection(arrays):
    
    # Create an empty hashtable
    table = {}

    # Put all items in first array into a hastable, with value of 1
    for item in arrays[0]:

        # How many times item is in table
        table[item] = 1

    # For all arrays after the first
    for array in arrays[1:]:

        # For each item in array
        for item in array:

            # If the item is in hashtable already
            if item in table:

                # Increment
                table[item] += 1
            
            # if not
            else:

                # Ignore
                pass

    # Create empty intersection list 
    in_every_array = []

    # For each key in our hashtable
    for key in table:

        # If it is in every array
        if table[key] == len(arrays):

            # Append to our intersection list
            in_every_array.append(key)
    
    # Return items where all lists intersect
    return in_every_array



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
