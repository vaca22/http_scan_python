import sys
import re
import urllib3
import functools
from concurrent.futures import ThreadPoolExecutor

# PARAMS - could be changed to be CLI arguments
TIMEOUT = 15                  # Connect/read timeout
RETRIES = 1                       # Connect/read retries that are permitted
REDIRECTS = 0                     # How many redirects to follow
OUTPUT_STATUS_CODES = [200, 403]  # Status codes to track in results

THREADS = 1000





# request a url and return a (url, status code) tuple
def request(url):
    try:
        response = http.request('GET', url)
        print(url, response.status)
        return (url, response.status)
    except Exception: # SSL error, timeout, host is down, firewall block, etc.
        # print(url, 'ERROR')
        return (url, None)


# parse hosts
hosts = ['vaca.vip']
paths = []
for i in range(1,10000):
    paths.append(i)


# initialize our http object
timeout = urllib3.util.Timeout(connect=TIMEOUT, read=TIMEOUT)
retries = urllib3.util.Retry(connect=RETRIES, read=RETRIES, redirect=REDIRECTS)
http = urllib3.PoolManager(
    retries=retries,
    timeout=timeout,
    num_pools=THREADS,
    maxsize=THREADS,
    block=True
)


print('------ REQUESTS ------\n')

urls = ["http://"+host +":" +str(path) for host in hosts for path in paths]
with ThreadPoolExecutor(max_workers=THREADS) as executor:
    results = executor.map(request, urls)
executor.shutdown(wait=True)

# print our results
print('\n------ RESULTS ------\n')




print("------ SCAN COMPLETE ------\n")