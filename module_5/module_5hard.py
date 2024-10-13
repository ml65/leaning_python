# Дополнительное практическое задание по модулю*

import time


#Задание "Свой YouTube":

class User:
    """
    Класс пользователя
    """
    def __init__(self, nickname, passwd, age):
        self.nickname = nickname
        self.password = hash(passwd)
        self.age      = age

class Video:
    """
    Класс видео
    """
    def __init__(self, title, duration, *args, **kwargs):
        self.title = title
        self.duration = duration
        self.time_now = 0
        if 'adult_mode' in kwargs:
            self.audit_mode = kwargs["adult_mode"]

class UrTube:
    """
    Класс УрТуба
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, passwd):
        usr = self.find_user(nickname)
        if usr and hash(passwd) == usr.passwd:
            self.current_user = usr.nickname
            return True
        self.current_user = None
        return False

    def find_user(self, nickname):
        for usr in self.users:
            if usr.nickname == nickname:
                return usr
        return None

    def register(self, nickname, password, age):
        usr = self.find_user(nickname)
        if not usr:
            usr = User(nickname, password, age)
            self.users.append(usr)
        self.current_user = usr.nickname

    def log_out(self):
        self.current_user = None

    def add(self,*videos):
        self.videos.extend(videos)

    def get_videos(self, search_str):
        result = []
        for video in self.videos:
            if search_str.lower() in video.title.lower():
                result.append(video.title)
        return result

    def find_video(self, title):
        for video in self.videos:
            if (video.title == title):
                return video
        return None

    def video_player(self, video):
        if video and self.adult(video):
            for t in range(1,video.duration):
                print(t)
                time.sleep(1)


    def watch_video(self, title):
        video = self.find_video(title)
        self.video_player(video)

    def adult(self, video):
        if self.current_user != None:
            if not video.audit_mode:
                return True
            elif self.find_user(self.current_user).age >= 18:
                return True
            else:
                return False
        else:
            print ("Войдите в аккаунт что бы смотреть видео")



if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
