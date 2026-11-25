def modify_content(content):
    """
    Modify the content from the file.
    In this example, we convert it to uppercase.
    """
    return content.upper()


def main():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            original_content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")
        return

    modified_content = modify_content(original_content)

    output_filename = "modified_" + input_filename

    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to file '{output_filename}'.")

if __name__ == "__main__":
    main()
