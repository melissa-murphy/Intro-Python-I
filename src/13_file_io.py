"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE


def read_foo():
    # open and read foo.txt
    f = open("foo.txt", "r")
    if f.mode == "r":
        contents = f.read()
        print(contents)


read_foo()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain


def create_foo():
    # open new file; create if none exist
    f = open("bar.txt", "w+")
    # add content to bar
    for i in range(1):
        f.write("Pirate Round Sail ho swing the lead doubloon blow the man down pinnace fore poop deck weigh anchor booty %d\r\n")
        f.write("Sea Legs haul wind port jolly boat Brethren of the Coast sloop heave to scallywag knave black jack %d\r\n")
        f.write("Scourge of the seven seas heave to holystone boatswain coffer Pirate Round furl schooner shrouds bowsprit. %d\r\n")
    f.close()


create_foo()

# YOUR CODE HERE
