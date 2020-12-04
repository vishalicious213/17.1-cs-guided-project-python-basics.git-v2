"""
Challenge #8:

Create a function that returns the number of arguments it was called with.

Examples:
- num_args() ➞ 0
- num_args("foo") ➞ 1
- num_args("foo", "bar") ➞ 2
- num_args(True, False) ➞ 2
- num_args({}) ➞ 1
"""
def num_args(*args, arg2):
    # Your code here
    print(len(args))
    print(arg2)
    return

num_args("foo", "bar", arg2='this is a keyword arg')
# num_args("foo")

# the arguments in the parenthesis in a specific location are called "positional arguments"
# named/keyword-only arguments look like props. They're key/value pairs.
# adding an asterisk in the parenthesis for a function lets it take unlimited arguments
# kwargs = keyword arguments

# "*args passes variable number of non-keyworded arguments, **kwargs passes variable number of keyword arguments"