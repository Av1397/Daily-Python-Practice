# Provided any given word or sentence, the program will return nato alpha value for each alphabets


# ADD NATO ALPHABETS in a dictionary format

nato_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'Xray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}


def nato(provided_str):

    modified_string = provided_str.upper()
    final_list = []

    for i in range(len(modified_string)):

        if modified_string[i].isalpha():

            final_list.append(nato_alphabet[modified_string[i]])

        else:
            final_list.append(None)

    return final_list





