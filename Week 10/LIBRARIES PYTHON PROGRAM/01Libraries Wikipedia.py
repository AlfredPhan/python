#Week - 10 Python Libraries 
#Program No-1 Displaying the contents from wiki page

import wikipedia  # for accessing Wikipedia pages

query = "Culture of Vietnam"
results = wikipedia.summary(query, sentences=3)
print(results)


