
#import flask

from flask import Flask, render_template


#set up our application
app=Flask(__name__)

#create an index route
app.route('./')
def home():
    data="This is our home page"
    return render_template('index.html', datum=data)
    

app.route('/about')
def about():
    return "<h1> About Page <h1>"

app.route('/contact')
def contact():
    return "<h2> Contact us <h2>"

if __name__=='__main__':
    app.run(debug=1)
    