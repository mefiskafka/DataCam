# Define count_entries()
def ____(____, ____):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            ____
        # Else add the language to langs_count, set the value to 1
        else:
            ____

    # Return the langs_count dictionary
    

# Call count_entries(): result


# Print the result
print(result)
