import os
import csv
import random


class Game:
    def __init__(self):
        self.ison = 0
        self.wordlist = []
        self.secret = ""
        self.question = None
        self.hint = ""

    def getwords(self):
        find_file = os.path.join(os.getcwd(), 'words', 'verbs_list.csv')

        with open(find_file) as words:
            conv_csv = csv.DictReader(words)
            for row in conv_csv:
                self.wordlist.append(row['French'])

    def set_score(self, word, poscore, negcore):
        find_file = os.path.join(os.getcwd(), 'words', 'word_data.csv')
        temp = {}

        with open(find_file) as file:
            compact = csv.DictReader(file)
            for row in compact:
                if word == row["Word"]:
                    temp.update({word: {"Word": row["Word"],
                                 "Positive": int(row["Positive"]) + poscore,
                                 "Negative": int(row["Negative"]) + negcore}})
                else:
                    temp.update({row["Word"]: {"Word": row["Word"],
                                 "Positive": row["Positive"],
                                 "Negative": row["Negative"]}})

        if word not in temp.keys():
            temp.update({word: {"Word": word, "Positive": poscore, "Negative": negcore}})

        with open(find_file, 'w') as file:
            conv_csv = csv.DictWriter(file, fieldnames=["Word", "Positive", "Negative"])
            conv_csv.writeheader()
            for value in temp.values():
                conv_csv.writerow({"Word": value["Word"], "Positive": value["Positive"],
                                   "Negative": value["Negative"]})

    def randomword(self):
        if not self.wordlist:
            self.getwords()
            self.secret = self.randomword()
            return self.secret
        else:
            randomword = self.wordlist[random.randint(0, len(self.wordlist)-1)]
            self.secret = randomword
            return self.secret

    def sliceword(self):
        sliceword = self.randomword()
        self.question = sliceword[0:random.randint(2, len(sliceword)-1)]
        return self.question

    def slicerand(self):
        sliceword = self.randomword()
        cut = list(sliceword)
        missing = []

        if len(cut) >= 5:
            take_out = random.randint(1, 3)
        elif len(cut) > 4:
            take_out = random.randint(1, 2)
        else:
            take_out = 1

        while take_out > 0:
            missing.append(cut[take_out])
            cut.pop(take_out)
            cut.insert(take_out, " ")
            take_out -= 1

        self.question = missing
        self.question.reverse()
        self.hint = "".join(cut)
        return self.secret

    def guessword(self):
        if not self.question:
            self.sliceword()
        print(self.question)
        answer = input("Please try to guess the word.")

        while answer != self.secret:
            print(self.question)
            answer = input("Incorrect. Please try again.")
            if answer != self.secret:
                self.set_score(self.secret, 0, 1)
            else:
                self.set_score(self.secret, 1, 0)

        print(self.secret)
        print("Good job!")
        return self.secret

    def randguess(self):
        if not self.question:
            self.slicerand()

        while len(self.question) > 0:
            print(self.hint)
            answer = input("Find missing letters.")
            if answer in self.question:
                self.question.remove(answer)
                self.set_score(self.secret, 1, 0)
            elif answer == "".join(self.question):
                self.question = []
                self.set_score(self.secret, 1, 0)
            else:
                self.set_score(self.secret, 0, 1)

        print("Good job! The correct answer was:")
        print(self.secret)
        return self.secret

new_game = Game()

if __name__ == '__main__':
    new_game.ison = 1
    while new_game.ison == 1:
        input("""Welcome to Langame! 
For help please type /help.
Would you like to play ? Type Y/N.""")