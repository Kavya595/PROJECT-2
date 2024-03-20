from flask import Flask ,render_template,request
app=Flask('kavya')

@app.route('/',methods=['GET'])
def homepage():
    return 'good morning hyderabad'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/kavya',methods=['GET'])
def login():
    return render_template('kavya.html')


@app.route('/login-form',methods=['POST'])
def login_form_data():
    num1=request.form['a_val']
    num2=request.form['b_val']
    return {'response':int(num1)+int(num2)}

@app.route('/addition',methods=['GET'])
def addition():
    return render_template('addition.html')

@app.route('/addition-form',methods=['POST'])
def addition_form():
     num1=request.form['a_val']
     num2=request.form['b_val']
     return [int(num1)+int(num2)]

@app.route('/substraction',methods=['GET'])
def substraction():
    return render_template('substraction.html')

@app.route('/substraction-form',methods=['POST'])
def substraction_form():
     num1=request.form['a_val']
     num2=request.form['b_val']
     return [abs(int(num1)-int(num2))]


@app.route('/division',methods=['GET'])
def division():
    return render_template('division.html')

@app.route('/division-form',methods=['POST'])
def division_form():
     num1=request.form['a_val']
     num2=request.form['b_val']
     return [(int(num1)/int(num2))]

@app.route('/multiplication',methods=['GET'])
def multiplication():
    return render_template('multiplication.html')

@app.route('/multiplication-form',methods=['POST'])
def multiplication_form():
     num1=request.form['a_val']
     num2=request.form['b_val']
     return [(int(num1)*int(num2))]



app.run()
