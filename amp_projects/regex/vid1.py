#way of describing patterns within search strings

#validating emails, credit card, find replace, formatting text

(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

# regex syntax
# \d digit 0-9
# \w letter digit or underscore
# \s whitespace character inc new line
# \D not a digit
# \W not a word character
# \S not a whitespace character
# . any character except line break

#quantifiers
# + one or more
# {3} exactly x times 
# {3,5} 3 to 5 times
# {4,} four or more times
# * zero or more times
# ? once or none (optionals)

#character class
# []
# [^]

# anchors and boundaries
# ^ start of string or line
# $ end of string or line
# \b word boundary