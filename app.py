from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Discord Sales Bot",
        "description": "Automated sales bot with payment integration and key delivery.",
        "tech": "Python, Discord.py, APIs"
    },
    {
        "name": "Web Control Panel",
        "description": "Admin dashboard to manage bots and users.",
        "tech": "Flask, MongoDB, HTML/CSS"
    },
    {
        "name": "Automation Scripts",
        "description": "Python scripts for task automation and system optimization.",
        "tech": "Python"
    }
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)