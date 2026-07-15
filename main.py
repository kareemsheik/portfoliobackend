from fastapi import FastAPI
import resend
import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    name:str
    mailfrom:str
    subject:str
    message:str

users=[{"id":1,"name":"John vesli","email":"john@example.com","age":28,"city":"Hyderabad"},{"id":2,"name":"Alice smith","email":"alice@example.com","age":25,"city":"Bangalore"},{"id":3,"name":"David Lee","email":"david@example.com","age":31,"city":"Chennai"},{"id":4,"name":"Sarah Johnson","email":"sarah@example.com","age":29,"city":"Mumbai"}]

resend.api_key = os.getenv("RESEND_API_KEY")

print("Key:", resend.api_key[:10] if resend.api_key else None)
@app.get("/")
async def read_root():
    return {"message": "Welcome to my portfolio!"}


@app.get("/dataa")
async def read_data():
    return users

@app.post("/send-email")
async def send_email(data: EmailRequest):
    try:
        res = resend.Emails.send({
            "from": "onboarding@resend.dev",   # or your verified email
            "to": ["kareemsheik133@gmail.com"],
            "subject": data.subject,
            "text": f"Name: {data.name}\nEmail: {data.mailfrom}\n\n{data.message}",
            "reply_to": data.mailfrom
        })

        return {
            "message": "Email sent successfully",
            "response": res
        }
    except Exception as e:
        return {"error": str(e)}
     