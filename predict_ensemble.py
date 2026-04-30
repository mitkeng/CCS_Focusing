import os
import argparse
import shutil
import pandas as pd
import tensorflow as tf
import ccs_focusing_utils as ccs_utils
import matplotlib
matplotlib.use('Agg')

def main():
    parser = argparse.ArgumentParser(description='CCS Prediction & Automatic Filtering')
    parser.add_argument('--folder', type=str, required=True, help='Path to folder containing .xyz files')
    # Default value set to ML_ccs.keras
    parser.add_argument('--model', type=str, default='ML_ccs.keras', help='Path to the Keras model (Default: ML_ccs.keras)')
    parser.add_argument('--output', type=str, default='ensemble_results.csv', help='Filename for CSV output')
    parser.add_argument('--target', type=float, help='Experimental CCS target for automatic siphoning')
    parser.add_argument('--tolerance', type=float, default=0.05, help='Tolerance (e.g., 0.05 for 5%%)')
    parser.add_argument('--name', type=str, default='Focused', help='Name of the compound/system for the output folder')

    args = parser.parse_args()

    if not os.path.exists(args.folder):
        print(f'Error: Folder {args.folder} not found.')
        return

    # Check for model existence
    if not os.path.exists(args.model):
        print(f'Error: Model file {args.model} not found. Ensure ML_ccs.keras is in the current directory.')
        return

    print(f'--- Loading Model: {args.model} ---')
    model = tf.keras.models.load_model(args.model)
    files = [f for f in os.listdir(args.folder) if f.lower().endswith('.xyz')]
    print(f'Found {len(files)} conformers.')

    results = []
    captured_count = 0
    do_filter = args.target is not None

    if do_filter:
        upper = args.target * (1 + args.tolerance)
        lower = args.target * (1 - args.tolerance)
        focus_dir = f'{args.name}_Target_{args.target}'
        os.makedirs(focus_dir, exist_ok=True)
        print(f'--- Filtering Mode: {args.name} | Range: {lower:.2f}-{upper:.2f} ---')

    for i, filename in enumerate(files):
        try:
            path = os.path.join(args.folder, filename)
            features = ccs_utils.get_physical_features(path)
            prediction = model.predict(features, verbose=0)[0][0]
            val = round(float(prediction), 3)
            results.append({'filename': filename, 'predicted_ccs': val})

            if do_filter and lower <= val <= upper:
                shutil.copy(path, os.path.join(focus_dir, filename))
                captured_count += 1
            
            if (i+1) % 25 == 0:
                print(f'Processed {i+1}/{len(files)}...')
        except Exception as e:
            print(f'Error processing {filename}: {e}')

    pd.DataFrame(results).to_csv(args.output, index=False)
    print(f'--- Finished! Results saved to {args.output} ---')
    if do_filter:
        print(f'--- Siphoned {captured_count} conformers into {focus_dir} ---')

if __name__ == "__main__":
    main()