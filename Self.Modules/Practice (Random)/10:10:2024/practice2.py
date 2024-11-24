if __name__ == "__main__":
    def print_diamond(size):
        diamond = ""  # This will hold the final diamond string
        # Loop to create the top half of the diamond
        for row in range(1, size + 1):

            # Calculate number of stars and spaces
            num_stars = 2 * row - 1  # Number of stars for this row
            num_spaces = size - row   # Number of leading spaces
            # Construct the row and add to the string
            diamond += ' ' * num_spaces + '*' * num_stars + '\n'
        
        # Loop to create the bottom half of the diamond
        for row in range(size - 1, 0, -1):
            num_stars = 2 * row - 1
            num_spaces = size - row
            diamond += ' ' * num_spaces + '*' * num_stars + '\n'

        return diamond.strip()  # Remove the last newline character

    # Example usage
    size = 5
    print(print_diamond(size))
