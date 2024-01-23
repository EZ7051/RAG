from openai import ChatCompletion  

class OpenAIAPIHandler:
    @staticmethod
    def get_chat_response(prompt):
        # Call the ChatGPT API (replace 'YOUR_OPENAI_API_KEY' with your actual API key)
        chat_completion = ChatCompletion.create(
            model="text-davinci-003",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            api_key="YOUR_OPENAI_API_KEY"
        )

        # Extract and return the model's reply
        return chat_completion['choices'][0]['message']['content']
