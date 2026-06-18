import os
import shutil



def count_existing_files(target_dir):
    valid_ext = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')
    existing_files = [
        f for f in os.listdir(target_dir)
        if os.path.isfile(os.path.join(target_dir, f)) and f.lower().endswith(valid_ext)
    ]
    return len(existing_files)


def move_files_to_single_folder(source_dirs, output_dir, limit=2000):
    count = 0
    target_dir = os.path.join(output_dir, f'images_{count}')
    os.makedirs(target_dir, exist_ok=True)
    # Valid image extensions
    valid_ext = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')

    # # Count already existing images
    # existing_files = [
    #     f for f in os.listdir(target_dir)
    #     if os.path.isfile(os.path.join(target_dir, f)) and f.lower().endswith(valid_ext)
    # ]
    # total_copied = len(existing_files)

    #print(f"Existing images: {total_copied}")

    # # If already reached limit → exit
    # if total_copied >= limit:
    #     print(f"Already reached limit ({limit}). Nothing to do.")
    #     return
    total_copied = 0
    for source_dir in source_dirs:
        # if total_copied >= limit:
        #     print(f"Reached limit of {limit}. Stopping...")
        #     return
        for root, _, files in os.walk(source_dir):
            if os.path.basename(root).lower() != "with_boxes":
                continue

            for file in files:
                if total_copied >= limit:
                    count = count + 1
                    print(f"Reached limit of {limit}. creating new directory...images_{count}")
                    target_dir = os.path.join(output_dir, f'images_{count}')
                    os.makedirs(target_dir, exist_ok=True)
                    total_copied = 0

                if not file.lower().endswith(valid_ext):
                    continue

                src_file = os.path.join(root, file)

                base, ext = os.path.splitext(file)
                dst_file = os.path.join(target_dir, file)

                # Handle duplicate names
                counter = 1
                while os.path.exists(dst_file):
                    dst_file = os.path.join(target_dir, f"{base}_{counter}{ext}")
                    counter += 1

                try:
                    shutil.copy2(src_file, dst_file)
                    total_copied += 1

                    if total_copied % 100 == 0:
                        print(f"Copied: {total_copied}")

                except Exception as e:
                    print(f"Error: {src_file} -> {e}")

    print(f"Done. Total images in folder: {total_copied}")


#YOUR PATH ADDED HERE
source_dirs = [
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_193246',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_193523',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_193717',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_193908',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_194004',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_194041',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_194156',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_194410',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_201428',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_201705',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_201835',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202235',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202309',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202528',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202607',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_202750',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_203450',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_203639',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_204914',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_204956',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205034',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205201',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205323',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205621',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205819',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_205907',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210217',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210326',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210419',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210443',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210549',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210643',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_210748',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211002',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211302',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211549',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211850',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_211936',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_212136',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_212354',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_212801',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_213050',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_213212',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_213335',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_213740',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_214223',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_214415',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_214720',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_222857',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223016',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223055',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223208',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223310',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_223431',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_224027',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_224159',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_224247',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225059',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225202',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225227',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225728',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225759',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_225834',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230355',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230423',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230557',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230652',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230816',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_230932',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231019',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231109',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231329',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231454',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231543',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_231915',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_232514',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_232700',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_233100',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_233633',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_233830',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_234409',
'/home/ml_training_data/manasa/damage/outputs_nsft_new_model_mar/NSFT/IN/24-05-2026/IN_2026-05-24_20260524_235723'
]

#Output folder (change if needed)
output_dir = "/home/ml_training_data/manasa/damage/lokesh/NSFT"

#Run function
move_files_to_single_folder(source_dirs, output_dir, limit=2000)
