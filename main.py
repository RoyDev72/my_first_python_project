import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

def speak(text):
    """
    Function to convert text to speech
    """
    engine.say(text)
    engine.runAndWait()

def listen():
    """
    Function to listen for user speech input
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-US")
        print(f"User: {query}")
        return query
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return None

# Example usage
speak("Hello! I am your voice assistant. How can I assist you today?")

while True:
    query = listen()
    if query:
        # Convert the query to lowercase for easier comparison
        query = query.lower()

        if "play" in query:
            song = query.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
        elif "search" in query:
            term = query.replace("search", "")
            speak(f"Searching for {term}")
            pywhatkit.search(term)
        elif "send message" in query:
            speak("To whom would you like to send a message?")
            recipient = listen()
            speak("What message would you like to send?")
            message = listen()
            pywhatkit.sendwhatmsg(recipient, message, 0, 0)  # Sending WhatsApp message
            speak("Message sent successfully!")
        elif "date" in query:
            date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"The current date is {date}")
        elif "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time}")
        elif "wikipedia" in query:
            search_query = query.replace("wikipedia", "")
            speak("Searching Wikipedia...")
            try:
                summary = wikipedia.summary(search_query, sentences=2)
                speak(f"According to Wikipedia, {summary}")
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Multiple results found. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, no information found for that query.")
        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "bye" in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that so. Can you please repeat?")
