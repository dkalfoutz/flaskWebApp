from flask import Flask, render_template, request, redirect, escape 
#from flask import redirect
from vsearch import search4letters
#module's name: flask, class' name: Flask
#to use the Flask's built-in request object,
#import it on the from flask line
#The request object contains a dictionary
#attribute called form that provides access
#to a HTML form's data posted from the browser.
#prosvasi sta key-value tou form leksikou:
#request.form["Phrase"]
#request.form["Letters"]
#dld, ta "Phrase", "Letters" einai ta values
#kai ta keys twn, oi times tous einai to text
#pou tha eisagw egw sta antistoixa pedia tis formas
#gia tin leksi kai ta grammata pou tha psaksw ta 
#koina tous simeia. 







#create an instance of a Flask objekt 
#and assign it to "app"
#__name__ : the name of the  currently
#active module

#SOS#

#The Flask class needs to know the current
#value of __name__ when creating a new Flask
#objekt, so it must be passed as an argument.
app = Flask(__name__)

###############################################
###############################################
####### PARATHRHSH!!! ########################
#The route decorator lets you associate a URL web
#path with an existing Python function. In this 
#case, the URL “/” is associated with the function
#defined on the very next line of code, which is
# called hello.

# The route decorator arranges for
# the Flask web server to call the function when a
#request for the “/” URL arrives at the server. 

#The route decorator then waits for any output 
#produced by the decorated function before 
#returning the output to the server, which then
# returns it to the waiting web browser.
######## PARATHRHSH !! #######################
##############################################
##############################################




#########################################
######SOS SOS SOS SOS################
##### Rendering Templates from Flask #######
#Flask comes with a function called render_template,
# which, when provided with the name of a template
# and any required arguments, returns a string of HTML
# when invoked. To use render_template, add its name
#to the list of imports from the flask module (at the
# top of your code), then invoke the function as needed.
###### SOS SOS SOS SOS ################
############################################

#FUNCTION: eisodos: flask_request: objekt, res: str:
#ta koina simeia twn dio inputs 
def log_request(req: "flask_request:", res: str) -> None:
	#anoigw to arxeio vsearch.log ws append leitourgeia, 
	#kai eisagw entos tou to res, diladi ta koina simeia
	#twn 2 input tou xristi, kai epistrefei to apotelesma tou fakelou se ena
	#objekt, to legomeno file stream, sto epilegen onoma
	#log.
	with open("vsearch.log", "a") as log:
		#print(str(dir(req)), res, file = log)
		print(req.form, req.remote_addr, req.user_agent, res, file = log, sep = "|")

"""
@app.route("/")
def hello() -> "302":
	#return "hello world from Flask!"
	return redirect("/entry")
"""

@app.route('/search4', methods = ["POST"])
def do_search() -> 'html':
	phrase = request.form['phrase']
	letters = request.form['letters']
	title = 'Here are your results:'
	results = str(search4letters(phrase, letters))
	#twra p egine invoke t en logw URL, thelw to 
	#string me ta koina grammata (ap t 2 input
	#pou edwse o xristis) na to perasw ws orisma
	#kalwntas t funtion pou orisa pio panw, kai h
	#opoia anoigei to log kai eisagei t string afto
	#me ta koina grammata. 
	log_request(request, results)
	return render_template('results.html',
							the_title=title,
							the_phrase=phrase,
							the_letters=letters,
							the_results=results,)
	#print("byee")
	#return render_template("results.html")
	#return str("hello")


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
	return render_template("entry.html", the_title = "Welcome to search4letters on the web!")


#add support for the /viewlog URL to my webapp. When my 
#webapp receives a request for /viewlog, it should open the 
#vsearch.log file, read in all of its data, and then send the
#data to the waiting browser. 
@app.route("/viewlog")
def view_the_log() -> str: 
	#no input
	#return a string to its caller; the string will be
	#concatenation of all of the lines of data from the
	#vsearch.log file. 
	with open("vsearch.log") as log:
		#read all the lines from the file. 
		#No need to loop through the file, reading each line.
		#read method: returns the entire contents of the file 
		#"in one go".
		contents = log.read()

	#with "with", the file closes. Ready to send the
	#data back to the waiting browser.
	return escape(contents) #afairese ta < kai >
							#k vale lt kai gt

#The final line of code takes the Flask object 
#assigned to the app variable and asks
#Flask to start running its web server. It does
# this by invoking run:
if __name__ == '__main__':
	app.run(debug = True)
