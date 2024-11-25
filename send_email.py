import os
import resend 
resend.api_key = os.environ["RESEND_API_KEY"]

params: resend.Emails.SendParams = {
    "from": "adetayo",
    "to": ["adetayo.adekunle@stonybrook.edu"],
    "subject": "Hello, Adetayo Adekunle, Schedule task executed",
    "html": "<strong>it works!</strong>",
}

email = "resend.Emails.send(params)"
print(email)
