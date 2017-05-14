import sys, os

args = sys.argv[1:]
if (args[0] == "h" or args[0] == "help"):
    print("addh to add a handler")
elif (args[0] == "addh"):
    newMPath = "res/private/html/" + args[1]
    if (os.path.isdir(newMPath)):
        print("Handler already exists")
    else:
        os.makedirs(newMPath)
        with open(newMPath + "/index.html", "w") as f:
            f.write("<main><h1>New page</h1></main>")
        newHFile = "views/{0}.py".format(args[1])
        with open("views/.template.py", "r") as t:
            with open(newHFile, "w") as f:
                f.write(t.read().replace("#HANDLER", args[1]))