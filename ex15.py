from sys import argv

script, filename = argv

txt = open(filename)

print "please make sure you make the file /etc/passwd"

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = filename

txt_again = open(file_again)

print txt_again.read()
