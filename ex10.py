tabby_cat = "\tI'm tabbed in. "
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

trying = """ \a ASCII Bell\n\b Backspace \n\f Formfeed \n\r carriage return
         \n\v  Vertical tab"""

last_one = ''' why is "this" bad? \n I don't understand''' + ''' I'm \\ a \\ cat '''
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(trying)
print(last_one)
