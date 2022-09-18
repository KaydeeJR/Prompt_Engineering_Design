"""
ENDPOINTS:
/bnewscore - for scoring  breaking news that may lead to public unrest
/jdentities - for extracting entities from job description
"""
import os

import cohere
from flask import Flask, request, jsonify
import extract_job_det


co = cohere.Client(os.getenv('cohere_classification'))

# create an instance of the Flask class
app = Flask(__name__)

# list of items
items = []

@app.route('/bnewscore', methods=['GET', 'POST'])
def clasification_route():
    """Classification"""
    if request.method == 'GET':
        # push the item to the list
        items.append(request.get_json())
        # return the created item
        return jsonify({
            "status": "success",
            "item": request.get_json()
        })
        # return jsonify({"status": "success", "message": "Post item!"})
    elif request.method == 'POST':
        company = request.get_json()['company']
        product_name = request.get_json()['product_name']
        type = request.get_json()['type']
        unique_ch = request.get_json()['unique_ch']
        
        # construct final string from input
        final = f"Company: {company}\nProduct Name: {product_name}\nWhat is it: {type}\nWhy is it unique: {unique_ch}\nDescription:"
        
        res = extract_job_det.extract_job_desc()
        # remove --SEPARATOR-- if x contains it
        if '--SEPARATOR--' in res:
            res = res.replace('--SEPARATOR--', '')
        
        return jsonify({"status": "success", "brand_description": res})
        # return jsonify({"status": "sucess", "message": "Get Route for items!"})
    return jsonify({
                "status": "success",
                "message": "Hello, world!"
                })


@app.route('/jdentities', methods=['GET', 'POST'])
def description_route():
    """Description"""
    if request.method == 'GET':
        # push the item to the list
        items.append(request.get_json())
        # return the created item
        return jsonify({
            "status": "success",
            "item": request.get_json()
        })
    elif request.method == 'POST': 
        jobs_desc_text = request.get_json()['jobs_description_text']
        product_name = request.get_json()['product_name']
        type = request.get_json()['type']
        unique_ch = request.get_json()['unique_ch']
        
        # construct final string from input
        final = f"Jobs Description Text: {jobs_desc_text}"
        result = extract_job_det.extract_job_desc(final)
        # remove --SEPARATOR-- if x contains it
        if '--SEPARATOR--' in result:
            result = result.replace('--SEPARATOR--', '')
        return jsonify({"status": "success", "extracted job details": result})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', debug=True, port=port)