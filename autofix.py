def fix_paths(raw_text):
    fixed_lines = []

    for line in raw_text.splitlines():
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Add opening quote if missing
        if not line.startswith("'"):
            line = "'" + line

        # Add closing quote if missing
        if not line.endswith("'"):
            line = line + "'"

        fixed_lines.append(line)

    # Add commas properly
    fixed_output = "source_dirs = [\n"
    fixed_output += ",\n".join(fixed_lines)
    fixed_output += "\n]"

    return fixed_output


# 🔹 Paste your raw text here (even broken format works)
raw_input_text = """
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
"""

# Run fix
result = fix_paths(raw_input_text)

print(result)