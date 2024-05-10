import os

def count_files_in_folder(folder_path):
  
    file_count = 0
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        if os.path.isfile(item_path):
            file_count += 1 
    
    return file_count


folder_path = "YoloV8-FT_box_output"  # Update with the path to your folder
total_files = count_files_in_folder(folder_path)
print(f"Total number of files in {folder_path}: {total_files}")
