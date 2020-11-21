from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/output', methods=['POST'])
def output():
    your_name = request.form['name']
    return redirect(url_for('redirect_test', name=your_name))


@app.route('/redirect_test', methods=['GET'])
def redirect_test():
    your_name = request.args.get('name', '')
    return render_template('output.html', name=your_name)


if __name__ == '__main__':
    app.run(debug=True)
