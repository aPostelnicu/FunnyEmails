import requests
import yagmail

category = 'funny'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'TGir2u3CL2gAhtL9CCr2wA==5L1TM5MffLCExgIw'})

if response.status_code == requests.codes.ok:
    data = response.json()
    dictionary = data[0]
    quote = list(dictionary.values())[0]
    author = list(dictionary.values())[1]
else:
    print("Error:", response.status_code, response.text)

title = author + " sent you a funny email"
message = "Dear Friend," + "\n\n" + "I hope this email finds you well." + "\n\n" + quote + "\n\n" + "Sincerely," + "\n" + author

try:
    yag = yagmail.SMTP(user='andrei.postelnicu1998@gmail.com', password='MyPassword')
    yag.send(to='andrei.postelnicu1998@gmail.com', subject=title, contents=message)
    print("Email sent successfully")
except:
    print("Error, email was not sent")