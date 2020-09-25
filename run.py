#build using repl.it

import urllib.request 

total_requests = 0
last_year_requests = 0

urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "save.log")
x = open("save.log", "r")
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
my_copy = 'save.log'

#finding amount of requests
for line in x:
   total_requests = total_requests + 1
   if '1995' in line:
      last_year_requests = last_year_requests + 1
x.close()
#print results
print("How many total requests have been made in the last year?", last_year_requests)
print("How many total requests were made in the time period represented by the log?", total_requests)

#Your program should split the log file into 12 smaller files

print("How many requests were made on each day?")
print("How many requests were made on a week-by-week basis? Per month?")
print("What percentage of the requests were not successful (any 4xx status code)?")
print("What percentage of the requests were redirected elsewhere (any 3xx codes)?")
print("What was the most-requested file?")
print("What was the least-requested file?")

