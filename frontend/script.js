async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const chatWindow = document.getElementById("chat-window");
    const userText = inputField.value.trim();

    if (userText === "") return;

    // User message
    const userDiv = document.createElement("div");
    userDiv.className = "user-msg";
    userDiv.innerText = userText;
    chatWindow.appendChild(userDiv);

    inputField.value = "";
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // AI loading message
    const aiDiv = document.createElement("div");
    aiDiv.className = "ai-msg";
    aiDiv.innerText = "CodeMentor AI is thinking...";
    chatWindow.appendChild(aiDiv);

    chatWindow.scrollTop = chatWindow.scrollHeight;

    try {

        const response = await fetch("http://127.0.0.1:8000/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: userText,
                user_id: 1
            })
        });

        if (!response.ok) {
            throw new Error("Server Error");
        }

        const data = await response.json();

        let aiResponse = data.response;

        // Remove Markdown code blocks
        aiResponse = aiResponse.replace(/```python/g, "");
        aiResponse = aiResponse.replace(/```/g, "");
        aiResponse = aiResponse.trim();

        aiDiv.innerText = aiResponse;

    } catch (error) {

        aiDiv.innerText = "Error: Could not connect to the backend server.";
        console.error(error);

    }

    chatWindow.scrollTop = chatWindow.scrollHeight;
}