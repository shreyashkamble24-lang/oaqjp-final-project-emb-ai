"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the homepage and process submitted text."""
    result = None
    text_to_analyze = ""

    if request.method == "POST":
        text_to_analyze = request.form.get(
            "textToAnalyze", ""
        )

        if not text_to_analyze.strip():
            result = {"error": "Please enter some text."}
        else:
            result = emotion_detector(text_to_analyze)

    return render_template(
        "index.html",
        result=result,
        text_to_analyze=text_to_analyze,
    )


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Return emotion analysis for the supplied text."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
