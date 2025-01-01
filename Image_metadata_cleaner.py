from PIL import Image
import os

def view_metadata(image_path):
    try:
        image=Image.open(image_path)
        metadata=image.info
        if metadata:
            print("Metadata found:")
            for key,value in metadata.items():
                print(f"{key}:{value}")
        else:
            print("NO metadata found")
    except Exception as e:
        print(f"Error viewing metadata :{e}")

def clean_metadata(image_path,save_path):
    try:
        image=Image.open(image_path)
        image.save(save_path,format=image.format)
        print(f"Clean image saved as :{save_path}")
    except Exception as e:
        print(f"Error cleaning metadata:{e}")

if __name__=="__main__":
    print("Image Metadata Cleaner")
    image_path=input("Enter the path to the image :").strip()
    if image_path.startswith("r"):
        image_path = image_path[1:]
    
    if not os.path.exists(image_path):
        print("File does not exist .Please check the path.")
    else:
        print("\nViewing Metadata...")
        view_metadata(image_path)

        save_path=input("\nEnter the path to save the cleaned image:")
        clean_metadata(image_path,save_path)
        print("\nDone!")














        
