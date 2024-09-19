#soru class i yaratildi
class Question():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):  #yanit kontrol metodu olusturuldu.
        return self.answer==answer #disardan gonderilen answer degeri ile object icindeki deger kontrol edilir.

#quiz class i yaratildi. soru listesini  buraya aktaracagiz.
class Quiz():
    def __init__(self,questions): #atamalar yapildi
        self.questions=questions 
        self.score=0
        self.questionIndex=0  #index default olarak 0 olarak atandi.     
    
    def getQuestion(self): #soru getirme metodu
        return self.questions[self.questionIndex]
    
    def displayQuestions(self): #soru gosterme metodu
        question=self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+q)
            
        answer=input('cevap: ')
        self.guess(answer)
        self.loadQuestions()

    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score+=1
            self.questionIndex+=1

    def loadQuestions(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayQuestions()

    def showScore(self):
        print(f'score {self.score}')
            
    
#soru objectleri yaratildi
q1=Question('En iyi programlama dili hangisidir?',['C#','Java','Python','C++'],'Python')
q2=Question('En populer programlama dili hangisidir?',['C#','Java','Python','C++'],'Java')

#soru objectleri liste icine aktarildi.
questions=[q1,q2]


quiz=Quiz(questions)
question=quiz.displayQuestions()




        