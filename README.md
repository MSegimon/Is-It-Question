# Is It Question
This program server to determine wether a sentence is a question or not. It does this by comparing the means of the cosine similarities between the sentence that you are trying to check and a database of predetermined questions and not questions.
## Next Steps
The next step of this project would be to further train the program by feeding it more sentences. This would not only help the accuracy of the program but it would also help me better determine the threshold value for the percentage difference of the two means.
## Get It Running
Assuming that you already have a remote database. Given that this program connect the a database through an sshtunnel you don't have to worry about any remote access setup. Then all you need to do is set up a table in your remote database and then install the necessary libraries to run the code.

`pip install pandas pymysql logging sshtunnel`