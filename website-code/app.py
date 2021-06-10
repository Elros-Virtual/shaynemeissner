from flask import Flask, render_template, request
import smtplib


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    # if request.method == "POST":
    #     name = request.form.get("name")
    #     email = request.form.get("email")
    #     message = request.form.get("message")
    #     server = smtplib.SMTP("smtp.gmail.com", 587)
    #     server.starttls()
    #     server.login("iar31.roberts@gmail.com", "password")
    #     server.sendmail("iar31.roberts@gmail.com", email, message)
    #     return render_template('index.html')

    # else:
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
