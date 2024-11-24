Need to understand:
String methods in JS

Normalize the strings:

.toLowerCase() makes both strings lowercase to avoid case sensitivity.
.replace(/\s+/g, '') removes all spaces so that we're only dealing with letters.
Sort the characters:

.split('') splits the string into an array of characters.
.sort() sorts the array alphabetically.
.join('') combines the sorted array back into a string.
Compare: If the sorted versions of both strings are equal, then the original strings are anagrams.