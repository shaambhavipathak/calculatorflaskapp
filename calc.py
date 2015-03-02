"""simple calculator flask application"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculatorapp', methods=['GET', 'POST'])
def calculate():

    if request.method == 'POST':
        if request.form['choice'] == 'add':
            SUM = float(request.form['n1'])+float(request.form['n2'])
            return ''' The sum of two no is ''' + str(SUM)
        elif request.form['choice'] == 'substract':
            SUB = float(request.form['n1'])-float(request.form['n2'])
            return ''' The substraction of two no is ''' + str(SUB)
        elif request.form['choice'] == 'multiply':
            MUL = float(request.form['n1'])*float(request.form['n2'])
            return''' The Multiplication of two no is ''' + str(MUL)
        elif request.form['choice'] == 'divide':
            DIV = float(request.form['n1'])/float(request.form['n2'])
            return ''' The Division of two no is ''' + str(DIV)
        else:
            return ''' Please Select correct option '''
    else:
      return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
