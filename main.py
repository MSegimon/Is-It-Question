import pandas as pd
import numpy as np

# Other files
import core
import cosineSimilarity


# Establish connection
core.connect()

# Main code
def isQuestion(text):
    # Call server and get result
    questionsResult = core.run_query("SELECT text FROM chatbot WHERE isQuestion = 1")
    answersResult = core.run_query("SELECT text FROM chatbot WHERE isQuestion = 0")

    # Convert question result to array
    questions = []
    answers = []
    for index, row in questionsResult.iterrows():
        questions.append(row['text'])

    for index, row in answersResult.iterrows():
        answers.append(row['text'])

    print(answers)


isQuestion('yeet')

# Disconnect from server
core.disconnect()
