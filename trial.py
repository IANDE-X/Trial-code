import datetime


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print(color.BLUE, color.BOLD, '''Hello welcome Doctor Online , im here to help you with diagnosis whenever you ae sick
always feel free to ask me any question , im your assitant,
welcome, \n ''', color.END)
# prevention phrase
prevention = '''Hey,Protect yourself and others around you by knowing the facts and 
taking appropriate precautions. Follow advice provided by your local health authority. To prevent the 
spread of COVID-19: Clean your hands often. Use soap and water, or an alcohol-based hand rub. 
Maintain a safe distance from anyone who is coughing or sneezing. Wear a mask when physical 
distancing is not possible. Don’t touch your eyes, nose or mouth. Cover your nose and mouth with your 
bent elbow or a tissue when you cough or sneeze. Stay home if you feel unwell. If you have a fever, 
cough and difficulty breathing, seek medical attention. Calling in advance allows your healthcare 
provider to quickly direct you to the right health facility. This protects you, and prevents the 
spread of viruses and other infections. Masks Masks can help prevent the spread of the virus from the 
person wearing the mask to others. Masks alone do not protect against COVID-19, and should be 
combined with physical distancing and hand hygiene. Follow the advice provided by your local health 
authority. '''

print(color.BOLD + 'Hello World !' + color.END)
questions_ask = [
    "Have you travelled to a red covid zone before?\n 1.YES \n 2.NO \n 3.IM NOT SURE\n\n",
    "Do you feel fatigue?\n 1.YES\n 2.NO \n 3.A LITTLE \n\n",
    "Do you feel a cough, a dry throat or headache?\n 1.YES \n 2.NO\n 3.I FEEL A LITTLE DIZZY\n\n",
    "Do you have a difficulty in breathing?\n 1.YES\n 2.NO \n 3.A LITTLE \n\n",
]


class Maswali:
    def __init__(self, ask, answer):
        self.ask = ask
        self.answer = answer


questions_object = [
    Maswali(questions_ask[0], "1"),
    Maswali(questions_ask[1], "2"),
    Maswali(questions_ask[2], "1"),
    Maswali(questions_ask[3], "2"),
    # qes ojcets
]


# here is a function called run that  i use to run it
def run_questions(questions_object):  # functio
    score = 0  # counter
    for question in questions_object:
        student_answer = input(question.ask)  # variable jibu
        if student_answer == question.answer:
            score += 1
            if score >= 3:
                print("you got ", str(score), "/", str(len(questions_object)), "covid 19 symptoms\n hence we "
                                                                               "\n recomend that you qurantine yourself"
                                                                               " for 14 days")
            elif score < 2:
                print("You are safe from covid !")


run_questions(questions_object)

print(color.RED + color.BOLD + "Bold red string" + color.END)
questions_ask = [
    color.RED, color.BOLD,
    "Have you travelled to a red covid zone before?\n 1.YES \n 2.NO \n 3.IM NOT SURE\n\n",
    "Do you feel fatigue?\n 1.YES\n 2.NO \n 3.A LITTLE \n\n",
    "Do you feel a cough, a dry throat or headache?\n 1.YES \n 2.NO\n 3.I FEEL A LITTLE DIZZY\n\n",
    "Do you have a difficulty in breathing?\n 1.YES\n 2.NO \n 3.A LITTLE \n\n", color.END
]


class Maswali:
    def __init__(self, ask, answer):
        self.ask = ask
        self.answer = answer


questions_object = [
    Maswali(questions_ask[0], "1"),
    Maswali(questions_ask[1], "2"),
    Maswali(questions_ask[2], "1"),
    Maswali(questions_ask[3], "2"),
    # qes ojcets
]


# here is a function called run that  i use to run it
def run_questions(questions_object):  # functio
    score = 0  # counter
    for question in questions_object:
        student_answer = input(question.ask)  # variable jibu
        if student_answer == question.answer:
            score += 1
            if score >= 3:
                print(color.RED, color.BOLD, "you got ", str(score), "/", str(len(questions_object)),
                      '''Self care If you feel sick you should rest, drink plenty of fluid, and eat nutritious food. 
Stay in a separate room from other family members, and use a dedicated bathroom if possible. 
Clean and disinfect frequently touched surfaces. Everyone should keep a healthy lifestyle at 
home. Maintain a healthy diet, sleep, stay active, and make social contact with loved ones 
through the phone or internet. Children need extra love and attention from adults during 
difficult times. Keep to regular routines and schedules as much as possible. It is normal to 
feel sad, stressed, or confused during a crisis. Talking to people you trust, such as friends 
 and family, can help. If you feel overwhelmed, talk to a health worker or counsellor. Learn 
more on who.int For informational purposes only. Consult your local medical authority for 
advice. Medical treatments If you have mild symptoms and are otherwise healthy, self-isolate 
and contact your medical provider or a COVID-19 information line for advice. Seek medical care 
if you have a fever, cough, and difficulty breathing. Call in advance.''', color.END)
            else:
                print(color.GREEN, prevention, color.END)


run_questions(questions_object)

now = datetime.datetime.now()
print("\nDiagnosed on\n:", (now.strftime("%Y-%m-%d %H:%M:%S")))
