import sys
import requests
import colorama
from colorama import Fore
from colorama import init
init()
import argparse
parser = argparse.ArgumentParser()                                               

parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument("--url", "-u", type=str, required=True)
args = parser.parse_args()
                                                                   
def banner():
    font = """
   _____  _____ _____  ______    _____ _               _             
  / ____|/ ____|  __ \|  ____|  / ____| |             | |            
 | |    | (___ | |__) | |__    | |    | |__   ___  ___| | _____ _ __ 
 | |     \___ \|  _  /|  __|   | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |____ ____) | | \ \| |      | |____| | | |  __/ (__|   <  __/ |   
  \_____|_____/|_|  \_\_|       \_____|_| |_|\___|\___|_|\_\___|_|      """
    print(font)

if __name__ == "__main__":
    banner()	
args.url = sys.argv[4]

from tqdm import tqdm

for i in tqdm (range (100), desc="\nScanning the HTTP Request..."):
	pass


def search_and_remove_substrings(file_path, substrings):


  with open(file_path, 'r') as f:
    file_contents = f.read()

  for substring in substrings:
    file_contents = file_contents.replace(substring, '')

  return file_contents

for i in tqdm (range (100), desc="\nSending HTTP Request without CSRF Tokens..."):
	pass
def send_http_request(url, body):
	response = requests.post(url, data=body)
	print(f'\nResponse Status code: {response.status_code}')
	if response.status_code >= 200 and response.status_code < 300:
		print(Fore.RED+'\nVulnerable')
	elif response.status_code >=300:
		print(Fore.GREEN+'\nNot Vulnerable')

# It Allows You to Execute Code When the File Runs as a Script, but Not When It's Imported as a Module
if __name__ == '__main__':
  # The file path.
  file_path = args.file

  # The list of substrings to search for.
  substrings = ['csrfmiddlewaretoken','csrf_token','X-Csrf-Token','Authorization','Referer','SameSite']

  # Search for the substrings in the file and remove them.
  file_contents = search_and_remove_substrings(file_path, substrings)

  # Send an HTTP request to a server with the modified string as the body of the request.
  send_http_request(args.url, file_contents)
