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
    result = core.run_query("SELECT text FROM chatbot WHERE isQuestion = 1")

    # Convert result to array
    questions = []
    for index, row in result.iterrows():
        questions.append(row['text'])



isQuestion('yeet')

# Disconnect from server
core.disconnect()
