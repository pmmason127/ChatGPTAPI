import openai			# pip install openai
'''
A basic implementation of ChatGPT that can carry a continuous conversation
'''

# openAI user key for pmarkmason account
openai.api_key = 'PUT KEY HERE'		# go to platform.openai.com, under profile, look at APIs and generate an API key, paste that here.

# Initialized conversation variable
messages = [{"role": "system", "content": "You are a helpful assistant"}]

while True:
	# Input prompt from the user
	message = input("🧑: ")

	# Initialize chat completion:
	chat_completion = None

	# If the user inputs a message
	if message:
		# Appends the user message to the conversation
		messages.append({"role": "user", "content": message})

		# Calls the GPT model to respond to
		chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

	# Assigns the response from the model to a reply
	reply = chat_completion.choices[0].message.content

	# Print out the reply from GPT
	print(f"🖥️: {reply}")

	# Append the reply to the conversation
	messages.append({"role": "assistant", "content": reply})