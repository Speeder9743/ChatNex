# Import necessary libraries
import json
from difflib import get_close_matches
import pyttsx3
import speech_recognition as sr

#--------------INIT-------------
# Initialize TTS engine
engine = pyttsx3.init()

# Initialize recognizer
recognizer = sr.Recognizer()

# Set properties
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)

#-------------JSON Functions--------------
# Load knowledge base from JSON file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

# Save knowledge base to JSON file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

#------------Difflib Matching Functions--------------
# Find best match for user question
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.7)
    if matches:
        return matches[0]
    return None

# Get answer for question
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

# Main chat function that ties all the other functions together
def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    prompt_type_asked = False

    # Ask the user if they want to speak their inputs or type them
    while not prompt_type_asked:
        prompt_type = input("Choose input type (1 for speech, 2 for text): ")
        if prompt_type in ['1', '2']:
            prompt_type_asked = True
        # Error handling for invalid inputs (seriously, people? Don't type in "as;dlfkj as;dlfkj as;dlfkj asd;lfkj asd;flkj" for MEANINGFUL questions!)
        else:
            print("Invalid input. Please choose 1 for speech or 2 for text.")

    user_input = ""
    
    # Chat loop 
    while True:
        mic_input = 1
        if prompt_type == '1':
                try:
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source)
                        user_input = recognizer.recognize_google(audio)
                        print('>>>', user_input)
                        mic_input = 0
                except sr.UnknownValueError:
                    text = print("I couldn't hear what you were saying. Can you please speak clearly?")
                    engine.say(text)
                    engine.runAndWait()

        elif prompt_type == '2':
            user_input = input(">>> ")

        if user_input.lower() in [":q", "quit", "exit"]:
            break

        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
            engine.say(answer)
            engine.runAndWait()
        else:
            text = "I don't know the answer. Can you teach me?"
            print(text)
            engine.say(text)
            engine.runAndWait()
            # Get the user's response to teach the bot
            print('Say the answer or say "skip" to skip:')
            if prompt_type == '1':
                    try:
                        with sr.Microphone() as source:
                            recognizer.adjust_for_ambient_noise(source)
                            audio = recognizer.listen(source)
                            new_answer = recognizer.recognize_google(audio)
                            print(new_answer)
                            mic_input = 0
                    except sr.UnknownValueError:
                        text = print("I couldn't hear what you were saying. Can you please speak clearly?")
                        engine.say(text)
                        engine.runAndWait()

            elif prompt_type == '2':
                new_answer = input('Type the answer or "skip" to skip: ')

        # Because of the code logic, you get an UnboundLocalError when you don't say your response when the chatbot asks you to teach it. For this reason, we ignore the error using a try-except block here.
        try:
            if new_answer.lower() != 'skip':
                # Lowercase user_input before adding to knowledge base
                knowledge_base["questions"].append({"question": user_input.lower(), "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)

                print("Bot: Thank you! I learned something new!")
                engine.say("Thank you! I learned something new!")
                engine.runAndWait()
        except UnboundLocalError:
            pass

if __name__ == '__main__':
    chat_bot()

