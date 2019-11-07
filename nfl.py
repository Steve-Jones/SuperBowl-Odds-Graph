# <td>class="g5-component--mlb-scores__linescore__table--summary__cell
#                                                g5-component--mlb-scores__linescore__table--summary__cell--runs"</td>
import json
import re
import urllib


# filename = "mlbSoxScore.htm"
#
# file = open(filename, "r")
# contents = file.read()
# file.close()

connection = urllib.urlopen("https://api.the-odds-api.com/v2/odds/?sport=NFL&region=uk&apiKey=df1b01d4f32621a2ebba2aec5516cd29")
contents = connection.read()
connection.close()


data = json.loads(contents)
# print data
print "Current Temp: ", data["data"]["events"]["Denver Broncos_New England Patriots"]["sites"]["pinnacle"]["odds"]["h2h"]
# print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


# m = re.search('<span class="competitor-name ng-binding ng-scope ellipsis-overflow" ng-if="market.hasPropositionLayout" swc-ellipsis-if-overflow="">', contents)

# if m:
#     print "It matched!"
#     print m.group()
#     print m.group(1)
# else:
#     print "Didn't match"

# # Find where "score" occurs
# score = contents.find("g5-component--mlb-scores__linescore__table--summary__cell--runs")
#
# # Find location of the FIRST </div> after
# # g5-component--mlb-scores__linescore__table--summary__cell--runs
# divIndex = contents.find("</div>", score)
#
# # Find the location of the "">" that's between g5-component--mlb-scores__linescore__table--summary__cell--runs and...."
# # and the </div>
# gtIndex = contents.find(">", score, divIndex)
#
# print "The score is: ", contents[gtIndex+1:divIndex]


# ### REGULAR EXPRESSIONS ###
# # REGEX: create a pattern -- string containing special characters that descrives what you're looking for
# #        - Determines if a given string contains that pattern
# import re
# s = "This is a long string. It may or may not contain a magic word"
#
# # re.search(pattern string, string you're going to search) --> returns match object
# m = re.search("magic", s)
# print m
# print m.start()
# print m.end()
# print m.span()
#
# m = re.search("[Mm]agic", s)
