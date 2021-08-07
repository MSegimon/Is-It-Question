# Is It Question
This program server to determine wether a sentence is a question or not. It does this by comparing the means of the cosine similarities between the sentence that you are trying to check and a database of predetermined questions and not questions. It was developed for my chatbot.
## Next Steps
The next step of this project would be to further train the program by feeding it more sentences. This would not only help the accuracy of the program but it would also help me better determine the threshold value for the percentage difference of the two means. It would also be a good idea to test other types of similarity programs, but this is not high priority at the moment.
## Get It Running
Assuming that you already have a remote database. Given that this program connect the a database through an sshtunnel you don't have to worry about any remote access setup. Then all you need to do is set up a table in your remote database and then install the necessary libraries to run the code.

`pip install pandas pymysql logging sshtunnel`