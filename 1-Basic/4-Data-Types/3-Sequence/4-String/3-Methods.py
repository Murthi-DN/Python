
#capitalize()
"""It returns a copy of the string with only its first character capitalized"""

str = "this is string example....wow!!!"
print(str.capitalize())

#center()
"""The method center() returns centered in a string of length width. Padding is done using
the specified fillchar."""

print (str.center(40, 'a'))

#count()
"""The count() method returns the number of occurrences of substring sub in the range
[start, end]."""

str="this is string example....wow!!!"
sub='i'
print (str.count(sub))
sub='exam'
print(str.count(sub,10,40))

#endswith()
#It returns True if the string ends with the specified suffix

Str='this is string example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='exam'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))

#find()
"""The find() method determines if the string str occurs in string, or in a substring of string
if the starting index beg and ending index end are given."""

str1 = "this is string example....wow!!!"
str2 = "exam";
print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))

#index()
"""The index() method determines if the string str occurs in string or in a substring of string,
if the starting index beg and ending index end are given. This method is same as find(),
but raises an exception if sub is not found."""

str1 = "this is string example....wow!!!"
str2 = "exam";
print (str1.index(str2))
print (str1.index(str2, 10))


#isalnum()
#The isalnum() method checks whether the string consists of alphanumeric characters

str = "this2016" # No space in this string
print (str.isalnum())
str = "this is string example....wow!!!"
print (str.isalnum())

#isalpha()
#The isalpha() method checks whether the string consists of alphabetic characters only
str = "this"; # No space & digit in this string
print (str.isalpha())
str = "this is string example....wow!!!"
print (str.isalpha())

#isdigit()
#The method isdigit() checks whether the string consists of digits only.

str = "123456"; # Only digit in this string
print (str.isdigit())
str = "this is string example....wow!!!"
print (str.isdigit())

#islower()
#The islower() method checks whether all the case-based characters (letters) of the string are lowercase.
str = "THIS is string example....wow!!!"
print (str.islower())
str = "this is string example....wow!!!"
print (str.islower())

#isnumeric()
str = "this2016"
print (str.isnumeric())
str = "23443434"
print(str.isnumeric())

#isspace()
#The isspace() method checks whether the string consists of whitespace.

str = " "
print (str.isspace())
str = "This is string example....wow!!!"
print (str.isspace())

#istitle()
"""The istitle() method checks whether all the case-based characters in the string following
non-casebased letters are uppercase and all other case-based characters are lowercase."""

str = "This Is String Example...Wow!!!"
print (str.istitle())
str = "This is string example....wow!!!"
print (str.istitle())

#isupper()
#The isupper() method checks whether all the case-based characters (letters) of the string are uppercase

str = "THIS IS STRING EXAMPLE....WOW!!!"
print (str.isupper())
str = "THIS is string example....wow!!!"
print (str.isupper())

#join()
#The join() method returns a string in which the string elements of sequence have been joined by str separator.

s = "-"
seq = ("a", "b", "c") # This is sequence of strings.
print (s.join( seq ))

#len()
#The len() method returns the length of the string

str = "this is string example....wow!!!"
print ("Length of the string: ", len(str))

#ljust()
"""The method ljust() returns the string left justified in a string of length width. Padding is
done using the specified fillchar (default is a space). The original string is returned if width
is less than len(s)."""

str = "this is string example....wow!!!"
print (str.ljust(50, '*'))

#lower()
#The method lower() returns a copy of the string in which all case-based characters have been lowercased.

str = "THIS IS STRING EXAMPLE....WOW!!!"
print (str.lower())

#lstrip()
"""The lstrip() method returns a copy of the string in which all chars have been stripped
from the beginning of the string (default whitespace characters)."""

str = " this is string example....wow!!!"
print (str.lstrip())
str = "*****this is string example....wow!!!*****"
print (str.lstrip('*'))

#max()
print (max( 4,12,43.3,19,100 ) )
print (min( 4,12,43.3,19,100 ) )

#replace()
"""The replace() method returns a copy of the string in which the occurrences of old have
been replaced with new"""

str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))

#rfind()
#The rfind() method returns the last index where the substring str is found, or -1 if no such index exists
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))

#rindex()
"""The rindex() method returns the last index where the substring str is found, or raises an
exception if no such index exists"""

str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))

#rjust()
str = "this is string example....wow!!!"
print (str.rjust(50, '*'))

#rstrip()
str = "this is string example....wow!!!    "
print (str.rstrip())
str = "*****this is string example....wow!!!*****"
print(str.rstrip('*'))

#split()
#The split() method returns a list of all the words in the string
str = "this is string example....wow!!!"
print (str.split( ))

#splitlines()
#The splitlines() method returns a list with all the lines in string

str = "this is \nstring example....\nwow!!!"
print (str.splitlines( ))

#startswith()
str = "this is string example....wow!!!"
print (str.startswith( 'this' ))
print (str.startswith( 'string', 8 ))
print (str.startswith( 'this', 2, 4 ))

#strip()
"""The strip() method returns a copy of the string in which all chars have been stripped from
the beginning and the end of the string (default whitespace characters)"""

str = "*****this is string example....wow!!!*****"
print (str.strip( '*' ))

#swapcase()
"""The swapcase() method returns a copy of the string in which all the case-based
characters have had their case swapped"""

str = "this is string example....wow!!!"
print (str.swapcase())
str = "This Is String Example....WOW!!!"
print (str.swapcase())

#title()
"""The title() method returns a copy of the string in which first characters of all the words
are capitalized"""

str = "this is string example....wow!!!"
print (str.title())

#upper()
"""The upper() method returns a copy of the string in which all case-based characters have
been uppercased"""

str = "this is string example....wow!!!"
print (str.upper())