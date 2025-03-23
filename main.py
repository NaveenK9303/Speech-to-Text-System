import speech_recognition as sr  # Import the SpeechRecognition library for speech-to-text conversion

def recognize_speech_from_mic():
    """
    Captures audio from the microphone and converts it to text using Google's speech recognition API.
    """
    recognizer = sr.Recognizer()  # Initialize the recognizer to process audio
    with sr.Microphone() as source:  # Use the default microphone as the audio source
        print("🎤 Speak now...")  # Prompt user to speak
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise to improve accuracy
        audio = recognizer.listen(source)  # Capture the audio input from the microphone

    try:
        text = recognizer.recognize_google(audio)  # Convert the captured speech to text using Google API
        print("📝 Recognized Speech:", text)  # Print the recognized text
        return text  # Return the transcribed text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")  # Error handling if speech is not clear
    except sr.RequestError:
        print("⚠️ Could not request results from Google Speech Recognition service.")  # API request failure

def recognize_speech_from_audio(file_path):
    """
    Converts an audio file (.wav format) to text using speech recognition.
    """
    recognizer = sr.Recognizer()  # Initialize the recognizer
    with sr.AudioFile(file_path) as source:  # Open the specified audio file
        print(f"🎵 Processing audio file: {file_path}")  # Notify user about file processing
        audio = recognizer.record(source)  # Read the entire audio file into memory

    try:
        text = recognizer.recognize_google(audio)  # Convert speech to text
        print("📝 Recognized Text from File:", text)  # Print the recognized text
        return text  # Return the transcribed text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio file.")  # Handle cases where audio is unclear
    except sr.RequestError:
        print("⚠️ Could not request results from Google Speech Recognition service.")  # Handle API request failure

# Example Usage
if __name__ == "__main__":  # Ensure the script runs only when executed directly
    choice = input("Choose input method: 1 for Microphone, 2 for Audio File: ")  # Ask user for input method

    if choice == "1":
        recognize_speech_from_mic()  # Convert speech from microphone to text
    elif choice == "2":
        file_path = input("Enter the path to the audio file (.wav format): ")  # Ask user for the file path
        recognize_speech_from_audio(file_path)  # Convert speech from audio file to text
    else:
        print("❌ Invalid choice! Please select 1 or 2.")  # Handle invalid input
