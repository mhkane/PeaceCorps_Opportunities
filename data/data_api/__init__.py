from flask import Flask, request, render_template, jsonify, current_app
from functools import wraps
import json, math

DB_KEYS = ['location', 'sector']

app = Flask(__name__)
 
def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f().data) + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function
 

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/all_jobs')
@support_jsonp
def all_jobs():
    jobs = None
    with open('data/pc.json') as f:
        jobs = json.load(f)
    return jsonify({'data':jobs})


@app.route('/get_jobs')
@support_jsonp
def get_jobs():
    specs = request.args

    # ImmutableMultiDict([ ('location', u'Uganda'), ('_', u'1392546022396')])
    all_jobs = None
    with open('data/pc.json') as f:
        all_jobs = json.load(f)


    def sifter(job):
        for k, v in specs.items():
            print key
            if (key in DB_KEYS) and (not v == ''):
                values = v.split('+')
                if (not job[k]) or (job[k] not in v):
                    return False
        return True

    jobs = filter(sifter, all_jobs)
    return jsonify({'data':jobs})


@app.route('/foo')
def foo():
    return "hi"



if __name__ == '__main__':
    app.run(debug=True)