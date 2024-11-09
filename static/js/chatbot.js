document.addEventListener("DOMContentLoaded", () => {
    const chatbotButton = document.getElementById("chatbot-button");
    const chatbotModal = document.getElementById("chatbot-modal");
    const closeChatbot = document.getElementById("close-chatbot");
    const sendMessage = document.getElementById("send-message");
    const chatInput = document.getElementById("chat-input");
    const messageContainer = document.getElementById("message-container");

    let lastRequestTime = 0;  // Para controlar el tiempo entre solicitudes
    let totalTokensUsed = 0;   // Para llevar el conteo total de tokens utilizados

    chatbotButton.addEventListener("click", () => {
        chatbotModal.classList.toggle("hidden");
    });

    closeChatbot.addEventListener("click", () => {
        chatbotModal.classList.add("hidden");
    });

    sendMessage.addEventListener("click", async () => {
        const userMessage = chatInput.value;
        if (userMessage.trim() === "") return;

        displayMessage(userMessage, "user");
        chatInput.value = "";  // Limpiar campo de entrada

        const response = await sendToOpenAIChatAPI(userMessage);
        displayMessage(response, "bot");
    });

    function displayMessage(message, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("mb-2", sender === "user" ? "text-right" : "text-left");
        messageDiv.textContent = message;
        messageContainer.appendChild(messageDiv);
        messageContainer.scrollTop = messageContainer.scrollHeight;  // Auto-scroll al último mensaje
    }

    async function sendToOpenAIChatAPI(message) {
        const currentTime = Date.now();
        if (currentTime - lastRequestTime < 3000) {  // Espera 3 segundos entre llamadas
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
        lastRequestTime = Date.now(); // Actualiza el tiempo de la última solicitud

        try {
            const response = await fetch('https://api.openai.com/v1/chat/completions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer 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',
                    'OpenAI-Organization': 'org-HEryS74SNV4b3PNmJAl7fvrC'  // Reemplaza con tu Organization ID
                },
                body: JSON.stringify({
                    model: "gpt-3.5-turbo",
                    messages: [{ role: "user", content: message }]
                })
            });

            if (!response.ok) {
                throw new Error("Network response was not ok.");
            }

            const data = await response.json();
            const tokensUsed = data.usage.total_tokens; // Obtén el número total de tokens utilizados
            totalTokensUsed += tokensUsed; // Acumula los tokens utilizados

            console.log(`Total de tokens usados hasta ahora: ${totalTokensUsed}`);

            return data.choices[0].message.content || "Lo siento, no se pudo obtener una respuesta.";
        } catch (error) {
            console.error('Error:', error);
            return "Lo siento, no pude obtener una respuesta. Intenta nuevamente más tarde.";
        }
    }
});
