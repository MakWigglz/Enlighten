def get_knowledge(topic, subtopic):
    # This function will contain the map of "if" statements and conditions
    # for accessing the knowledge in the database about each topic and subtopic

    if topic == "Science":
        if subtopic == "Physics":
            return "Knowledge about Physics in Science"
        elif subtopic == "Chemistry":
            return "Knowledge about Chemistry in Science"
        # ... more conditions for other Science subtopics ...

    elif topic == "Geography":
        if subtopic == "Physical Geography":
            return "Knowledge about Physical Geography"
        elif subtopic == "Human Geography":
            return "Knowledge about Human Geography"
        # ... more conditions for other Geography subtopics ...

    # ... more conditions for other main topics ...

    else:
        return "Knowledge not found for the given topic and subtopic"