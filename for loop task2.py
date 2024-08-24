
total_jumping_jacks = 100
set_size = 10
completed_jumping_jacks = 0
while completed_jumping_jacks < total_jumping_jacks:
    completed_jumping_jacks += set_size
    
    tired_response = input("Are you tired? (yes/no): ").strip().lower()
    
    if tired_response in ["yes", "y"]:

        skip_response = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        
        if skip_response in ["yes", "y"]:
            print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
            break
        else:
            remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
            print(f"{remaining_jumping_jacks} jumping jacks remaining.")
    else:
        remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
        if remaining_jumping_jacks > 0:
            print(f"{remaining_jumping_jacks} jumping jacks remaining.")
if completed_jumping_jacks >= total_jumping_jacks:
    print("Congratulations! You completed the workout.")
