from infosect import app
from flask_ngrok import run_with_ngrok

if __name__=="__main__":
    app.run(debug=True,port=5000)
