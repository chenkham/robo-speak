from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def speak():
    text = request.form.get("text")

    if text.strip().lower() == 'exit':
        print("Exiting RoboSpeaker system 2.0. Have a great day! sir")
        try:

            engine = pyttsx3.init()
            engine.say("Goodbye! Have a great day!")
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f"[ERROR] Not able to speak! goodbye sir: {e}")
        return render_template("index.html", last_text="Goodbye!")

    elif text.strip() == "":
        print("You didn't type anything!")
        try:

            engine = pyttsx3.init()
            engine.say("You didn't type anything!")
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f"[ERROR] Failed to speak empty message alert: {e}")
        return render_template("index.html", last_text="You didn't type anything!")

    else:
        print(f"Speaking: {text}")
        try:

            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f"[ERROR] Failed to speak: {e}")
        return render_template("index.html", last_text=text)


if __name__ == "__main__":
    app.run(debug=True, port=5001)