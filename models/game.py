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
        
        # if p1 == None and p2 == None:
        #     return f"{player_1.name} and {player_2.name} draw with {p1_choice}!"
        # elif p1 == True:
        #     return f"{player_1.name} wins with {p1_choice}!"
        # elif p2 == True:
        #     return f"{player_2.name} wins with {p2_choice}!"
        
        
#_________________PREVIOUS VERSIONS OF def play():
        
#   def play(player1_name, p1_choice, player2_name, p2_choice):
#         p1 = None
#         p2 = None       
#         if p1_choice == p2_choice:
#             p1 == None, p2 == None
#         elif p1_choice == "rock" and p2_choice == "scissors":
#             p1 == True
#         elif p2_choice == "rock" and p1_choice == "scissors":
#             p2 == True
              
#         elif p1_choice == "rock" and p2_choice == "paper":
#             p2 == True
#         elif p2_choice == "rock" and p1_choice == "paper":
#             p1 == True        
#         elif p1_choice == "paper" and p2_choice == "scissors":
#             p1 == True
#         elif p2_choice == "paper" and p1_choice == "scissors":
#             p2 == True
        
#         if p1 == None and p2 == None:
#             return f"{player1_name} and {player2_name} draw with {p1_choice}!"
#         elif p1 == True:
#             return f"{player1_name} wins with {p1_choice}!"
#         elif p2 == True:
#             return f"{player2_name} wins with {p2_choice}!"
        