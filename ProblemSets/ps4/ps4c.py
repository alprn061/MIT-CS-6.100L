# Problem Set 4C
# Name:
# Collaborators:

import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(r" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("ProblemSets/ps4/story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('ProblemSets/ps4/pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'ProblemSets/ps4/words.txt'
### END HELPER CODE ###
words = load_words(WORDLIST_FILENAME)

def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    # initialize best score
    best_score = 0
    #initialize best pad
    best_pad = None
    # initialize best decryption
    best_decryption = ""
    for pad in pads:
        # pad = [1,2,3,6,8], [3,3,2,5,6], ...
        # decrypt the message with looping pad
        result = ciphertext.decrypt_message(pad).get_text()
        # split the result into words 
        words_in_result = result.split()
        # calculalte how many valid word is generated
        valid_count = sum(is_word(words, w) for w in words_in_result)

        if valid_count >= best_score:   # choose most valid word generated
            best_score = valid_count
            best_decryption = result 
            best_pad = pad
    return ps4b.PlaintextMessage(best_decryption, best_pad)


def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story
    '''
    # initialize best score
    best_score = 0
    #initialize best pad
    best_pad = None
    # best story
    best_story = None

    for pad in get_story_pads():
        # pad = [1,2,3,6,8], [3,3,2,5,6], ...
        # initialize encyrepted story
        encrypted_story = ps4b.EncryptedMessage(get_story_string())
        # decrypt the story with looping pad
        result = encrypted_story.decrypt_message(pad).get_text()
        # split the story into words
        words_result = result.split()
        # calculalte how many valid word is generated
        valid_count = sum(is_word(words, w) for w in words_result)


        # check if valid_count greater than best_score
        if valid_count >= best_score:
            best_score = valid_count
            best_pad = pad
            best_story = result
    return best_story




if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
    # print(len(get_story_string()), [len(i) for i in get_story_pads()])