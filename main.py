import pandas as pd
import numpy as np

# Other files
import core
import cosineSimilarity


# Establish connection
core.connect()

# Main code
def isQuestion(text):
    result = core.run_query("SELECT text FROM chatbot WHERE isQuestion = 1")

    print(result[0])


isQuestion('yeet')

# Disconnect from server
core.disconnect()