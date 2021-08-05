import pandas as pd
import numpy as np

# Other files
import core
import cosineSimilarity
import otherFunctions


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

    # Getting means of both similarities
    questionsMean = questionsSum / len(questions)
    answersMean = answersSum / len(answers)

    # check if it is question
    if otherFunctions.percentageDiff(questionsMean, answersMean) <= 40:
        print('Unknown')
    elif questionsMean > answersMean:
        print('its a question')
    elif answersMean > questionsMean:
        print('it is not a question')


isQuestion('this is america')

# Disconnect from server
core.disconnect()
