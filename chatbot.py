from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ✅ Make sure this matches your frontend
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type", "Authorization"],
)

# ✅ Ensure API key is correctly set
genai.configure(api_key="AIzaSyDyJNQAMUw6t_pbBdoka2Q_u0qFWiIaAQw")

@app.post("/chat")
async def chat(request: dict):
    try:
        user_message = request.get("message", "")
        if not user_message:
            return {"response": "⚠️ Please enter a message."}

        # ✅ Initialize model
        model = genai.GenerativeModel("gemini-1.5-pro")

        # ✅ Generate response safely
        response = model.generate_content(user_message)

        if not response or not hasattr(response, "text"):
            return {"response": "⚠️ No response from AI."}

        return {"response": response.text}

    except Exception as e:
        print(f"❌ Error: {e}")  # ✅ Debugging in the console
        return {"response": "⚠️ AI service unavailable. Try again later."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
