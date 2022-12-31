import requests
import hashlib
import sys

def request_api_data(query):
  link = 'https://api.pwnedpasswords.com/range/' + query
  result = requests.get(link)
  if result.status_code != 200:
    raise RuntimeError(f'Sorry there is an error, please try again!')
  return result

def get_password_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_count(response, tail)

def main(args):
  for password in args:
    count = pwned_check(password)
    if count:
      print(f'{password} was found {count} times... please update your password!!')
    else:
      print(f'{password} is found not to be used that often! Safe for now!!')
  return 'Checked!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))