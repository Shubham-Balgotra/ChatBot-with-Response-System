import re
#import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sorry...I am under building stage.",
                "Pardan !",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(6)]
    return response


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)


    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi','hii','hiii', 'hey', 'sup', 'heyo', 'hay'], single_response=True)
    response('The weather is unpredictable now a days. Sometime its sunny and sometime its rain heavily.',['weather','sun','rain'],single_response=True, required_words=['weather','wather','sun','rain'])
    response('I was build by Shubham (AI engineer) using python v3.11.4.', ['build', 'built'],single_response=True, required_words=['build you', 'built you'])
    response('I was develop by Shubham (AI engineer) using python v3.11.4.', ['develop', 'developed'],single_response=True, required_words=['develop you', 'developed you'])
    response('I was created by Shubham (AI engineer) using python v3.11.4.', ['create', 'created', 'creates'],single_response=True, required_words=['create you','create you', 'created you'])
    response('See you! Have a great day.', ['bye', 'goodbye','tata'], single_response=True)
    response('Thats good to hear. I hope you be great every day :-)', ['happy', 'good', 'fine', 'great'],single_response=True, required_words=['happy','great', 'good', 'fine'])
    response("I'm doing fine, and you?", ['hows', 'you'],single_response=True)
    response('I\'m doing fine, and you?', ['whats', 'up'], single_response= True)
    response("No, as an assistant I can't sing.", ['sing'],single_response=True, required_words=['sing'])
    response('You\'re welcome!', ['thank', 'thanks','thankyou', 'thank you'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Longer responses
    response(R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Type 'goodbye' to exit chat
# Testing the response system
while True:
    user_input = input('You: ')
    if user_input.lower() == 'goodbye':
        print('Jarvis: Nice meeting you! Have a good day!')
        break
    response = get_response(user_input)
    print('Jarvis: ' + response)


