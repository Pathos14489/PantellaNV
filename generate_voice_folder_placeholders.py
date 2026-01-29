import json
import os

source_dir = "./Sound/Voice/PantellaNV.esm/FemaleAdult01DefaultDC/"
output_dir = "./Sound/Voice/PantellaNV.esm/"

ttw_voice_id_map = json.loads(open("ttw_voice_id_map.json", "r", encoding="utf-8").read())

for _, voice_name in ttw_voice_id_map.items(): # Copy the contents of the source directory to the output directory with new names for each directory. The files inside hte source directory are not renamed.
    voice_folder = os.path.join(output_dir, voice_name)
    if not os.path.exists(voice_folder):
        os.makedirs(voice_folder)
    for file_name in os.listdir(source_dir):
        source_file_path = os.path.join(source_dir, file_name)
        target_file_path = os.path.join(voice_folder, file_name)
        print(f"Creating placeholder for {target_file_path} using source {source_file_path}")
        if not os.path.exists(target_file_path):
            with open(source_file_path, "rb") as source_file:
                with open(target_file_path, "wb") as target_file:
                    target_file.write(source_file.read())