# Defines this string formatting object
formatter = "%r %r %r %r"

# And then formats in these values.

# Digits don't require quotes.
print formatter % (1, 2, 3, 4)

# Strings do.
print formatter % ("one", "two", "three", "four")

# Boolean values don't.
print formatter % (True, False, False, True)

# This one treats the original definition as a string because no values are defined for the %r's
print formatter % (formatter, formatter, formatter, formatter)

# This one just has strings, but I don't understand why the third %r prints with double quotes rather than single, like the others.
# Or vice versa, for that matter.
print formatter % (
	"I had this thing,",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
