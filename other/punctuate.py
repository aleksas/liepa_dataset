import string

# Function to normalize a line (lowercase, remove spaces, punctuation, and accentuation numbers)
def normalize(line):
    # Remove all whitespace, punctuation, and accentuation numbers (2, 3, 4, 5)
    line_normalized = ''.join(char for char in line.lower() if char not in string.whitespace + string.punctuation + '2345')
    return line_normalized

# Function to transfer punctuation from source_line to target_line while preserving numbers
def transfer_punctuation(source_line, target_line):
    result = []
    target_idx = 0
    
    for char in source_line:
        if char in '2345':  # Preserve accentuation numbers in the source
            result.append(char)
            continue
        if target_idx < len(target_line) and target_line[target_idx] in string.punctuation:
            result.append(target_line[target_idx])
            target_idx += 1
        result.append(char)
        target_idx += 1
    
    # Append any remaining punctuation from the target line
    while target_idx < len(target_line):
        if target_line[target_idx] in string.punctuation:
            result.append(target_line[target_idx])
        target_idx += 1
    
    return ''.join(result)

def main(file1_path, file2_path, output_file_path):
    # Read files
    with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    # Check if the number of lines matches
    if len(lines1) != len(lines2):
        print("Warning: The number of lines in the files do not match.")
    
    # Generate the output by transferring punctuation
    output_lines = []
    for line1, line2 in zip(lines1, lines2):
        norm_line1 = normalize(line1)
        norm_line2 = normalize(line2)
        
        if norm_line1 == norm_line2:
            output_line = transfer_punctuation(line1.strip(), line2.strip())
        else:
            # If no match is found (unlikely in correct input), use the line from the first file as is
            output_line = line1.strip()
        
        output_lines.append(output_line)
    
    # Write the output to a new file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in output_lines:
            output_file.write(line + '\n')


# Run the script
if __name__ == "__main__":
    for voice in ['aiste', 'regina', 'vladas', 'edvardas']:
        main('/root/liepa_dataset/other/{}_transcript_stressed.txt'.format(voice), '/root/liepa_dataset/other/{}_transcript.txt'.format(voice), '/root/liepa_dataset/other/{}_transcript_stressed_punctuated.txt'.format(voice))
