"""
Introduction to Programming: Coursework 1
Please write your name
@author: James Schwar

"""

# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None:
    
    
    pass


def valid_puzzle(puzzle: list) -> bool:
    valid = True # initial boolean declaration, before proceeding to run tests to invalidate if necessary
    tmp = len(puzzle[0]) # inital int variable of first string's length to 
    for i in puzzle: # iterate through puzzle list using 'i' as identifier
        if tmp != len(i): # tmp compared with length of string, index varies with i  
            valid = False # if not equal, set valid to false. the puzzle is not valid 
    return valid # passes value of valid back to function 

def valid_wordlist(wordlist: list) -> bool:
    valid = True
    for i in wordlist: # iterate through wordlist with 'i' 
        if not isinstance(i, str): # isinstance - builtin function that returns true if the given variable 'i' in list is a string  
            valid = False
    return valid


def get_positions(puzzle: list, word: str) -> list: #WHY DOES FULLLIST EMPTY ITSELF 
    
    first_letter = word[0] # assign first letter of work to string variable to compare later 
    word_length = len(word) # assign word length to int variable for readability
    
    full_list = [] # list declaration that stores tuple list of coordinates

    for y, y_val in enumerate(puzzle): # enumberate function assigns a stepper variable y and a string variable y_val of the corresponding value returned in the array. 

        for x, x_val in enumerate(y_val): # x_val refers to char within string, y_val refers to the string

            if first_letter == x_val: # only searches for adjacent tiles when finding matchin first letter, ignores otherwise for efficiency

                tmp = [] # list structure declared to append coordinates to
                tmp.append((x,y)) # append coordinate values of first list structure

                # same iterative structure used in eight directions 

                # going north - decrementing y variable  
                
                for p in range(1, word_length): # p increments from 1 as the first coordinate x,y has already been written to the list 
                    
                    if y-p >= 0: # y cannot be decremented below index 0 (top side) or error is thrown 
                        # accessing char along 2d list requires 'y-coordinate' pointer first, followed by 'x-coordinate'
                        current_char = puzzle[y-p][x] # assigned to specific variable name for readability and reusability
                        current_coords = (x, y-p) # declare tuple for appending to list

                        if current_char == word[p]: # p additionally funcitons as an index pointer for the 'word' string, corresponding with expected char in the grid 

                            tmp.append(current_coords) # append current coordinates to tmp 

                            if len(tmp) == word_length: # number of coordinates in the list must equal the number of characters, 
                                full_list.append(tmp) # ..so word has been found. append the coordinate list to the full list.
                                
                        else: # adjacent char does not match the next letter in the word, search has failed
                            tmp.clear() # so the list must be emptied for next search 
                            break # exit forloop early

                    else: # boundary check failed, adjacent element in list is null so word cannot be found. 
                        tmp.clear() 
                        break 

                # going north-east - decrementing y, incrementing x

                tmp.append((x,y)) # tmp has been cleared from failing the search from the past iteration so the initial coordinate must be appended again. 
                for p in range(1, word_length): 
                    
                    if y-p >= 0 and x+p < len(y_val): # y_val is a string that len() can be applied to reflect the horizonal length of the grid, of which the x index cannot exceed  
                    
                        current_char = puzzle[y-p][x+p]
                        current_coords = (x+p, y-p)

                        if current_char == word[p]:

                            tmp.append(current_coords)

                            if len(tmp) == word_length: 
                                full_list.append(tmp)
                                
                        else: 
                            tmp.clear() 
                            break

                    else: 
                        tmp.clear()
                        break

                # going east - incrementing x
                tmp.append((x,y))
                for p in range(1, word_length): 
                    
                    if x+p < len(y_val):  
                        
                        current_char = puzzle[y][x+p]
                        current_coords = (x+p, y)  

                        if current_char == word[p]:
                            
                            tmp.append(current_coords)

                            if len(tmp) == word_length: 
                                full_list.append(tmp)
                                
                        else:                        
                            tmp.clear()
                            break

                    else:                    
                        tmp.clear()
                        break 

                # going south-east - incrementing y, incrementing x
                tmp.append((x,y))
                for p in range(1, word_length): 
                    
                    if x+p < len(y_val) and y+p < len(puzzle):  # if both x and y are being iterated upon, the and operator is used to check for both simultaneously
                        
                        current_char = puzzle[y+p][x+p]
                        current_coords = (x+p, y+p)  

                        if current_char == word[p]:
                            
                            tmp.append(current_coords)

                            if len(tmp) == word_length: 
                                full_list.append(tmp)
                                
                        else: 
                            tmp.clear()
                            break

                    else: 
                        tmp.clear()
                        break

                # going south - incrementing y variable (this is where TRAY should be returned starting from coords (2,7))
                tmp.append((x,y))
                for p in range(1, word_length): 

                    if y+p < len(puzzle): # len(puzzle) refers to the number of rows which can be used to ensure the y index not exceeding it
                        
                        current_char = puzzle[y+p][x]
                        current_coords = (x, y+p)
                        
                        if current_char == word[p]:

                            tmp.append(current_coords)

                            if len(tmp) == word_length:
                                a = tmp 
                                full_list.append(a) ################################################################################
                                print("appendnign")
                                print(full_list)
                                
                        else: 
                            tmp.clear() 
                            break

                    else: 
                        tmp.clear()
                        print("fuckup")
                        break 

                print("after loop")
                print(full_list)

                # going south-west - incrementing y, decrementing x
                tmp.append((x,y))
                for p in range(1, word_length): 
                    
                    if x-p >= 0 and y+p > len(puzzle):  
                        
                        current_char = puzzle[y+p][x-p]
                        current_coords = (x-p, y+p)  
                        if current_char == word[p]:
                            
                            tmp.append(current_coords)

                            if len(tmp) == word_length: 
                                full_list.append(tmp)
                                
                        else: 
                            tmp.clear()
                            break

                    else: 

                        tmp.clear()
                        break

                # going west - decrementing x
                tmp.append((x,y))
                for p in range(1, word_length):

                    if x-p >= 0:

                        current_char = puzzle[y][x-p]
                        current_coords = (x-p, y)

                        if current_char == word[p]:

                            tmp.append(current_coords)

                            if len(tmp) == word_length:
                                full_list.append(tmp)

                        else:
                            tmp.clear()
                            break

                    else:
                        tmp.clear()
                        break

                #going north-west - decrementing y, decrementing x
                tmp.append((x,y))
                for p in range(1, word_length):

                    if x-p >= 0 and y-p >= 0:

                        current_char = puzzle[y-p][x-p]
                        current_coords = (x-p, y-p)

                        if current_char == word[p]:

                            tmp.append(current_coords)

                            if len(tmp) == word_length:
                                full_list.append(tmp)

                        else:
                            tmp.clear()
                            break

                    else:
                        tmp.clear()
                        break

    
    
    if len(full_list) > 0: # if elements present in full list, at least one occurence of word is present
        return full_list # so return list
    else: # if no elements present
        return "'{0}' not found.".format(word) # return statement indicating given word is not found
                




    


def basic_display(grid: list) -> None:
    tmp = ""
    for i in grid:
        for k in i:
            tmp += k + " "
        tmp = tmp[:-1]
        tmp += "\n"
    print(tmp)
    return tmp
        



def coloured_display(grid: list, positions: list) -> None:
    
    pass
    for i in list:
        for k in i:
            tmp = [index(i), index(k)] 
            # if in positions list 
            


# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "TRAY"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
    # test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # full solution
    # test_coloured_display()
    test_get_positions()
    # test_wordsearch()
