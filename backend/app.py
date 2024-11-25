from flask import Flask, request, jsonify
import subprocess
import matrix_ops #The C++ module built with pybind11

app = Flask(__name__)

#Example: Calling Java for recommendations
def call_java_recommendations(user_id):
    result = subprocess.run(
        ['java', '-cp', './backend', 'RecommendationLogic', str(user_id)],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    #Call Java for recommendations
    recommendations = call_java_recommendations(user_id)
    return jsonify({'recommendations': recommendations})
@app.route('/similarity', methods=['POST'])
def similarity():
    data = request.json
    vec1, vec2= data['vec1'], data['vec2']
    sim = matrix_ops.cosine_similarity(vec1, vec2)
    return jsonify({'similarity': sim})

if __name__ == '__main__':
    app.run(debug=True)