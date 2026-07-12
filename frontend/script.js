async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const chatWindow = document.getElementById("chat-window");
    const userText = inputField.value.trim();

    if (userText === "") return;

    // 1. User ka message UI par add karein
    const userDiv = document.createElement("div");
    userDiv.className = "user-msg";
    userDiv.innerText = userText;
    chatWindow.appendChild(userDiv);

    // Input box clear karein aur window scroll karein
    inputField.value = "";
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // 2. Temporary AI loading message dikhayein
    const aiDiv = document.createElement("div");
    aiDiv.className = "ai-msg";
    aiDiv.innerText = "CodeMentor AI is thinking...";
    chatWindow.appendChild(aiDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;

    try {
        // 3. FastAPI Server ko request bhejein
        const response = await fetch("http://127.0.0.1:8000/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userText })
        });

        const data = await response.json();
        
        // 4. Loading text ko actual AI response se replace karein
        aiDiv.innerText = data.response;

    } catch (error) {
        aiDiv.innerText = "Error: Could not connect to the backend server.";
        console.error("Error connecting to backend:", error);
    }
    
    chatWindow.scrollTop = chatWindow.scrollHeight;
}