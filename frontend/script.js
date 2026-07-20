// ----------------------
// Signup
// ----------------------

async function signup() {

    const username = document.getElementById("signup-username").value.trim();
    const email = document.getElementById("signup-email").value.trim();
    const password = document.getElementById("signup-password").value;


    if (!username || !email || !password) {
        alert("Please fill all signup fields.");
        return;
    }


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/signup",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    username: username,
                    email: email,
                    password: password
                })
            }
        );


        const data = await response.json();

        alert(data.message);


    } catch (error) {

        alert("Unable to connect to backend.");

        console.error(error);

    }

}





// ----------------------
// Login
// ----------------------

async function login() {

    const email = document.getElementById("login-email").value.trim();

    const password = document.getElementById("login-password").value;



    if (!email || !password) {

        alert("Please enter email and password.");
        return;

    }



    try {


        const response = await fetch(
            "http://localhost:8000/login",
            {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },


                body: JSON.stringify({

                    email: email,
                    password: password

                })

            }
        );



        const data = await response.json();
        console.log(data);
        alert(JSON.stringify(data));


        if (data.user_id) {


            localStorage.setItem(
                "user_id",
                data.user_id
            );


            alert("Login Successful!");

            window.location.href = "chat.html";


        } else {


            alert(data.message);


        }



    } catch(error) {


        alert("Unable to connect to backend.");

        console.error(error);


    }


}








// ----------------------
// Chat Function
// ----------------------

async function sendMessage() {


    const inputField = document.getElementById("user-input");

    const chatWindow = document.getElementById("chat-window");


    const userText = inputField.value.trim();



    if (userText === "") return;




    // Add user message

    const userDiv = document.createElement("div");

    userDiv.className = "user-msg";

    userDiv.innerText = userText;


    chatWindow.appendChild(userDiv);



    inputField.value = "";




    // AI loading message

    const aiDiv = document.createElement("div");

    aiDiv.className = "ai-msg";

    aiDiv.innerText = "CodeMentor AI is thinking...";


    chatWindow.appendChild(aiDiv);



    chatWindow.scrollTop =
    chatWindow.scrollHeight;





    try {


        const userId =
        localStorage.getItem("user_id") || 1;



        const response = await fetch(
            "http://127.0.0.1:8000/api/chat",
            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },


                body: JSON.stringify({

                    message: userText,

                    user_id: Number(userId)

                })

            }
        );



        const data = await response.json();



        aiDiv.innerHTML =
        formatAIResponse(data.response);



    } catch(error) {


        aiDiv.innerText =
        "Error: Could not connect to backend server.";


        console.error(
            "Chat Error:",
            error
        );


    }



    chatWindow.scrollTop =
    chatWindow.scrollHeight;


}








// ----------------------
// Format AI Response
// ----------------------

function formatAIResponse(text) {


    // Convert Gemini markdown code blocks

    text = text.replace(

        /```(?:python|javascript|java|cpp|html|css|sql)?\s*([\s\S]*?)```/gi,

        function(match, code) {


            return `

            <pre class="code-box"><code>${escapeHTML(code.trim())}</code></pre>

            `;

        }

    );



    return text.replace(
        /\n/g,
        "<br>"
    );

}








// ----------------------
// Escape HTML
// ----------------------

function escapeHTML(text) {


    return text

        .replace(/&/g, "&amp;")

        .replace(/</g, "&lt;")

        .replace(/>/g, "&gt;")

        .replace(/"/g, "&quot;")

        .replace(/'/g, "&#039;");


}