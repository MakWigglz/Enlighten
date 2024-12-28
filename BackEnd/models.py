class Topic:
    def __init__(self, name, subtopics):
        self.name = name
        self.subtopics = subtopics

topics = {
    "Science": Topic("Science", ["Physics", "Chemistry", "Biology", "Computer Science"]),
    "Geography": Topic("Geography", ["Physical Geography", "Human Geography", "Cartography", "Climatology"]),
    "History": Topic("History", ["Ancient Civilizations", "Middle Ages", "Modern Era", "World Wars"]),
    "Economics": Topic("Economics", ["Microeconomics", "Macroeconomics", "International Economics", "Economic Policy"]),
    "Astronomy": Topic("Astronomy", ["Solar System", "Stars", "Galaxies", "Cosmology"])
}