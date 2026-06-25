const btn = document.getElementById("analyzeBtn");

btn.addEventListener("click", analyzeSentiment);

async function analyzeSentiment() {

    const text =
        document.getElementById("textInput").value;

    if (!text.trim()) {
        alert("Please enter text");
        return;
    }

    btn.classList.add("loading");
    btn.disabled = true;

    const btnText =
        document.getElementById("btnText");

    const loadingTexts = [
        "Analyzing...",
        "Processing...",
        "Detecting Emotion...",
        "Generating Result..."
    ];

    let index = 0;

    const textAnimation = setInterval(() => {

        btn.classList.remove("loading");

        btnText.style.display = "inline";

        btnText.textContent =
            loadingTexts[index];

        index =
            (index + 1) %
            loadingTexts.length;

    }, 1000);

    try {

        const response = await fetch(
            "http://localhost:8000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type":
                    "application/json"
                },
                body: JSON.stringify({
                    text: text
                })
            }
        );

        const data = await response.json();

        document.getElementById(
            "sentiment"
        ).textContent =
            data.sentiment;

        const confidence =
            (data.confidence * 100)
            .toFixed(1);

        document.getElementById(
            "confidence"
        ).textContent =
            confidence + "%";

        document.getElementById(
            "progressBar"
        ).style.width =
            confidence + "%";

        const sentimentElement =
            document.getElementById(
                "sentiment"
            );

        if (
            data.sentiment
            .toLowerCase()
            .includes("positive")
        ) {
            sentimentElement.style.color =
                "#22c55e";
        }

        else if (
            data.sentiment
            .toLowerCase()
            .includes("negative")
        ) {
            sentimentElement.style.color =
                "#ef4444";
        }

        else {
            sentimentElement.style.color =
                "#facc15";
        }

    }

    catch (error) {

        console.error(error);

        alert(
            "Failed to connect API"
        );

    }

    finally {

        clearInterval(textAnimation);

        btn.classList.remove("loading");

        btn.disabled = false;

        btnText.textContent =
            "Analyze Sentiment";

    }

}