# Enlighten

Certainly! Here's a detailed step-by-step plan for this project, followed by a pseudocode outline:

Step-by-Step Plan:

1. Project Setup:
   a. Create a new directory for your project.
   b. Set up a virtual environment for Python.
   c. Install Flask and any other required dependencies.

2. Backend Development:
   a. Create the models.py file with the Topic class and topics dictionary.
   b. Develop the Flask application (app.py) with routes for the main page, subtopics, and content.
   c. Implement placeholder functions for database interactions (to be replaced later).

3. Frontend Development:
   a. Create the HTML template (index.html) with the pentagram structure.
   b. Develop the CSS file (style.css) to style the pentagram and other UI elements.
   c. Write the JavaScript file (main.js) to handle user interactions and API calls.

4. Pentagram UI:
   a. Implement the pentagram layout in HTML and CSS.
   b. Use JavaScript to position the topic points around the pentagram.
   c. Add click events to the pentagram points to display subtopics.

5. Subtopics and Content Display:
   a. Implement the subtopics display area in HTML.
   b. Create functions to fetch and display subtopics when a topic is clicked.
   c. Implement content display area and functions to show content when a subtopic is selected.

6. Database Integration:
   a. Choose and set up a database system (e.g., SQLite, PostgreSQL).
   b. Design the database schema for topics, subtopics, and content.
   c. Replace placeholder functions in app.py with actual database queries.

7. Testing:
   a. Write unit tests for backend functions.
   b. Perform integration testing of the full application.
   c. Conduct user testing and gather feedback.

8. UI/UX Improvements:
   a. Refine the pentagram design and overall layout.
   b. Add animations and transitions for a more dynamic user experience.
   c. Implement a color scheme and possibly add icons for topics and subtopics.

9. Deployment:
   a. Choose a hosting platform (e.g., Heroku, AWS).
   b. Set up the production environment.
   c. Deploy the application and perform final testing.

10. Documentation and Maintenance:
    a. Write documentation for the project setup and usage.
    b. Plan for ongoing maintenance and potential future features.

Pseudocode Outline:

```
// models.py
CLASS Topic
    PROPERTIES:
        name
        subtopics
    
    CONSTRUCTOR(name, subtopics):
        SET this.name = name
        SET this.subtopics = subtopics

DEFINE topics_dict AS DICTIONARY:
    "Science": ["Physics", "Chemistry", "Biology", "Computer Science"]
    "Geography": ["Physical Geography", "Human Geography", "Cartography", "Climatology"]
    "History": ["Ancient Civilizations", "Middle Ages", "Modern Era", "World Wars"]
    "Economics": ["Microeconomics", "Macroeconomics", "International Economics", "Economic Policy"]
    "Astronomy": ["Solar System", "Stars", "Galaxies", "Cosmology"]

DEFINE topics AS DICTIONARY:
    FOR EACH name, subtopics IN topics_dict:
        CREATE Topic(name, subtopics) AND ADD TO topics

// app.py
IMPORT Flask, render_template, jsonify
IMPORT topics FROM models

CREATE Flask application

DEFINE ROUTE '/':
    RENDER 'index.html' WITH topics.keys()

DEFINE ROUTE '/subtopics/<topic>':
    IF topic IN topics:
        RETURN JSON of topics[topic].subtopics
    ELSE:
        RETURN empty JSON list

DEFINE ROUTE '/content/<topic>/<subtopic>':
    // Placeholder for database query
    RETURN JSON with placeholder content

// main.js
WHEN document is loaded:
    GET pentagram element
    GET subtopics div
    GET content div

    POSITION pentagram points:
        FOR EACH point IN pentagram points:
            CALCULATE x and y based on index
            SET point position to x and y

    WHEN pentagram is clicked:
        IF clicked element is a point:
            GET topic from point's data attribute
            FETCH subtopics for topic from '/subtopics/<topic>'
            CLEAR subtopics div
            FOR EACH subtopic IN fetched subtopics:
                CREATE button for subtopic
                WHEN button is clicked:
                    FETCH content for subtopic from '/content/<topic>/<subtopic>'
                    DISPLAY content in content div
                ADD button to subtopics div

// HTML and CSS
CREATE HTML structure with pentagram, subtopics area, and content area
STYLE pentagram and other elements using CSS
```



###  Python file to have 5 Topic classes in a dictionary structure, and adjust the rest of the program files accordingly. I'll also provide a basic structure for the HTML and CSS to create a large pentagram UI.

1. Python Backend:

