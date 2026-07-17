from flask import Flask

app = Flask(__name__)

@app.route("/")
def teacup():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Rotating Tea Cup</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
            }
            .cup {
                width: 150px;
                height: 150px;
                background: url('https://upload.wikimedia.org/wikipedia/commons/4/45/Teacup_icon.png') no-repeat center;
                background-size: contain;
                animation: spin 10s linear infinite;
            }
            @keyframes spin {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>
        <div class="cup"></div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
