from flask import Flask , render_template , jsonify
app = Flask(__name__)

JOBS = [
    {'id':1,
     'title':'Software Engineer',
     'location':'New York, NY',
     'salary':'$120,000'},
    {
        'id':2,
        'title':'Data Scientist',
        'location':'San Francisco, CA',
        'salary':'$130,000'},
    {
        'id':3,
        'title':'Web Developer',
        'location':'Austin, TX',
        'salary':'$110,000'},
    {
        'id':4,
        'title':'Product Manager',
        'location':'Remote',
        'salary':'$140,000' },
    
    {
        'id':5,
        'title':'AI Engineer',
        'location':'Seattle, WA',
        'salary':'$120,000'}
    ]
@app.route("/")
def hello_world():
    return render_template("home.html",jobs = JOBS,company_name = "Code with Arman") #render_template is used to render the html file
#render_template is used to render the html file

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS) #jsonify is used to convert the python object to json format
# print(__name__)
if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug = True)
