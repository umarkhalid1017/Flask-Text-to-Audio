from flask import Flask, render_template, request, send_file
import pyttsx3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    output_file = "output_audio.mp3"

    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
