import sys
from datetime import datetime


class Console:

    @staticmethod
    def Writeln(*args, sep=" ", end="\n", file=None):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = sep.join(map(str, args))

        if file == None:
            file = sys.stdout
        file.write(f"{output}{end}{timestamp}{end}")

     


Console.Writeln(5)
Console.Writeln("Hello")

