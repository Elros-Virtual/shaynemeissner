from flask import Flask, render_template, request
from flask_sendgrid import SendGrid


key = open('/vault/secrets/api-key.txt').read()
i = key.find(":", 5)
j = key.find("]")
apikey = key[i+1:j]

app = Flask(__name__)
app.config['SENDGRID_API_KEY'] = apikey
app.config['SENDGRID_DEFAULT_FROM'] = 'hello@elrosvirtual.co.uk'
mail = SendGrid(app)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        mail.send_email(to_email=email,
                        subject='Thank you for your Contact', text=message)

        return render_template('index.html')

    else:
        return render_template('index.html')


@app.route('/seouless')
def seouless():
    return render_template('seouless.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
