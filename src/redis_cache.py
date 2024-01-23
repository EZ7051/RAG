import redis

class RedisCacheHandler:
    def __init__(self):
        # Connect to Redis
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    def get_cached_user_data(self, user_id):
        # Check if user data is in Redis cache
        return self.redis_client.get(f'user_data:{user_id}')

    def cache_user_data(self, user_id, user_data):
        # Store user data in Redis cache with a time-to-live (TTL) of 1 hour
        self.redis_client.setex(f'user_data:{user_id}', 3600, str(user_data))
