# Amino acid residue mass table (monoisotopic, amu)
aa_mass_table = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'I': 113.08,
    'L': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08
}


def calculate_protein_mass(sequence):
    """
    Calculate the total mass of a protein sequence
    :param sequence: Amino acid sequence string
    :return: Total mass in amu
    :raises ValueError: If invalid amino acid symbol is found
    """
    # Convert input to uppercase to support lowercase input
    sequence = sequence.upper()
    total_mass = 0.0

    for aa in sequence:
        if aa not in aa_mass_table:
            raise ValueError(f"Invalid amino acid symbol: '{aa}'. This symbol is not recognized.")
        total_mass += aa_mass_table[aa]
    
    return total_mass


if __name__ == "__main__":
    # Example 1: Test normal valid sequence
    print("Example 1: Test valid protein sequence")
    test_seq = "MA"
    try:
        result = calculate_protein_mass(test_seq)
        print(f"Input sequence: {test_seq}")
        print(f"Calculated protein mass: {result:.2f} amu")
    except ValueError as e:
        print(f"Error: {e}")

    # Example 2: Test invalid sequence to show error handling
    print("\nExample 2: Test invalid sequence (error handling)")
    invalid_seq = "MAX"
    try:
        result = calculate_protein_mass(invalid_seq)
        print(f"Input sequence: {invalid_seq}")
        print(f"Calculated protein mass: {result:.2f} amu")
    except ValueError as e:
        print(f"Input sequence: {invalid_seq}")
        print(f"Error: {e}")