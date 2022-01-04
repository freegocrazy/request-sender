# import libraries
import requests
import threading

# get input for the url var
url = input("URL: ")

# get input for looptime var
looptime = input("How many requests to send: ")

# get input for how many threads to use
threadamount = input("How many threads to use (sends the amount of request per thread): ")

# proxy list
proxy = {
    'http': 'http://64.227.62.123:80'
}

def send_requests():
    for i in range(int(looptime)):
        # send the request
        requestinfo = requests.get(url, proxies=proxy)

        # print out a success response
        print("[SUCCESS] Response sent")
    
        # print out response code to debug anything happening :D
        print(requestinfo)

# do threading stuff

threads = []

for i in range(int(threadamount)):
    thread = threading.Thread(target=send_requests)
    thread.daemon = True
    threads.append(thread)

for i in range(int(threadamount)):
    threads[i].start()

for i in range(int(threadamount)):
    threads[i].join()