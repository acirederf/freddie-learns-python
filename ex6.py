# Defines a variable as a string with a digit formatted into it.
x = "There are %d types of people." % 10
# Defines a variable.
binary = "binary"
# And another.
do_not = "don't"
# defines another variable as a string with a punchline formatted into it.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Prints two strings overexplaining itself. Har har.
print "I said: %r." % x
print "I also said: '%s'." % y 

# Defines a variable as False
hilarious = False
# Defines a variable as a string with a raw value to be formatted in.
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints the above phrase and a negative value judgement
print joke_evaluation % hilarious

# Defines two strings...
w = "This is the left side of..."
e = "a string with a right side."

# ...And prints them together.
print w + e
