import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import os
from dotenv import load_dotenv


load_dotenv()

class BotService:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API key is missing. Please set it in the environment variables.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat_session = self.model.start_chat(history=[])

    def generate_reply(self, user_message: str):
        if not user_message.strip():
            raise ValueError("User message is empty.")
        
        response = self.chat_session.send_message(user_message)
        if not response or not response.text:
            raise ValueError("Failed to generate a reply from the model.")
        
        return response.text, self.chat_session.history

# FastAPI application setup
app = FastAPI()
bot_service = BotService()

# Pydantic model for request validation
class MessageInput(BaseModel):
    content: str

# API endpoint to handle user interaction
@app.post("/interact")
async def interact(message_input: MessageInput):
    try:
        reply, _ = bot_service.generate_reply(message_input.content)
        return {"reply": reply}
    except (ValidationError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
