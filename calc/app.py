from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def calc_page():
    return '''
    <h1>Welcome to my calculator</h1>
    <h1>Add</h1>
    <form method='POST'>
    <select Name="calc" Size="4">  
  <option>add</option>  
  <option>sub</option>  
  <option>mult</option>  
  <option>div</option>  
</select>  
        <input type='text' placeholder='first num' name='number1'/>
        <input type='text' placeholder='second num' name='number2'/>
    <button>Submit</button>
    </form>
    '''


@app.route('/',methods=['POST'])
def calc_1():
    a = int(request.form.get('number1', 1))
    b = int(request.form.get('number2', 1))
    data3 = request.form.get('calc', 'add')

    # a=int(request.form('number1'))
    # b=int(request.form('number2'))
    # calc=request.form('calc')
    if data3=='add':
        return str(add(a,b))
    elif data3 == 'sub':
        return str(sub(a,b))
    elif data3 == 'mult':
        return str(mult(a,b))
    elif data3 == 'div':
        return str(div(a,b))

def add(a, b):
    """Add a and b."""
    return a + b

def sub(a, b):
    """Substract b from a."""
    return a - b

def mult(a, b):
    """Multiply a and b."""
    return a * b

def div(a, b):
    """Divide a by b."""
    return a / b