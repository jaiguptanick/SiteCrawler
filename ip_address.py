import os

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command) #this will pipe code with os and open the command in the terminal
    results = str(process.read()) #read what is output in terminal and convrt to string
    marker = results.find('has address') + 12  # this will go to index of ip
    return results[marker:].splitlines()[0]  #splitlines used as we only want ip in first line of terminal output

#print(get_ip_address('google.com'))