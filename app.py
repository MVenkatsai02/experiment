from flask import Flask, request, jsonify
from flask_cors import CORS 

from utils import search_articles, concatenate_content, generate_answer
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

app = Flask(__name__)
CORS(app)  

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get("query", "")
    print("Received query: ", user_query)

    try:
        print("Step 1: searching articles")
        articles = search_articles(user_query)

        print("Step 2: concatenating content")
        content = concatenate_content(articles)

        print("Step 3: generating answer")
        answer = generate_answer(content, user_query)

        return jsonify({"answer": answer})

    except Exception as e:
        print("Exception occurred:")
        traceback.print_exc()  
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
