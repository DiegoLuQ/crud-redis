import redis
import psutil
import time

def get_redis_memory_usage(redis_client):
    info = redis_client.info('memory')
    used_memory = info.get('used_memory', 0)  # Bytes
    return used_memory

def get_system_memory_info():
    virtual_mem = psutil.virtual_memory()
    total_memory = virtual_mem.total  # Bytes
    used_memory = virtual_mem.used  # Bytes
    available_memory = virtual_mem.available  # Bytes
    return total_memory, used_memory, available_memory

def main():
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    while True:
        # Obtener el uso de memoria de Redis
        redis_memory_usage = get_redis_memory_usage(redis_client)
        
        # Obtener información de la memoria del sistema
        total_memory, used_memory, available_memory = get_system_memory_info()
        
        # Convertir a MB para una lectura más fácil
        redis_memory_usage_mb = redis_memory_usage / (1024 * 1024)
        total_memory_mb = total_memory / (1024 * 1024)
        used_memory_mb = used_memory / (1024 * 1024)
        available_memory_mb = available_memory / (1024 * 1024)
        
        print(f"Redis Memory Usage: {redis_memory_usage_mb:.2f} MB")
        print(f"System Total Memory: {total_memory_mb:.2f} MB")
        print(f"System Used Memory: {used_memory_mb:.2f} MB")
        print(f"System Available Memory: {available_memory_mb:.2f} MB")
        print("-" * 40)
        
        # Esperar antes de la próxima actualización
        time.sleep(10)

if __name__ == "__main__":
    main()
