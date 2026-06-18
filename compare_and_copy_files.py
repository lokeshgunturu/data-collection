import os
import shutil
from pathlib import Path

# from move_files import source_dirs

# from move_files import source_dirs

# from move_files import source_dirs

def get_all_file_paths(directory):
    """Get all file paths from a directory and its subdirectories."""
    file_paths = []
    for root, _, files in os.walk(directory):
        if os.path.basename(root) in ["labels", "with_boxes"]:
            continue
        for file in files:
            file_paths.append(os.path.join(root, file))
    print(file_paths)
    return file_paths

def get_file_names(directory):
    """Get all file paths relative to the directory, maintaining full subdirectory structure."""
    file_paths = {}
    directory = os.path.normpath(directory)  # Normalize the path
    for root, _, files in os.walk(directory):

        print("FFFFFFF", root, files)
        for file in files:
            full_path = os.path.join(root, file)
            # Get relative path while preserving the full structure
            rel_path = os.path.relpath(full_path, os.path.dirname(directory))
            file_paths[file] = rel_path
    return file_paths

def copy_matching_files(source_dirs, comparison_dir, output_dir):
    """
    Copy files from source directories that match file names in comparison directory
    to output directory, maintaining the same directory structure.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all file names and their relative paths from comparison directory
    comparison_files = get_file_names(comparison_dir)
    print(len(comparison_files))
    
    # Track copied files to avoid duplicates
    copied_files = set()
    not_there=0
    for source_dir in source_dirs:
        # Get all file paths from source directory and its subdirectories
        file_paths = get_all_file_paths(source_dir)
        #print(file_paths)
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            print("***********", comparison_files)
            
            # Check if file exists in comparison directory
            if file_name in comparison_files:
                # not_there+=1
                # Get the relative path from comparison directory
                rel_path = comparison_files[file_name]
                
                # Create the full destination path
                dest_dir = os.path.join(output_dir, os.path.dirname(rel_path))
                dest_path = os.path.join(dest_dir, file_name)
                
                # Create destination directory if it doesn't exist
                os.makedirs(dest_dir, exist_ok=True)
                
                # Copy the file if it hasn't been copied before
                if file_name not in copied_files:
                    shutil.copy2(file_path, dest_path)
                    copied_files.add(file_name)
                    # print(f"Copied {file_path} to {dest_path}")
                
                
                try:
                    # Copy file to the destination path
                    shutil.copy2(file_path, dest_path)
                    # print(f"Copied {file_path} to {dest_path}")
                except Exception as e:
    # Print summary
                    print(f"Error copying {file_path}: {e}")
            else:
                not_there+=1
    
    # Print summary
    # Print summary
    print(f"\nSummary:")
    print(f"Total files copied: {len(copied_files)}")
    # Print summary
    # Print summary
    print(f"Source directories: {len(source_dirs)}")
    print(f"Not there: {not_there}")

if __name__ == "__main__":
    # Example usage - modify these paths as needed
    # source_dirs = [
    #     "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/01-07-2025",
    #     "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/02-07-2025",
    #      "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/03-07-2025",
    #      "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/04-07-2025",
    #      "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/05-07-2025",
    #      "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/06-07-2025",
    #      "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/07-07-2025",
    #      "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/08-07-2025",
    #      "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/09-07-2025",
    #      "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/10-07-2025",
    #     # Add more source directories as needed
    # ]
    # source_dirs = [ "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/01-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/02-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/03-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/04-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/05-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/06-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/07-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/08-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/09-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/10-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/11-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/12-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/13-08-2025"]

    # source_dirs = ["/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/14-08-2025",

    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/15-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/16-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/17-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/18-08-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model/19-08-2025"]

#     source_dirs = ["/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/11-07-2025",
#         "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/12-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/13-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/14-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/15-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/16-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/17-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/18-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/19-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/20-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/21-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/22-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/23-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/24-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/25-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/26-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/27-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/28-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/29-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/30-07-2025",
# "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_diff_cls_conf/31-07-2025"]

    # source_dirs = [
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/01-01-2026",
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/22-12-2025",
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/23-12-2025",
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/24-12-2025",
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/26-12-2025",
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/27-12-2025",
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/28-12-2025"
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/29-12-2025",
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/30-12-2025",
    #     "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/31-12-2025"]
#     source_dirs = ["/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/01-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/10-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/11-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/12-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/13-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/14-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/15-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/16-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/17-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/18-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/19-12-2025"] 
#     source_dirs = ["/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/01-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/02-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/03-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/04-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/05-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/06-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/07-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/08-01-2026"]
#     source_dirs = [
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/19-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/20-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/21-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/22-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/23-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/24-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/25-12-2025"]
    # source_dirs = ["/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/dec/22-12-2025"]      
    # source_dirs = ["/home/atai-netapp-storagev4/damage_data/outputs_cnrail_new_model_9_jan/CN_Rail/IN/09-01-2026/"]
    #source_dirs = ["/home/ml_training_data/manasa/damage/outputs_psa_new_model/20260511/20260508_135802"]
    source_dirs = []
    # comparison_dir = "/home/atai-netapp-storagev3/damage_data/CLDN_Data/selected_new_frames/images_set4/images"  # Directory to compare file names with
    # output_dir = "/home/atai-netapp-storagev3/damage_data/CLDN_Data/selected_new_frames/raw_images_new_model_aug_2"  # Directory where matching files will be copied
    # comparison_dir = "/home/atai-netapp-storagev4/damage_data/selected_frames_cwc_whitefield_dec_19_25/chosen/"  # Directory to compare file names with
    # output_dir = "/home/atai-netapp-storagev4/damage_data/selected_frames_cwc_whitefield_dec_19_25/raw_imgs"  # Directory where matching files will be copied
    # comparison_dir = "/home/atai-netapp-storagev4/damage_data/selected_frames_cnrail_minor/images_3/all_imgs/"

    # comparison_dir = "/home/atai-netapp-storagev4/damage_data/selected_frames_cnrail_9_jan/"
    comparison_dir = "/home/ml_training_data/manasa/damage/lokesh/NSFT/images"
    # output_dir = "/home/atai-netapp-storagev4/damage_data/selected_frames_cnrail_minor/images_3/raw_imgs/"
    output_dir = "/home/ml_training_data/manasa/damage/lokesh/NSFT/comparsion_result/"

    
    copy_matching_files(source_dirs, comparison_dir, output_dir)
