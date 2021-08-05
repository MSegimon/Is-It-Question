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

    # Convert question and answer result to arrays
    questions = []
    answers = []
    for index, row in questionsResult.iterrows():
        questions.append(row['text'])

    for index, row in answersResult.iterrows():
        answers.append(row['text'])

    # Get the sum of cosine similarities
    questionsSum = 0.0
    answersSum = 0.0
    for string in questions:
        questionsSum += cosineSimilarity.cosineSimilarity(text, string)
    
    for string in answers:
        answersSum += cosineSimilarity.cosineSimilarity(text, string)

    print(questionsSum)
    print(answersSum)


isQuestion('what is the answer to life')

# Disconnect from server
core.disconnect()
