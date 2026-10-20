# In-class 6 notes

## What happens with a wrong key? What status code?
It will prevent any image metadata records from loading, 403 Forbidden** HTTP status code

## Where does your key live, and why isn't it in earth.py?
file labeled .env directly in my workspace because coding secret keys inside your code makes it highly vulnerable to public and anyone can see, steal, and abuse your API credentials.

## Stuck? Where?
confusing at first how to pass the key retrieved from os.getenv("NASA_API_KEY") into the requests.get() function. I did params = {"api_key": key}.