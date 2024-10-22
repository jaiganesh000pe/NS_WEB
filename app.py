from flask import Flask, render_template ,request, redirect

app = Flask(__name__)







@app.route("/", methods=['GET', 'POST'])
def home():
    
    name12 = ''
    name1 = ''
    pass12 = ''
    if request.method == 'POST':
        ns12 = request.form['ns']
        name12 = request.form['nsemail']
        pass12 = request.form['nspass']
        

        if name12 == 'ns@mamil.com' and pass12 == "1234":
            return redirect('/home/'+ns12)
        else:
            return redirect('/erorr1/'+ns12)
    
        
    return render_template('index.html', nsname=name12 ,name1 =name1)


@app.route("/home/<ns12>" , methods=['GET', 'POST'])
def page1(ns12):
    return render_template('page1.html',ns12 = ns12)


@app.route("/erorr1/<ns12>" , methods=['GET', 'POST'])
def eroor(ns12):
    return render_template('erorr.html',ns12 = ns12)

if __name__ == '__mani__':
    app.run(debug=True)