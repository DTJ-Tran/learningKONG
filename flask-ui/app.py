from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    text = ""
    if request.method == "POST":
        text = request.form.get("text", "")
    return render_template_string("""
        <h1>Text Input Form</h1>
        <form method="post">
            <input name="text" placeholder="Type something"/>
            <input type="submit"/>
        </form>
        {% if text %}
        <p>You typed: <strong>{{ text }}</strong></p>
        {% endif %}
    """, text=text)