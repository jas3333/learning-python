class WordGame:


    def __init__(self, word, guessed_letters):
        self.word = word
        self.guessed_letters = guessed_letters
        self.game_on = True
        


    def present_word(self):
        fail = 0
        for letters in self.word:
            if letters in self.guessed_letters:
                print(letters, end="")
            else:
                print(" _ ", end="")
                fail += 1
        if fail == 0:
            print("\nNice, you won!")
            self.game_on = False


    def display_hang(self, data, tries_num):
        print(data[tries_num])
