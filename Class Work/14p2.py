class Teacher:
    def schedule_class(self):
        print("Scheduling class...")
    
    def grade_student(self):
        print("Grading student...")
    
    def display_name(self):
        print("Teacher: Display Name")

class Author:
    def write_article(self):
        print("Writing article...")
    
    def publish_blog(self):
        print("Publishing blog...")

class TeacherAuthor(Teacher, Author):
    pass

teacher_author = TeacherAuthor()

teacher_author.schedule_class()
teacher_author.grade_student()
teacher_author.display_name()
teacher_author.write_article()
teacher_author.publish_blog()