**File: /app/models.py**
```python
class Topic:
    def __init__(self, name, subtopics):
        self.name = name
        self.subtopics = subtopics

# Define your 5 main topics
topics_dict = {
    "Science": ["Physics", "Chemistry", "Biology", "Computer Science"],
    "Geography": ["Physical Geography", "Human Geography", "Cartography", "Climatology"],
    "History": ["Ancient Civilizations", "Middle Ages", "Modern Era", "World Wars"],
    "Economics": ["Microeconomics", "Macroeconomics", "International Economics", "Economic Policy"],
    "Astronomy": ["Solar System", "Stars", "Galaxies", "Cosmology"]
}

# Create Topic instances
topics = {name: Topic(name, subtopics) for name, subtopics in topics_dict.items()}
```

2. Flask Application:

**File: /app/app.py**
```python
from flask import Flask, render_template, jsonify
from models import topics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', topics=topics.keys())

@app.route('/subtopics/<topic>')
def get_subtopics(topic):
    if topic in topics:
        return jsonify(topics[topic].subtopics)
    return jsonify([])

@app.route('/content/<topic>/<subtopic>')
def get_content(topic, subtopic):
    # Here you would typically fetch content from a database
    # For this example, we'll return a placeholder
    return jsonify({"content": f"Content for {subtopic} in {topic}"})

if __name__ == '__main__':
    app.run(debug=True)
```

3. HTML Template:

**File: /app/templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Encyclopedia</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div id="app">
        <h1>Interactive Encyclopedia</h1>
        <div id="pentagram">
            {% for topic in topics %}
                <div class="point" data-topic="{{ topic }}">
                    <span>{{ topic }}</span>
                </div>
            {% endfor %}
        </div>
        <div id="subtopics"></div>
        <div id="content"></div>
    </div>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
```

4. CSS Styling:

**File: /app/static/css/style.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f0f0;
}

#app {
    width: 100%;
    max-width: 1200px;
    text-align: center;
}

#pentagram {
    position: relative;
    width: 90vw;
    height: 90vw;
    max-width: 90vh;
    max-height: 90vh;
    margin: 0 auto;
}

.point {
    position: absolute;
    width: 100px;
    height: 100px;
    background-color: #3498db;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: background-color 0.3s;
}

.point:hover {
    background-color: #2980b9;
}

.point span {
    color: white;
    font-weight: bold;
}

#subtopics, #content {
    margin-top: 20px;
}

button {
    margin: 5px;
    padding: 10px;
    cursor: pointer;
}
```

5. JavaScript for Interactivity:

**File: /app/static/js/main.js**
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const pentagram = document.getElementById('pentagram');
    const subtopicsDiv = document.getElementById('subtopics');
    const contentDiv = document.getElementById('content');

    // Position the points of the pentagram
    const points = document.querySelectorAll('.point');
    points.forEach((point, index) => {
        const angle = (index * 72 - 90) * Math.PI / 180;
        const x = 50 + 40 * Math.cos(angle);
        const y = 50 + 40 * Math.sin(angle);
        point.style.left = `${x}%`;
        point.style.top = `${y}%`;
    });

    pentagram.addEventListener('click', (event) => {
        const point = event.target.closest('.point');
        if (point) {
            const topic = point.dataset.topic;
            fetch(`/subtopics/${topic}`)
                .then(response => response.json())
                .then(subtopics => {
                    subtopicsDiv.innerHTML = '';
                    subtopics.forEach(subtopic => {
                        const subtopicBtn = document.createElement('button');
                        subtopicBtn.textContent = subtopic;
                        subtopicBtn.addEventListener('click', () => {
                            fetch(`/content/${topic}/${subtopic}`)
                                .then(response => response.json())
                                .then(data => {
                                    contentDiv.innerHTML = `<h2>${subtopic}</h2><p>${data.content}</p>`;
                                });
                        });
                        subtopicsDiv.appendChild(subtopicBtn);
                    });
                });
        }
    });
});
```

This modified version of the program now includes:

1. A Python backend with 5 topics in a dictionary structure.
2. A Flask application adjusted to work with the new topic structure.
3. An HTML template that sets up a pentagram structure.
4. CSS styling to create a large pentagram that takes up 90% of the webpage.
5. JavaScript that positions the topic points around the pentagram and handles user interactions.

The pentagram is created by positioning five circular divs (the points) around a central point. Each point represents a topic and can be clicked to display its subtopics.

To further improve the UI and make it more visually appealing:

1. You could add animations when transitioning between topics and subtopics.
2. Implement a color scheme that corresponds to each topic.
3. Add icons or images to represent each topic and subtopic.
4. Create a more detailed pentagram shape using SVG for better visual appeal.

Remember to replace the placeholder content in the `get_content` function with actual database queries when you're ready to connect to your knowledge database.