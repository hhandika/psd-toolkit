# Using short option
python script.py -d /path/to/psd/files

# Using long option
python script.py --dir /path/to/psd/files

# With custom output directory
python script.py -d input_folder -o output_folder

# Process recursively
python script.py -d input_folder -o output_folder -r

# Mix short and long options
python script.py --dir input_folder -o output_folder --recursive
