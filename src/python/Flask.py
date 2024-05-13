import json
import KeyYearMonthSearch
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    result = KeyYearMonthSearch.key_search(keyword)
    return result
if __name__ == '__main__':
    app.run(debug=True)
