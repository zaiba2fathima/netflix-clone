from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    lang = session.get('lang', 'en')
    return render_template('index.html', lang=lang)

@app.route('/change_language', methods=['POST'])
def change_language():
    selected_lang = request.form.get('language', 'en')
    session['lang'] = selected_lang
    return redirect('/')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        print("Email entered:", email)
        return render_template('signup.html', email=email)
    return render_template('signup.html', email=None)

# ✅ Footer links routes
@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/help')
def help_centre():
    return render_template('help.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

if __name__ == '__main__':
    app.run(debug=True)