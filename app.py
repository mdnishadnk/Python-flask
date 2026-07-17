from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask_Nishad N K"

if __name__ == "__main__":
    # Bind to all interfaces, not just localhost
    app.run(host="0.0.0.0", port=5000)
