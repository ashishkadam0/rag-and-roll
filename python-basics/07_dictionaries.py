copilot_response = {
    "user": "Ashish",
    "projects": [
        {
            "name": "AI Engineer Journey",
            "progress": {
                "python": {
                    "completed_topics": [
                        "Variables",
                        "Strings",
                        "Input",
                        "Lists",
                        "Loops",
                        "Functions",
                        "Dictionaries"
                    ]
                }
            }
        }
    ]
}

print(copilot_response)
print(copilot_response["user"])
print(copilot_response["projects"][0]["name"])
print(copilot_response["projects"][0]["progress"]["python"]["completed_topics"])