// ==============================
// User Authentication
// ==============================

const userId = localStorage.getItem("user_id");
let selectedFile = "";

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

const aiDiv = document.createElement("div");

aiDiv.className = "ai-msg";

aiDiv.innerHTML = `
<div class="typing">
    🤖 CodeMentor AI is thinking
    <span></span>
    <span></span>
    <span></span>
</div>
`;

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



        const data = await response.json();

       
        aiDiv.innerHTML = formatAIResponse(data.response);

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

function formatAIResponse(text) {

    if (!text)
        return "";

    text = text.replace(
        /```(\w+)?\n?([\s\S]*?)```/g,
        function (match, language, code) {

            return createCodeBox(
                language || detectLanguage(code),
                code
            );

        }
    );

    text = text.replace(/\n/g, "<br>");

  //  setTimeout(() => {

       // if (window.hljs) {

         //   document
            //    .querySelectorAll("pre code")
            //    .forEach((block) => {

              //      hljs.highlightElement(block);

            //    });

     //   }

   // }, 100);

    return text;

}

    


// ==============================
// Create Code Box
// ==============================

// ==============================
// Create Code Box
// ==============================

function createCodeBox(language, code) {

    console.log("CODE RECEIVED:");
    console.log(code);

    return `
<div class="code-container">
    <div class="code-header">
        <span>${language}</span>
        <button onclick="copyCode(this)">📋 Copy</button>
    </div>
    <pre><code class="language-${language.toLowerCase()}">${escapeHTML(code)}</code></pre>
</div>
`;

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

function copyCode(button) {

    const code =
        button
            .closest(".code-container")
            .querySelector("code")
            .innerText;

    navigator.clipboard.writeText(code);

    button.innerHTML = "✅ Copied";

    setTimeout(() => {

        button.innerHTML = "📋 Copy";

    }, 2000);

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





// ----------------------
// GitHub Repository
// ----------------------

let selectedFile = "";


// Show repositories

async function showRepositories(){

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/github/repos"
        );


        const repos = await response.json();


        const chatWindow =
        document.getElementById("chat-window");


        repos.forEach(repo=>{


            const div =
            document.createElement("div");


            div.className="ai-msg";


            div.innerHTML = `

            <h3>📂 Repository</h3>

            <b>Name:</b> ${repo.name}<br>

            <b>Owner:</b> ${repo.owner.login}<br><br>


            <button onclick="showFiles()">
            📁 Show Files
            </button>

            `;


            chatWindow.appendChild(div);


        });


    }

    catch(error){

        console.log(error);

        alert("Unable to fetch repository");

    }

}




// ----------------------
// Show Repository Files
// ----------------------


async function showFiles(){


    const owner =
    "khushi49429-maker";


    const repo =
    "autonomous-coding-assistant";



    try{


        const response = await fetch(

        `http://127.0.0.1:8000/github/files/${owner}/${repo}`

        );


        const files =
        await response.json();



        const chatWindow =
        document.getElementById("chat-window");



        files.forEach(file=>{


            const div =
            document.createElement("div");


            div.className="ai-msg";


            div.innerHTML = `


            📄 <b>${file.path}</b>


            <br><br>


            <button onclick="selectFile('${file.path}')">

            Select

            </button>


            `;



            chatWindow.appendChild(div);



        });


    }


    catch(error){

        console.log(error);

        alert("Files loading failed");

    }


}





// ----------------------
// Select File
// ----------------------


function selectFile(path){


    selectedFile = path;


    const chatWindow =
    document.getElementById("chat-window");



    const div =
    document.createElement("div");



    div.className="ai-msg";



    div.innerHTML = `

    ✅ Selected File:

    <b>${path}</b>

    `;



    chatWindow.appendChild(div);


}






// ----------------------
// Review Selected File
// ----------------------


async function reviewFile(){


    if(selectedFile===""){

        alert("Select a file first");

        return;

    }



    const response = await fetch(

    "http://127.0.0.1:8000/github/review-file",

    {

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },


        body:JSON.stringify({

            owner:"khushi49429-maker",

            repo:"autonomous-coding-assistant",

            path:selectedFile

        })


    }

    );



    const data =
    await response.json();



    const chatWindow =
    document.getElementById("chat-window");



    const div =
    document.createElement("div");



    div.className="ai-msg";



    div.innerHTML = `


    <h3>📝 Review Result</h3>


    ${formatAIResponse(data.review)}


    `;



    chatWindow.appendChild(div);


}





// ----------------------
// Fix Selected File
// ----------------------


async function fixCurrentFile(){


    if(selectedFile===""){


        alert("Select a file first");

        return;

    }



    const response = await fetch(


    "http://127.0.0.1:8000/github/fix-file",


    {

        method:"POST",


        headers:{


            "Content-Type":"application/json"

        },


        body:JSON.stringify({


            owner:"khushi49429-maker",


            repo:"autonomous-coding-assistant",


            path:selectedFile


        })


    }



    );



    const data =
    await response.json();



    const chatWindow =
    document.getElementById("chat-window");



    const div =
    document.createElement("div");



    div.className="ai-msg";



    div.innerHTML = `


    <h3>🔧 Fixed Code</h3>


    ${formatAIResponse(data.fixed_code)}


    `;



    chatWindow.appendChild(div);



    chatWindow.scrollTop =
    chatWindow.scrollHeight;


}
console.log("chat.js loaded");

