import langchain
from apikey import OPENAI_API_KEY
import os
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Input text
input_text = "con vịt đang ở trong nồi, con gà ca hát nhảy múa, chủ thì u sầu"

# Create model
model = langchain.OpenAI(model_name="text-davinci-003", n=1, best_of=1, temperature=0.9, top_p=0.95)

# Generate a sentence from the input text
output_sentence = model.generate([input_text])

print("Input text:", input_text)
print("Generated text:", output_sentence)

