num_rounds = int(input())

final_score = 0 
print(f"Registering {num_rounds} rounds:")
 
# accumulator for final score
for i in range(1, num_rounds + 1):
    round_score = int(input(f"Enter score for round {i}: "))

    if round_score > 100:
        bonus = round_score * 0.2  
        round_score += bonus        

    final_score += round_score  # update cumulative total
    print(f"Round {i} total added: {round_score:.1f}, Cumulative = {final_score:.1f}")
rounds_processed = num_rounds

print(f"{final_score:.1f}")
print(rounds_processed)