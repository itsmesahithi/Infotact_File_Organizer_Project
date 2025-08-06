import os
import shutil
import logging

FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Others': []
}

def setup_logging():
    logging.basicConfig(
        filename='file_organizer.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(target_dir):
    try:
        if not os.path.exists(target_dir):
            logging.error(f"Directory not found: {target_dir}")
            return
        
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            
            if os.path.isfile(item_path):
                _, extension = os.path.splitext(item)
                category = get_category(extension)
                category_path = os.path.join(target_dir, category)

                if not os.path.exists(category_path):
                    os.makedirs(category_path)

                shutil.move(item_path, os.path.join(category_path, item))
                logging.info(f"Moved: {item} --> {category}/")
                
    except Exception as e:
        logging.error(f"Error organizing files: {str(e)}")

if __name__ == "__main__":
    setup_logging()
    target_directory = input("Enter the full path of the directory to organize: ").strip()
    organize_files(target_directory)
    print("File organization completed. Check the log for details.")