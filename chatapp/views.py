from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from django.shortcuts import render

# Create your views here.


#initialize the lemmatizer and stopwords
lemmatizer = WordNetLemmatizer() 
stop_words = set(stopwords.words('english'))

@api_view(['POST'])
def chatbot(request):
    # getting users request POST request
    message = request.data['message']
    
    #tokenize the users message
    words = nltk.word_tokenize(message.lower())
    
    #remove stop words from the users  message
    words = [word for word in words if word not in stop_words]
    
    # lemmatize the remaining words in the users message
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # determine the chatbots response based on the users message
    response = 'Hello, how can I help you?'
    if 'help' in words:
        response = 'Sure, what do you need help with?'
    elif 'problem' in words:
        response = 'What seems to be your problem?'
    elif 'thanks' in words or 'thank you' in words:
        response = "You\'re welcome!"
        
    # return the chatbots response
    return Response({message:response})
    