def main():
    try:
        no_of_blocks = int(input("Enter the number of blocks"))
        if no_of_blocks < 1 or no_of_blocks > 20:
            print("Invalid Input")
            return
    except ValueError:
        print("Invalid Input")
        return

    plots = []
    for i in range(no_of_blocks):
        try:
            plot = int(input("Enter the value of plot"))
            if plot < 0:
                print("Invalid Input")
                return
            plots.append(plot)
        except ValueError:
            print("Invalid Input")
            return

    even_plots = [plot for plot in plots if plot % 2 == 0]
    odd_plots = [plot for plot in plots if plot % 2 != 0]

    sum_of_evenplots = sum(even_plots)
    sum_of_oddplots = sum(odd_plots)

    average = (sum_of_oddplots + sum_of_evenplots) / 2
    print(f"The password for the file is: {average:.2f}")  # Corrected line

if __name__ == "__main__":
    main()
