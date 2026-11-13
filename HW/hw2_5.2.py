import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения: {end-start:.1f} секунд')
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")

download_video()