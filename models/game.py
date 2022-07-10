class Game():
    def __init__(self):
        self
    
    def play(p1_name, p1_choice, p2_name, p2_choice):
        # p1 = None
        # p2 = None
        winner = None
        
        if p1_choice == p2_choice:
            winner == None
        
        elif p1_choice == "rock" and p2_choice == "scissors":
            winner = p1_name
        elif p2_choice == "rock" and p1_choice == "scissors":
            winner = p2_name
        
        elif p1_choice == "rock" and p2_choice == "paper":
            winner = p2_name
        elif p2_choice == "rock" and p1_choice == "paper":
            winner = p1_name
        
        elif p1_choice == "paper" and p2_choice == "scissors":
            winner = p1_name
        elif p2_choice == "paper" and p1_choice == "scissors":
            winner = p2_name
            
        return winner
 