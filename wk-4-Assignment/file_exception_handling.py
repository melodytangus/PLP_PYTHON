def main():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, "r") as infile:
            content = infile.read()  
        modified_content = content.upper()

        new_filename = "modified_" + filename

    
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified file has been saved as '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
