import json
import re
import urllib

connection = urllib.urlopen("http://www.sportsoddshistory.com/nfl-reg/?y=2017&sa=nfl&a=sb&o=r")
contents = connection.read()
connection.close()

# print contents

# m = re.search('New England Patriots    </a></td><td align=right>.* </td>', contents)
# match = re.search('New England Patriots    </a>[\n]</td>[\n]<td align=right>[\n].* </td>', contents)
match = re.search(r'New England Patriots    </a>.*<td align=right>', contents, re.DOTALL)

if match:
    print "It matched!"
    print match.group()
    print match.group(0)
else:
    print "Didn't match"
