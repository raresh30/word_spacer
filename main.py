def main():
    sep = input("Enter separation string: ")
    with open("result.txt", "w") as write_file:
        with open("words.txt", "r") as file:
            for line in file:
                for word in line.split():
                    write_file.write(word + sep)
        write_file.write("\n")

if __name__ == "__main__":
    main()
