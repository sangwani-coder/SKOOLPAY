from flask import Flask, request, render_template, redirect, sessions

app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    return render_template('school/index.html')


@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    return render_template('school/dashboard.html', session="show")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    try:
        if request.method =='GET':
            return render_template('auth/login.html')
        return redirect('/dashboard')
    except Exception as e:
        print(e)
    


@app.route('/register', methods = ['GET', 'POST'])
def register():
    try:
        if request.method =='GET':
            return render_template('auth/register.html')
        return redirect('/login')
    except Exception as e:
        print(e)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    try:
        if request.method =='GET':
            return render_template('auth/signup.html')
        return redirect('/login')
    except Exception as e:
        print(e)

@app.route('/history', methods = ['GET', 'POST'])
def history():
    return render_template('history.html')

@app.route('/logout')
def logout():
    try:
        return redirect('/')
    except Exception as e:
        print(e)

if __name__=='__main__':
    app.run(port=5000, debug=True)
