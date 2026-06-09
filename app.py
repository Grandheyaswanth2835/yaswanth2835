from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {
        "id": 1,
        "title": "Flutter Basics",
        "instructor": "John"
    },
    {
        "id": 2,
        "title": "Python Flask",
        "instructor": "David"
    }
]

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

if __name__ == '__main__':
    app.run(debug=True)