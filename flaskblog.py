from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bce812732221c912dc71975601c09500'

posts =[
    {
        'author': 'Soham Deshpande',
        'title' : 'blog 1',
        'content' : 'first blog',
        'date_posted': '21 Feb 2023'

    },
    {
        'author': 'Prachi Kane',
        'title' : 'blog 10',
        'content' : 'tenth blog',
        'date_posted': '20 Feb 2023'

    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)