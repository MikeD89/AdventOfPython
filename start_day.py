import os
import webbrowser


def start_day(y, d):
    # copy the template file and replace the contents with the day and year
    # then open the file in the editor

    # get the path to the template file
    template_path = os.path.join(os.path.dirname(__file__), "template.py")
    # get the path to the new file
    new_path = os.path.join(os.path.dirname(__file__), str(y),  str(y) + "_day_" + f"{d:02}" + ".py")
    # get the path to the test data file
    testdata_path = os.path.join(os.path.dirname(__file__), str(y),  "testdata", str(y) + "_day_" + f"{d:02}" + ".txt")

    # make the directory if it doesn't exist
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    os.makedirs(os.path.dirname(testdata_path), exist_ok=True)

    # make an empty testdata file
    with open(testdata_path, "w") as f:
        f.write("")

    # create the new file
    with open(new_path, "w+") as new_file:
        # open the template file
        with open(template_path, "r") as template_file:
            # read the template file
            template = template_file.read()
            # replace the year and day in the template
            template = template.replace("YEAR", str(y))
            template = template.replace("DAY", str(d))
            # write the template to the new file
            new_file.write(template)

    # open the new file in the editor
    os.system("code " + testdata_path)
    os.system("code " + new_path)
    # Open the aoc website
    webbrowser.open(f'https://adventofcode.com/{y}/day/{d}')


if __name__ == "__main__":
    # get the year and day from the command line
    y = int(input("Year: "))
    d = int(input("Day: "))
    # start the day
    start_day(y, d)
