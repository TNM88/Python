class Teacher:
    def profile(self):
        print("Teacher Profile")

class Author(Teacher):
    def profile(self):
        print("Author Profile")

teacher = Teacher()
author = Author()

teacher.profile()
author.profile()
