import random

class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)

class Pupil:
    def __init__(self, *current_knowledge):
        self.knowledge = [*current_knowledge, ]

    def take(self, info):
        self.knowledge.append(info)

    def accidentally_forget(self):
        del self.knowledge[random.randint(0, len(self.knowledge))]


lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
marIvanna = Teacher()
vasy = Pupil('base')
pety = Pupil('function', 'input & output')
marIvanna.teach(lesson[1], vasy, pety)
marIvanna.teach(lesson[0], pety)
print(vasy.knowledge)
print(pety.knowledge)
pety.accidentally_forget()
print(pety.knowledge)
