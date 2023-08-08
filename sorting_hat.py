# call Q&A from the prompt list below, ask user each question while tallying each response to a HP house, then finally report the house the user belongs to.
def main():

    global griffindor
    global hufflepuff
    global ravenclaw
    global slytherin

    griffindor = 0
    hufflepuff = 0
    ravenclaw = 0
    slytherin = 0

    print("Hello! I am the sorting hat. I will ask you a series of questions to determine which Hogwarts house you belong in.\n")

    for prompt in prompt_list:
    
        user_response = ""
        
        print("\n", prompt["question"] + "\n", prompt["options"] + "\n", sep = "")
    
        while user_response != "A" or "B" or "C" or "D":
        
            user_response = input("Enter your response: ").strip().upper()

            if user_response == "A":
                griffindor += 1
                break
            elif user_response == "B":
                hufflepuff += 1
                break
            elif user_response == "C":
                ravenclaw += 1
                break
            elif user_response == "D":
                slytherin += 1
                break
            else:
                print("Please enter A, B, C, or D: ")

        ## option to print out summary as you go along
        ## print(f"\nTotal so far:\nGriffindor: {griffindor}\nHufflepuff: {hufflepuff}\nRavenclaw: {ravenclaw}\nSlytherin: {slytherin}\n")
    
    print("\nHmm, yes. I have made my final determinaton. You belong to...\n")

    if griffindor > hufflepuff and griffindor > ravenclaw and griffindor > slytherin:
        print("GRIFFINDOR!!!")
    elif hufflepuff > ravenclaw and hufflepuff > slytherin and hufflepuff > griffindor:
        print("HUFFLEPUFF!!!")
    elif ravenclaw > slytherin and ravenclaw > griffindor and ravenclaw > hufflepuff:
        print("RAVENCLAW!!!")
    else:
        print("SLYTHERIN!!!")
    
# list of questions the hat can ask
prompt_list = [
    {
        "question": "What do you value most in yourself?",
        "options": "A: Bravery and courage\nB: Loyalty and patience\nC: Intelligence and wisdom\nD: Ambition and cunning"
    },
    {
        "question": "How do you handle challenges?",
        "options": "A: Face them head-on with determination\nB: Seek help and support from friends and family\nC: Analyze the situation and come up with a strategic plan\nD: Use any means necessary to overcome them"
    },
    {
        "question": "Which animal would you choose as your companion?",
        "options": "A: Lion\nB: Badger\nC: Eagle\nD: Serpent"
    },
    {
        "question": "What kind of people do you admire the most?", 
        "options": "A: Those who show bravery and heroism\nB: Those who are loyal and kind-hearted\nC: Those who are intelligent and knowledgeable\nD: Those who are ambitious and resourceful"
    },
    {
        "question": "How do you prefer to spend your free time?",
        "options": "A: Engaging in adventurous activities and sports\nB: Spending time with close friends and family\nC: Reading and learning new things\nD: Pursuing your goals and ambitions"
    },
    {
        "question": "Which of these qualities do you think is most important for a leader?",
        "options": "A: Fearlessness and determination\nB: Fairness and compassion\nC: Intelligence and creativity\nD: Ambition and the ability to make tough decisions"
    },
    {
        "question": "What type of environment do you feel most comfortable in?",
        "options": "A: Exciting and challenging situations\nB: A close-knit and supportive community\nC: An intellectually stimulating and academically oriented setting\nD: A place where you can exercise influence and power"
    },
    {
        "question": "What kind of books would you most likely choose to read?",
        "options": "A: Adventure and action-packed stories\nB: Tales of friendship and loyalty\nC: Books filled with knowledge and riddles\nD: Stories about achieving greatness and success"
    },
    {
        "question": "What is your favorite element?",
        "options": "A: Fire\nB: Earth\nC: Air\nD: Water"
    },
    {
        "question": "Which house do you think you'd enjoy the most?",
        "options": "A: Gryiffindor\nB: Hufflepuff\nC: Ravenclaw\nD: Slytherin"
    }
]
    
main()