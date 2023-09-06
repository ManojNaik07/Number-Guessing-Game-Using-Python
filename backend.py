import random

class NumberGuessingGame:
    def __init__(self):
        self.number = None
        self.num_guesses = None
        self.max_guesses = None
        self.player_name = None
        self.game_over = None
        self.score=None

        self.high_scores = []
        ''' try:
            with open("high_scores.txt", "r") as file:
                for line in file:
                    name, score = line.strip().split(",")
                    self.high_scores.append((name, int(score)))
        except FileNotFoundError:
            pass'''

    def start_game(self, name):
        self.player_name = name if name else "Player"
        self.number = random.randint(1, 50)
        self.num_guesses = 0
        self.max_guesses = 5

    def guess_number(self, guess):
        self.num_guesses += 1
        if self.num_guesses==self.max_guesses:
            if guess==self.number:
                self.score=10
            else:
                self.score=0
            self.game_over=1
            self.high_scores = []
            self.high_scores.append(self.player_name)
            self.high_scores.append(self.score)
            #self.high_scores.append((self.player_name, self.score))
            #self.high_scores.sort(key=lambda x: x[1])
            #with open("Documents//cas1//cas1//high_scores.txt", "w") as file:
                #for name, score in self.high_scores[:10]:
                    #file.write(f"{name},{score}\n")
                #file.write(self.player_name+" "+str(self.score))
            if guess==self.number:
                return "You got correct answer at last try, Congratulations"
            return "All guesses over"
        if guess < self.number:
            return f"Your guess of {guess} is too low! Guess again. ({self.max_guesses - self.num_guesses} guesses remaining)"
        elif guess > self.number:
            return f"Your guess of {guess} is too high! Guess again. ({self.max_guesses - self.num_guesses} guesses remaining)"
        else:
            self.game_over=1
            self.score = (self.max_guesses - self.num_guesses+1) * 10
            self.high_scores = []
            #self.high_scores.append((self.player_name, self.score))
            #self.high_scores.sort(key=lambda x: x[1])
            self.high_scores.append(self.player_name)
            self.high_scores.append(self.score)
            #with open("D:\python\high_scores.txt", "w") as file:
                #for name, score in self.high_scores[:10]:
                    #file.write(f"{name},{score}\n")
                #file.write(self.high_scores[0]+" "+str(self.high_scores[1])+"\n")
            return f"Congratulations, {self.player_name}! You guessed the number {self.number} in {self.num_guesses} guesses and won {self.score} points!"
        
    def get_high_scores(self):
        return self.high_scores