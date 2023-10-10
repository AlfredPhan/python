#Program no-5 
import textblob  # for sentiment analysis
#natural language processing -> Machine Learning

def print_sentiment(text):
    analysis = textblob.TextBlob(text)
    print(f"{text:30}: {analysis.sentiment}")
#positive & negative & neutral (MATLAB)Voice recognition

print_sentiment("I am happy") #polarity and subjectivity
print_sentiment("I think she is bit depressed")
print_sentiment("The temperature is 10 degrees")
print_sentiment("I think it is very cold")
print_sentiment("I don't think I will buy this product because my previous expereince wasn't good")



                
