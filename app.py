from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    render_template('writings.html')

