// ==============================
// User Authentication
// ==============================

const userId = localStorage.getItem("user_id");


if (!userId) {

    alert("Please login first.");

    window.location.href = "index.html";

}



// Load history
window.onload = function () {

    loadChatHistory();

};




// ==============================
// Send Message
// ==============================

async function sendMessage() {


    const inputField =
        document.getElementById("user-input");


    const chatWindow =
        document.getElementById("chat-window");


    const userText =
        inputField.value.trim();



    if (userText === "")
        return;



    // User message

    const userDiv =
        document.createElement("div");


    userDiv.className =
        "user-msg";


    userDiv.innerText =
        userText;


    chatWindow.appendChild(userDiv);



    inputField.value = "";




    // AI loading

    const aiDiv =
        document.createElement("div");


    aiDiv.className =
        "ai-msg";


    aiDiv.innerText =
        "CodeMentor AI is thinking...";


    chatWindow.appendChild(aiDiv);



    chatWindow.scrollTop =
        chatWindow.scrollHeight;



    try {


        const response =
        await fetch(

            "http://127.0.0.1:8000/api/chat",

            {

                method: "POST",

                headers: {

                    "Content-Type":
                    "application/json"

                },


                body: JSON.stringify({

                    message: userText,

                    user_id: Number(userId)

                })

            }

        );



        const data =
        await response.json();



        aiDiv.innerHTML =
            formatAIResponse(
                data.response
            );



        loadChatHistory();



    }


    catch(error){


        aiDiv.innerText =
        "❌ Unable to connect to backend.";


        console.error(
            "Chat Error:",
            error
        );


    }



    chatWindow.scrollTop =
        chatWindow.scrollHeight;


}







// ==============================
// Format AI Response
// ==============================

function formatAIResponse(text){

    if(!text)
        return "";

    // Convert markdown code blocks
    text = text.replace(
    /```(\w+)?\n?([\s\S]*?)```/g,
    function(match, language, code){
        return createCodeBox(
            language || detectLanguage(code),
            code.trim()
        );
    }
);
    // Replace line breaks
    return text.replace(/\n/g, "<br>");

}


    


// ==============================
// Create Code Box
// ==============================

function createCodeBox(language, code){

    return `
<div class="code-container">
    <div class="code-header">
        <span>${language}</span>
        <button onclick="copyCode(this)">Copy</button>
    </div>
    <pre><code>${escapeHTML(code.trim())}</code></pre>
</div>`;
}







// ==============================
// Detect Language
// ==============================

function detectLanguage(code){


    if(code.includes("def "))
        return "Python";


    if(code.includes("console.log"))
        return "JavaScript";


    if(code.includes("#include"))
        return "C++";


    if(code.includes("public class"))
        return "Java";


    return "Code";


}







// ==============================
// Escape HTML
// ==============================

function escapeHTML(text){


    return text

    .replace(/&/g,"&amp;")

    .replace(/</g,"&lt;")

    .replace(/>/g,"&gt;")

    .replace(/"/g,"&quot;")

    .replace(/'/g,"&#039;");


}








// ==============================
// Copy Code
// ==============================

function copyCode(button){


    const code =

    button
    .closest(".code-container")
    .querySelector("code")
    .innerText;



    navigator.clipboard.writeText(code);



    button.innerText =
    "Copied ✓";



    setTimeout(()=>{


        button.innerText =
        "Copy";


    },2000);


}








// ==============================
// Load Chat History
// ==============================

async function loadChatHistory(){


    try{


        const response =
        await fetch(

        `http://127.0.0.1:8000/chat-history/${userId}`

        );



        const chats =
        await response.json();



        const historyList =
        document.getElementById(
            "history-list"
        );



        if(!historyList)
            return;



        historyList.innerHTML = "";



        chats.reverse().forEach(chat=>{


            const li =
            document.createElement("li");


            li.innerText =
            chat.prompt;


            historyList.appendChild(li);


        });



    }


    catch(error){


        console.error(
            "History Error:",
            error
        );


    }


}








// ==============================
// New Chat
// ==============================

function newChat(){


    document.getElementById(
        "chat-window"
    ).innerHTML = `


    <div class="ai-msg">


    Hello! 👋 I am CodeMentor AI.

    How can I help you today?


    </div>


    `;


}








// ==============================
// Logout
// ==============================

function logout(){


    localStorage.removeItem(
        "user_id"
    );


    window.location.href =
    "index.html";


}