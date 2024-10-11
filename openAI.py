
from openai import OpenAI

client = OpenAI()

#this is the ai contained in a function
def teamsAid(recipient, chat):
    response = client.chat.completions.create(
        #this model was the cheapest option. each call cost less than a penny =)
        model="gpt-4o-mini",
        messages=[
            {
            #this is the user
            "role": "user",
            "content": [
                {
                "type": "text",
                #I played around with this text in the OpenAI playground to make sure the prompt was cleaned enough to where there would be no confusion to the AI on what is being asked
                "text": "Please generate a different way to word the Chat.\n\nGuidelines to formatting:\n- Length: Max of 4 sentences\n- Tone: Professional\n-Name Awareness: If the recipient's name is provided, greet and reference the recipient name at the beginning of the chat.\n\nRecipient's name: {}\n\nChat: {}".format(recipient,chat)
                }
            ]
            }
        ],
        #temp was set lower to 1 but above .01 because I want the response to be professional but not the same every time
        temperature=0.5,
        #I set the token to 1000 which should be about 4-5 sentences worth of characters
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )
    #By default the response will only give 1 choice so I am collecting that response and setting it to the var *reply_text*
    reply_text = response.choices[0].message.content
    #Then returning the response to *getPrompt.py*
    return reply_text
#"Hello Yaci, I recommend using Adobe Reader as an alternative since you currently lack a license. This will ensure you can access the necessary features without any issues. Thank you for your understanding."