import openai
from openai import OpenAI
import os 

openai.api_key = 'sk-Wxf6xhdZ3Ym5VcW7FOekGx4--ZHv31RUI0HTkanTEMT3BlbkFJVVb_2EVwqeBdlKG2t9eLMFOpQjG7-y6wJKu6UBO9oA'

client = OpenAI(api_key= openai.api_key)

PantsComp ="https://i.imgur.com/G6K2X9J.png"
ShortsComp = "https://i.imgur.com/cvhqvfY.png"
Pants = True

if(Pants):
    url = PantsComp
else:
    url = ShortsComp


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a friendly park ranger who grew up in the who knows fashion who always has an opinion on if pants or shorts is the best option"},
        {"role": "user", "content": [
            {"type": "text", "text": "Is this outfit suitable for a park that can go up to 100 degrees farenheight"},
            {"type": "image_url", "image_url": {
                "url": url}
            }           
        ]} 
    ],
    temperature=0.0,
)

feedback = response.choices[0].message.content
print(response.choices[0].message.content)
