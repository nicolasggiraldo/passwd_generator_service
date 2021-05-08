"""
Random Password Generator using Python
Based on the code of: https://github.com/ayushi7rawat/Youtube-Projects/tree/master/Random%20Password%20Generator
"""

import random
import string


def password_generator(length=10):

    # define data
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    # combine the data
    all_strings = lower + upper + num + symbols

    # use random
    temp = random.sample(all_strings, length)

    # create the password
    password = "".join(temp)

    # return the password
    return password
