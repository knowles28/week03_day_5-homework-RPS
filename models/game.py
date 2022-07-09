class Game():
    def __init__(self, p1_choice, p2_choice):
        self.p1_choice = p1_choice
        self.p2_choice = p2_choice
    
    def play(choice1, choice2):
        
        if choice1 == "rock" and choice2 == "rock":
            return "Player 1 & Player 2 draw with rock"
        
        elif choice1 == "paper" and choice2 == "paper":
            return "Player 1 & Player 2 draw with paper"
        
        elif choice1 == "scissors" and choice2 == "scissors":
            return "Player 1 & Player 2 draw with scissors"
        
        
        elif choice1 == "rock" and choice2 == "scissors":
            return "Player 1 wins with rock"
        elif choice2 == "rock" and choice1 == "scissors":
            return "Player 2 wins with rock"
        
        
        elif choice1 == "rock" and choice2 == "paper":
            return "Player 2 wins with paper"
        elif choice2 == "rock" and choice1 == "paper":
            return "Player 1 wins with paper"
        
        
        elif choice1 == "paper" and choice2 == "scissors":
            return "Player 1 wins with paper"
        elif choice2 == "paper" and choice1 == "scissors":
            return "Player 2 wins with paper"
    

        