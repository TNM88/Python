class Teacher:
    def profile(self):
        print("Teacher Profile")

class Author:
    def profile(self):
        print("Author Profile")

class TeacherAuthor(Teacher, Author):
    def profile(self):
        Teacher.profile(self)
        Author.profile(self)

teacher_author = TeacherAuthor()
teacher_author.profile()
