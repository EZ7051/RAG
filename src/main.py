# main.py

from database import DatabaseHandler
from redis_cache import RedisCacheHandler
from openai_api import OpenAIAPIHandler

def main():
    user_id = 123  
    user_prompt = "How does photosynthesis work?"  

    # Database operations
    db_handler = DatabaseHandler()
    user_data = db_handler.get_user_data(user_id)
    db_handler.close_connection()

    # Redis cache operations
    redis_handler = RedisCacheHandler()
    cached_user_data = redis_handler.get_cached_user_data(user_id)

    if cached_user_data:
        print("User data retrieved from cache.")
        user_data = eval(cached_user_data)  
    else:
        redis_handler.cache_user_data(user_id, user_data)
        print("User data retrieved from PostgreSQL and cached.")

    # OpenAI GPT API call
    openai_handler = OpenAIAPIHandler()
    augmented_prompt = f"{user_prompt}\nUser Data: {user_data}"
    chat_reply = openai_handler.get_chat_response(augmented_prompt)

    # Display the augmented prompt and model's reply
    print("Augmented Prompt:", augmented_prompt)
    print("ChatGPT Reply:", chat_reply)

if __name__ == "__main__":
    main()
