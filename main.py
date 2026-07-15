from fastapi import FastAPI
from dotenv import load_dotenv
import resend
import os
load_dotenv()
app = FastAPI()

users=[{"id":1,"name":"John vesli","email":"john@example.com","age":28,"city":"Hyderabad"},{"id":2,"name":"Alice smith","email":"alice@example.com","age":25,"city":"Bangalore"},{"id":3,"name":"David Lee","email":"david@example.com","age":31,"city":"Chennai"},{"id":4,"name":"Sarah Johnson","email":"sarah@example.com","age":29,"city":"Mumbai"}]

resend.api_key = os.getenv("RESEND_API_KEY")
print("Resend API Key:", resend.api_key)  
@app.get("/")
async def read_root():
    return {"message": "Welcome to my portfolio!"}


@app.get("/dataa")
async def read_data():
    return users

@app.post("/send-email")
async def send_email(name:str, mailfrom:str,subject:str,message:str, mailto:str="kareemsheik133@gmail.com"):
    try:
        res = resend.Emails.send({
            "from": "onboarding@resend.dev",   # or your verified email
            "to": [mailto],
            "subject": subject,
            "text": f"Name: {name}\nEmail: {mailfrom}\n\n{message}",
            "reply_to": mailfrom
        })

        return {
            "message": "Email sent successfully",
            "response": res
        }
    except Exception as e:
        return {"error": str(e)}
     