"""Flask app for emotion detection using Watson NLP."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def render_index_page():
    """Render the main HTML interface for the application."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emo_detector():
    """
    Process the text input from the user and return emotion analysis results.

    This function retrieves the 'textToAnalyze' query parameter,
    sends it to the emotion_detector, and returns a formatted response
    with emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return 'Error: No text provided. Please enter some text.', 400

    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return 'Invalid input! Try again.', 400

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)

