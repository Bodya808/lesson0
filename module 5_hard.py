import time

class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return False

    def __contains__(self, item):
        return item in self.title

class UrTube:
    def __init__(self, users, videos):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname: str, password: int):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return

    def register(self, nickname: str, password: int, age: int):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def add(self, *args):
        for movie in args:
            if movie.title not in [video.title for video in self.videos]:
                self.videos.append(movie)

    def get_videos(self, text: str):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie: str):
        if self.current_user:
            for video in self.videos:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return True
                if movie in video.title:
                    for i in range(1, video.duration):
                        print(i, end=' ')
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print('Конец видео')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


    ur.add(v1, v2)


    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))


    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')


    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)


    ur.watch_video('Лучший язык программирования 2024 года!')