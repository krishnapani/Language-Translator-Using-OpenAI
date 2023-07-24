from flask import Flask, render_template, request
import openai
app = Flask(__name__)

openai.api_key = "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"


def translate_text(input_language, text, target_language):
    prompt = f"Translate '{text}' from '{input_language}' to {target_language}:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].text.strip()


@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        input_language = request.form["input_language"]
        text = request.form["text"]
        target_language = request.form["target_language"]

        translated_text = translate_text(input_language, text, target_language)

    return render_template("index.html", translated_text=translated_text)


if __name__ == "__main__":
    app.run(debug=True)
