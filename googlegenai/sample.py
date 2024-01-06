import google.generativeai as genai
import time

api_key = "AIzaSyCc4o3_ZNbpwLGisP1SRw_hQaWTzo0wavE"

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

t1 = time.time()

prompt = "For the word given below, generate sentences that describes the meaning of the word. Also, if the word is available in its other grammatical forms such as noun, adjective, verb, gerund, pronoun, adverb, etc also generate sentences using  them. The sentences should describe the meaning of the word clearly. The sentences can also be continuous (i.e) can form a continuous story or context. The sentences should be of variable length. Generate atleast 500 Sentences describing the word and its other form in various context. Each sentence should start with ### Sentence: template . If the sentences are of continuous context just separete them by a dot(.).Word : AIDS"

response = model.generate_content(prompt)

t2 = time.time()

print(response.text)

print("Time taken: ", t2-t1)

