import os
import shutil
from pathlib import Path


# from compare_and_copy_files import source_dirs


def move_files_to_single_folder(source_dir, output_dir):
    # source_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(output_dir, 'images')
    os.makedirs(target_dir, exist_ok=True)
    
    # Get all subdirectories
    subdirs = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))]
    
    for subdir in subdirs:
        subdir_path = os.path.join(source_dir, subdir)
        if os.path.isdir(subdir_path):
            for root, _, files in os.walk(subdir_path):
                if os.path.basename(root)!="with_boxes":
                    # print(os.path.basename(root))
                    continue
                for file in files:
                    # print(file, (("_IN_right." not in file)))
                    # if "_IN_right." in file or "_IN_left." in file:
                    #     pass
                    # else:
                    #     continue
                    print(file)
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(target_dir, file)
                    
                    # Add counter to filename if it already exists
                    counter = 1
                    while os.path.exists(dst_file):
                        base, ext = os.path.splitext(file)
                        dst_file = os.path.join(target_dir, f"{base}_{counter}{ext}")
                        counter += 1
                    
                    try:
                        shutil.copy2(src_file, dst_file)
                        print(f"Moved: {src_file} -> {dst_file}")
                    except Exception as e:
                        print(f"Error moving {src_file}: {str(e)}")

def move_first_n_images(source_dir, dest_dir, n=10000):
    """
    Move first n images from source directory to destination directory.
    
    Args:
        source_dir (str): Source directory containing images
        dest_dir (str): Destination directory to move images to
        n (int): Number of images to move (default: 10000)
    """
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Get all image files (common image extensions)
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif'}
    
    # Convert to Path objects for easier handling
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    
    # Count of moved files
    moved_count = 0
    
    # Walk through source directory
    for root, _, files in os.walk(source_path):
        for file in files:
            # Check if file has an image extension (case-insensitive)
            if Path(file).suffix.lower() in image_extensions:
                src_file = Path(root) / file
                dst_file = dest_path / file
                
                # Handle filename conflicts
                counter = 1
                while dst_file.exists():
                    stem = src_file.stem
                    suffix = src_file.suffix
                    dst_file = dest_path / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                try:
                    # Move the file
                    shutil.move(str(src_file), str(dst_file))
                    moved_count += 1
                    print(f"Moved: {src_file} -> {dst_file}")
                    
                    # Check if we've moved enough files
                    if moved_count >= n:
                        print(f"Successfully moved {moved_count} images to {dest_dir}")
                        return
                        
                except Exception as e:
                    print(f"Error moving {src_file}: {str(e)}")
    
    print(f"Moved {moved_count} images (fewer than requested {n} images were found)")


if __name__ == "__main__":
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
    # source_dirs = ["/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_jun/21-06-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_jun/22-06-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_jun/23-06-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_jun/24-06-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_jun/25-06-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_jun/26-06-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_jun/27-06-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_jun/28-06-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_jun/29-06-2025"]
    # source_dirs = ["/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_out_gate/09-05-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_out_gate/08-05-2025",
    # "/home/atai-netapp-storagev3/damage_data/CLDN_Data/New_Frames/outputs_no_TIR_new_model_out_gate/07-05-2025"]
#     source_dirs = ["/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_1_Trimmed_Transaction_Videos/25-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_1_Trimmed_Transaction_Videos/26-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_2_Trimmed_Transaction_Videos/01-12-2025" ,
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_2_Trimmed_Transaction_Videos/11-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_2_Trimmed_Transaction_Videos/12-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_2_Trimmed_Transaction_Videos/26-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_2_Trimmed_Transaction_Videos/27-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_2_Trimmed_Transaction_Videos/28-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_2_Trimmed_Transaction_Videos/29-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_3_Trimmed_Transaction_Videos/01-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_3_Trimmed_Transaction_Videos/26-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_3_Trimmed_Transaction_Videos/27-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_3_Trimmed_Transaction_Videos/28-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_3_Trimmed_Transaction_Videos/29-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_3_Trimmed_Transaction_Videos/30-10-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/MUMBAI/IN_3_Trimmed_Transaction_Videos/31-10-2025"]

#     source_dirs = ["/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/22-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/23-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/24-12-2025" ,
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/01-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/26-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/27-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/28-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/29-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/30-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail_minor_damages/31-12-2025"]
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
#     source_dirs = [
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/19-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/20-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/21-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/22-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/23-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/24-12-2025",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cwc/WHITEFIELD/IN_GATE/25-12-2025"]
    # source_dirs = ["/home/atai-netapp-storagev4/damage_data/outputs_cnrail_new_model_9_jan/CN_Rail/IN/09-01-2026/"]
#     ["/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/01-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/02-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/03-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/04-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/05-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/06-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/07-01-2026",
# "/home/atai-netapp-storagev4/damage_data/outputs_new_cnrail/08-01-2026"]
    # output_dir = "/home/atai-netapp-storagev4/damage_data/selected_frames_cnrail_9_jan/"
    source_dirs = [
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_193246
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_193523
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_193717
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_193908
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_194004
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_194041
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_194156
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_194410
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_201428
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_201705
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_201835
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202235
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202309
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202528
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202607
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202750
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_203450
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_203639
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_204914
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_204956
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205034
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205201
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205323
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205621
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205819
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205907
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210217
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210326
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210419
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210443
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210549
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210643
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210748
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211002
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211302
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211549
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211850
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211936
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_212136
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_212354
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_212801
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_213050
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_213212
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_213335
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_213740
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_214223
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_214415
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_214720
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_222857
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223016
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223055
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223208
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223310
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223431
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_224027
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_224159
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_224247
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225059
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225202
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225227
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225728
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225759
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225834
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230355
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230423
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230557
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230652
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230816
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230932
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231019
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231109
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231329
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231454
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231543
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231915
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_232514
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_232700
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_233100
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_233633
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_233830
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_234409
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_235723
]


    output_dir = "''/home/ml_training_data/manasa/damage/lokesh"
    for source_dir in source_dirs:
        move_files_to_single_folder(source_dir, output_dir)
    # move_first_n_images("/home/atai-netapp-storagev4/damage_data/selected_frames_cnrail_minor/images", "/home/atai-netapp-storagev4/damage_data/selected_frames_cnrail_minor/images_3")
