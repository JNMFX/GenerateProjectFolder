import os

def create_project_folders():
    # Get the current working directory
    base_dir = os.getcwd()
    
    # Prompt the user for the project name
    project_name = input("Enter the project name: ")
    main_folder = os.path.join(base_dir, project_name)
    
    # Create the main project folder
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)
        print(f"Created main project folder: {main_folder}")
    else:
        print(f"Main project folder '{main_folder}' already exists.")
    
    # Prompt the user for the number of sequences
    sequence_count = int(input("Enter the number of sequences: "))
    
    # Create the sequence folders and their respective shot folders
    for seq in range(1, sequence_count + 1):
        padded_sequence = f"{seq:03}"
        sequence_folder = os.path.join(main_folder, f"SEQ-{padded_sequence}")
        
        if not os.path.exists(sequence_folder):
            os.makedirs(sequence_folder)
            print(f"Created sequence folder: {sequence_folder}")
        else:
            print(f"Sequence folder '{sequence_folder}' already exists.")
        
        # Prompt the user for the number of shots in this sequence
        shot_count = int(input(f"Enter the number of shots for sequence SEQ-{padded_sequence}: "))
        
        for shot in range(1, shot_count + 1):
            padded_shot = f"{shot:04}"
            shot_folder = os.path.join(sequence_folder, f"sh{padded_shot}")
            
            if not os.path.exists(shot_folder):
                os.makedirs(shot_folder)
                print(f"Created shot folder: {shot_folder}")
            else:
                print(f"Shot folder '{shot_folder}' already exists.")
    
    print("All requested folders have been created (if they didn't already exist).")

if __name__ == "__main__":
    create_project_folders()