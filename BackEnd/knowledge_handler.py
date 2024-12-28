from .models import topics

def get_knowledge(topic, subtopic):
    knowledge_base = {
        "Science": {
            "Physics": "Knowledge about Physics in Science",
            "Chemistry": "Knowledge about Chemistry in Science",
            "Biology": "Knowledge about Biology in Science",
            "Computer Science": "Knowledge about Computer Science"
        },
        "Geography": {
            "Physical Geography": "Knowledge about Physical Geography",
            "Human Geography": "Knowledge about Human Geography",
            "Cartography": "Knowledge about Cartography",
            "Climatology": "Knowledge about Climatology"
        },
        "History": {
            "Ancient Civilizations": "Knowledge about Ancient Civilizations",
            "Middle Ages": "Knowledge about the Middle Ages",
            "Modern Era": "Knowledge about the Modern Era",
            "World Wars": "Knowledge about World Wars"
        },
        "Economics": {
            "Microeconomics": "Knowledge about Microeconomics",
            "Macroeconomics": "Knowledge about Macroeconomics",
            "International Economics": "Knowledge about International Economics",
            "Economic Policy": "Knowledge about Economic Policy"
        },
        "Astronomy": {
            "Solar System": "Knowledge about the Solar System",
            "Stars": "Knowledge about Stars",
            "Galaxies": "Knowledge about Galaxies",
            "Cosmology": "Knowledge about Cosmology"
        }
    }

    if topic in knowledge_base and subtopic in knowledge_base[topic]:
        return knowledge_base[topic][subtopic]
    else:
        return f"Knowledge not found for the topic '{topic}' and subtopic '{subtopic}'"

def get_subtopics(topic):
    if topic in topics:
        return topics[topic].subtopics
    else:
        return []

def get_all_topics():
    return list(topics.keys())