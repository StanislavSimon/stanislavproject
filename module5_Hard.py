class Users:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_users = None
    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == hash(password):
                self.current_users = user
                return
            print("Пользователь не найден")
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = Users(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname,password)
    def log_out(self):
        self.current_users = None
    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]
    def watch_video(self, video_title):
        if not self.current_users:
            print("Войдите в свой аккаунт,чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == video_title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет,пожалуйста покиньте страницу")
                    return
                print(f"Смотреть видео: {video_title}")
                for i in range(video_duration):
                    print(i + 1, end = '')
                    time.sleep(1)
                    print("Конец видео")
                    video.time_now = 0
                    return
        print("Видео не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)


ur.add(v1, v2)


print(ur.get_videos('Best'))
print(ur.get_videos('ПРОГ'))


ur.watch_video('Для чего девушкам нужен парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам нужен парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам нужен парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)


print(ur.current_users)

ur.watch_video('Лучший язык программирования 2024 года!')