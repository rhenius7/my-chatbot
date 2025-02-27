from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

# ✅ Step 1: Create FastAPI App
app = FastAPI()

# ✅ Step 2: Configure CORS (MUST come after `app = FastAPI()`)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 🔥 Replace with your actual frontend URL
    allow_credentials=True,
    allow_methods=["POST"],  # Limit to only needed methods for security
    allow_headers=["Content-Type", "Authorization"],  # Limit to required headers
)

# ✅ Step 3: Set up Gemini API Key
genai.configure(api_key="AIzaSyCXYAtK0-IchMXc5z9HZBlnN9KrYDVf_pg")

# ✅ Step 4: Define Chatbot Route
@app.post("/chat")
async def chat(request: dict):
    user_message = request.get("message", "")
    if not user_message:
        return {"response": "Please enter a message."}
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_message)
    
    return {"response": response.text}

# ✅ Step 5: Run Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
