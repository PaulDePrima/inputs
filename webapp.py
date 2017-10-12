from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')
@app.route("/fir")
def render_page1():
    return render_template('first.html')
@app.route("/sec")
def render_page2():
    return render_template('second.html')
@app.route("/thi")
def render_page3():
    return render_template('third.html')

@app.route("/response")
def render_response():
        ins = float(request.args['inches'])
        #The request object stores information that was sent by the client to the server.
        #the args is a multidict
        #the way we get info from args is that it is visible in a url. - the information in args is visible in the url for hte page being requested(ex. .../response?color=blue)
        res = str((ins-32)*5/9)
        return render_template('response.html', their = request.args['inches'], response = res)
@app.route("/responsetwo")
def render_responsetwo():
        ins = float(request.args['inches'])
        #The request object stores information that was sent by the client to the server.
        #the args is a multidict
        #the way we get info from args is that it is visible in a url. - the information in args is visible in the url for hte page being requested(ex. .../response?color=blue)
        res = str(ins*9/5+32)
        return render_template('responsetwo.html', their = request.args['inches'], response = res)
@app.route("/responsethree")
def render_responsethree():
        ins = float(request.args['miles'])
        #The request object stores information that was sent by the client to the server.
        #the args is a multidict
        #the way we get info from args is that it is visible in a url. - the information in args is visible in the url for hte page being requested(ex. .../response?color=blue)
        res = str(ins+273.15)
        return render_template('responsethree.html', their = request.args['miles'], response = res)
