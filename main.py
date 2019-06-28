import requests
import json
import datetime
import timeit

url = 'http://api.pathofexile.com/public-stash-tabs'

print("[%s] Starting load json ..."%datetime.datetime.now())

## Start Json load
start = timeit.default_timer()
r = requests.get(url)
j = json.loads(r.content)
stop = timeit.default_timer()
workingTime = stop - start

## End Json load

print("[%s] Completed load json..."%datetime.datetime.now())
print("Loading time : %0.1f sec"%workingTime)


# Display Result
next_change_id = j["next_change_id"]
print ("next_change_id:")
print (next_change_id)
print ("\n")

# Display Player
stashes = j["stashes"]
print("array size : {0}".format(len(stashes)))

# Find Player
resultList = []
for s in stashes:
    if s['accountName']  ==  "barbartimosolo" :
        resultList.append(s)

#find account
print (resultList)
print ("\n")


