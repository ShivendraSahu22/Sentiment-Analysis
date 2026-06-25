const btn = document.getElementById("analyzeBtn");

btn.addEventListener("click", analyzeSentiment);

async function analyzeSentiment() {

    const text = document.getElementById("textInput").value;

    if (!text.trim()) {
        alert("Please enter text");
        return;
    }

    btn.disabled = true;

    const btnText = document.getElementById("btnText");

    const loadingTexts = [
        "Analyzing...",
        "Processing...",
        "Detecting Emotion...",
        "Generating Result..."
    ];

    let index = 0;

    const originalText = "Analyze Sentiment";

    // animation
    const textAnimation = setInterval(() => {
        btnText.textContent = loadingTexts[index];
        index = (index + 1) % loadingTexts.length;
    }, 1000);

    try {

        const response = await fetch(
            "https://sentiment-analysis-07s3.onrender.com/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: text   // ✅ FIXED: user input used
                })
            }
        );

        if (!response.ok) {
            throw new Error("Server Error: " + response.status);
        }

        const data = await response.json();

        document.getElementById("sentiment").textContent = data.sentiment;

        const confidence = (data.confidence * 100).toFixed(1);

        document.getElementById("confidence").textContent = confidence + "%";

        document.getElementById("progressBar").style.width = confidence + "%";

        const sentiment = data?.sentiment || "unknown";

        if (sentiment.toLowerCase().includes("positive")) {
            sentimentElement.style.color = "#22c55e";
        }
        else if (sentiment.toLowerCase().includes("negative")) {
            sentimentElement.style.color = "#ef4444";
        }
        else {
            sentimentElement.style.color = "#facc15";
        }

document.getElementById("sentiment").textContent = sentiment;

    } catch (error) {

        console.error(error);
        alert("Failed to connect API");

    } finally {

        clearInterval(textAnimation);

        btn.disabled = false;

        btnText.textContent = originalText;
    }
}

const data = await response.json();

console.log("API RESPONSE:", data);