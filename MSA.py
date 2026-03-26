def calculate_msa_stats(file_path):
    sequences = []
    with open(file_path, 'r') as f:
        current_seq = ""
        for line in f:
            line = line.strip()
            if not line: continue
            if line.startswith(">"):
                if current_seq: sequences.append(current_seq)
                current_seq = ""
            else:
                current_seq += line
        if current_seq: sequences.append(current_seq)

    if not sequences: return "No sequences found."
    alignment_length = max(len(s) for s in sequences)
    sequences = [s.ljust(alignment_length, '-') for s in sequences]
    num_sequences = len(sequences)
    total_gaps = 0
    conserved_cols = 0
    for i in range(alignment_length):
        column = [seq[i] for seq in sequences]
        total_gaps += column.count('-')
        if all(char == column[0] for char in column) and column[0] != '-':
            conserved_cols += 1
    gap_percentage = (total_gaps / (alignment_length * num_sequences)) * 100
    return {
        "Alignment Length": alignment_length,
        "Conserved Columns": conserved_cols,
        "Gap Percentage": f"{gap_percentage:.2f}%",
        "Number of Sequences": num_sequences
    }

stats = calculate_msa_stats("all_seq.txt")
print(stats)