import google.generativeai as genai

genai.configure(api_key="AIzaSyBJ7l-knz2iWlt9n68Cc_BUyLi77iOcPD8")

myfile = genai.upload_file("audio_2025-10-14_22-48-08.ogg")
print(f"{myfile}")
context = \
    '''
    I am a developer and I want to use you as a methodologist for the ielts oral interview. I will provide you with the criteria, user audio and the text of the interview itself. You are required to evaluate each part of the test, offer recommendations, advice, and evaluate the overall score according to the ielts criteria set out below. please try to explain everything clearly and understandably
    Add a score at the head in the form of points in parts, and the final score
    Please keep in mind that your answer will be broadcast to the user, and not to me
    So answer as you should answer to a client
    
    Band 9	Expert user	You have a full operational command of the language. Your use of English is appropriate, accurate and fluent, and you show complete understanding.
    Band 8	Very good user	You have a fully operational command of the language with only occasional unsystematic inaccuracies and inappropriate usage. You may misunderstand some things in unfamiliar situations. You handle complex detailed argumentation well.
    Band 7	Good user	You have an operational command of the language, though with occasional inaccuracies, inappropriate usage and misunderstandings in some situations. Generally you handle complex language well and understand detailed reasoning.
    Band 6	Competent user	Generally you have an effective command of the language despite some inaccuracies, inappropriate usage and misunderstandings. You can use and understand fairly complex language, particularly in familiar situations.
    Band 5	Modest user	You have a partial command of the language, and cope with overall meaning in most situations, although you are likely to make many mistakes. You should be able to handle basic communication in your own field.
    Band 4	Limited user	Your basic competence is limited to familiar situations. You frequently show problems in understanding and expression. You are not able to use complex language.
    Band 3	Extremely limited user	You convey and understand only general meaning in very familiar situations. There are frequent breakdowns in communication.
    Band 2	Intermittent user	You have great difficulty understanding spoken and written English.
    Band 1	Non-user	You have no ability to use the language except a few isolated words.
    Band 0	Did not attempt the test	You did not answer the questions.
    
    IELTS:
    
    Part 1
Hobbies
1) Can you tell me about any hobbies that you have?
2) Are there any other hobbies that you would like to have in the future?
3) Do you think hobbies should be relaxing or should they be exciting?
English Studies
4) When and why did you start to learn English?
5) What aspects of learning English do you find the most difficult?
Daily Routine
6) How do you spend a typical Sunday?
7) What routine activity do you dislike the most?
8) Do you like having a set routine at work or would you prefer less structure?
Part 2
Describe a sport that you enjoy playing or watching.
You should say:
Why you started playing or watching this sport
How often you play or watch it
What benefits you get from playing or watching it
And explain why you prefer this sport to others.
Part 3
Spectator Sports
1) Are there differences between the numbers of people who watch sports and the numbers who play it?
2) Why do you think some people enjoy watching sport?
3) What are the advantages and disadvantages of watching sport live or on television?
Sports Advertising and the Media
4) What role does advertising have in sports events?
5) How important is money in sport?
'''

model = genai.GenerativeModel("gemini-2.5-flash")
result = model.generate_content([myfile, context])
text = result
print(text)