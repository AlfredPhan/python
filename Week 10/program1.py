#Week 10 Python Libraries
#Program No.1 Displaying the contents from wiki page

import wikipedia #for accessing Wekipedia pages

query = "Tradition of Vietnam"
results = wikipedia.summary(query,sentences = 3)
print(results)
