class Topic:
    def __init__(self, name, subtopics):
        self.name = name
        self.subtopics = subtopics

topics = {
    "Philosophy": Topic("Philosophy", ["Metaphysics", "Epistemology", "Ethics"]),
    "Science": Topic("Science", ["Physics", "Biology", "Chemistry"]),
    "Art": Topic("Art", ["Painting", "Sculpture", "Music"]),
    "History": Topic("History", ["Ancient", "Medieval", "Modern"]),
    "Literature": Topic("Literature", ["Poetry", "Prose", "Drama"])
}