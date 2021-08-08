# Is It Question
This is a program that will help servers determine whether a sentence is a question or not. It does this by comparing the means of the cosine similarities between the sentence that is being checked, and a database of sentences that have been classified as being either questions, or as not being questions. It was developed for my chatbot.
## Next Steps
The next step of this project would be to further train the program by feeding it more sentences. This would not only help the accuracy of the program but it would also help me better determine the threshold value for the percentage difference of the two means. It would also be a good idea to test other similar programs, however this is not a high priority at the moment.
## Get It Running
Assuming that you already have a remote database, then given that this program connects to the database through an sshtunnel, you don't have to worry about any remote access setup. Then all you need to do is set up a table in your remote database and install the necessary libraries to run the code.

`pip install pandas pymysql logging sshtunnel`
