import React, { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";
import "./Chatbot.css";

const Chatbot = () => {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSendMessage = async () => {
    if (!message.trim()) return;

    setLoading(true);
    setChatHistory([...chatHistory, { sender: "user", text: message }]);
    setMessage("");

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", { message });

      console.log("API Response:", res.data); // Debugging

      setTimeout(() => {
        setChatHistory((prevChat) => [
          ...prevChat,
          { sender: "bot", text: res.data.response || "⚠️ No response from AI" },
        ]);
        setLoading(false);
      }, 1500);
    } catch (error) {
      console.error("Request Error:", error); // Debugging

      setChatHistory([
        ...chatHistory,
        { sender: "bot", text: "⚠️ Error: Unable to fetch response" },
      ]);
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-card">
        <h2 className="chat-title">🤖 Prompt AI</h2>
        <div className="chat-history">
          {chatHistory.map((msg, index) => (
            <div key={index} className={`chat-message ${msg.sender}`}>
              {msg.sender === "bot" ? (
                <ReactMarkdown>{msg.text}</ReactMarkdown>
              ) : (
                msg.text
              )}
            </div>
          ))}
          {loading && <div className="chat-message bot typing-animation">...</div>}
        </div>
        <div className="chat-box">
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your message..."
            rows="3"
          />
          <button onClick={handleSendMessage} disabled={loading} className="send-btn">
            {loading ? "Thinking..." : "Send"}
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;
