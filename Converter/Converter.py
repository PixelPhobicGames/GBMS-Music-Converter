import sys , os , platform , time


print("\033[1;31;40m")
print("GBMS Converter 1.0")
print("\033[1;35;40m")
print("Software By Liquid")

if (sys.argv[1] == "--help"):
        print("\033[1;32;40m")
        print("Usage: GBMSConverter File.gbms OUTFILE.c")
        print("For Info On the GBMS File Format use the -I Argument")
        sys.exit()

if (sys.argv[1] == "-I"):
        print("\033[1;31;40m")
        print("GBMS File Format:")
        print("\033[1;32;40m")
        print("Example 1: C3|C#|0|END")
        print("           ^     ^  ^")
        print("           |     |  |")
        print("          Note  Skip|")
        print("                    |")
        print("                Ends Music")
        print()
        print("Warning Do Not Put Any Spaces or Create NewLines or the Software Might Not Work as Intended")
        sys.exit()


MusicFile = open(sys.argv[1],"r")

OutFile = open(sys.argv[2],"w")

SongName = sys.argv[1].replace(".gbms" , "")

print(SongName)

Counter = 0

MusicData = MusicFile.read()

MusicFile.close

CStringData = "unsigned char {}[] = "

CString = CStringData.format(SongName) + "{"

Length = len(MusicData.split("|"))

print("Converting Music . . . ")


while (Length != Counter):
    Data = MusicData.split("|")
    print(Data[Counter])
    if (Data[Counter] == "0"):
            CString += "0 , 0"         
    if (Data[Counter] == "C3"):
            CString += "44 , 0 "
    if (Data[Counter] == "C3#"):
            CString += "156 , 0 "
    if (Data[Counter] == "D3"):
            CString += "262 , 1 "
    if (Data[Counter] == "D3#"):
            CString += "363 , 1 "
    if (Data[Counter] == "E3"):
            CString += "457 , 1 "
    if (Data[Counter] == "F3"):
            CString += "547 , 2 "
    if (Data[Counter] == "F3#"):
            CString += "631 , 2 "
    if (Data[Counter] == "G3"):
            CString += "710 , 2 "
    if (Data[Counter] == "G3#"):
            CString += "786 , 3 "
    if (Data[Counter] == "A3"):
            CString += "854 , 3 "
    if (Data[Counter] == "A3#"):
            CString += "923 , 3 "
    if (Data[Counter] == "B3"):
            CString += "986 , 3 "
    if (Data[Counter] == "C4"):
            CString += "1046 , 4 "
    if (Data[Counter] == "C4#"):
            CString += "1102 , 4 "
    if (Data[Counter] == "D4"):
            CString += "1155 , 4 "
    if (Data[Counter] == "D4#"):
            CString += "1205 , 4 "
    if (Data[Counter] == "E4"):
            CString += "1253 , 4 "
    if (Data[Counter] == "F4"):
            CString += "1297 , 5 "
    if (Data[Counter] == "F4#"):
            CString += "1339 , 5 "
    if (Data[Counter] == "G4"):
            CString += "1379 , 5 "
    if (Data[Counter] == "G4#"):
            CString += "1417 , 5 "
    if (Data[Counter] == "A4"):
            CString += "1452 , 5 "
    if (Data[Counter] == "A4#"):
            CString += "1486 , 5 "
    if (Data[Counter] == "B4"):
            CString += "1517 , 5 "
    if (Data[Counter] == "C5"):
            CString += "1546 , 6 "
    if (Data[Counter] == "C5#"):
            CString += "1575 , 6 "
    if (Data[Counter] == "D5"):
            CString += "1602 , 6 "
    if (Data[Counter] == "D5#"):
            CString += "1627 , 6 "
    if (Data[Counter] == "E5"):
            CString += "1650 , 6 "
    if (Data[Counter] == "F5"):
            CString += "1673 , 6 "
    if (Data[Counter] == "F5#"):
            CString += "1694 , 6 "
    if (Data[Counter] == "G5"):
            CString += "1714 , 6 "
    if (Data[Counter] == "G5#"):
            CString += "1732 , 6 "
    if (Data[Counter] == "A5"):
            CString += "1750 , 6 "
    if (Data[Counter] == "A5#"):
            CString += "1767 , 6 "
    if (Data[Counter] == "B5"):
            CString += "1783 , 6 "
    if (Data[Counter] == "C6"):
            CString += "1798 , 7 "
    if (Data[Counter] == "C6#"):
            CString += "1812 , 7 "
    if (Data[Counter] == "D6"):
            CString += "1825"
    if (Data[Counter] == "D6#"):
            CString += "1837 , 7 "
    if (Data[Counter] == "E"):
            CString += "1849 , 7 "
    if (Data[Counter] == "F6"):
            CString += "1860 , 7 "
    if (Data[Counter] == "F6#"):
            CString += "1871 , 7 "
    if (Data[Counter] == "G6"):
            CString += "1881 , 7 "
    if (Data[Counter] == "G6#"):
            CString += "1890 , 7 "
    if (Data[Counter] == "A6"):
            CString += "1899 , 7 "
    if (Data[Counter] == "A6#"):
            CString += "1907 , 7 "
    if (Data[Counter] == "B6"):
            CString += "1915 , 7 "
    if (Data[Counter] == "C7"):
            CString += "1923 , 7 "
    if (Data[Counter] == "C7#"):
            CString += "1930 , 7 "
    if (Data[Counter] == "D7"):
            CString += "1936 , 7 "
    if (Data[Counter] == "D7#"):
            CString += "1943 , 7 "
    if (Data[Counter] == "E7"):
            CString += "1949 , 7 "
    if (Data[Counter] == "F7"):
            CString += "1954 , 7 "
    if (Data[Counter] == "F7#"):
            CString += "1959 , 7 "
    if (Data[Counter] == "G7"):
            CString += "1964 , 7 "
    if (Data[Counter] == "G7#"):
            CString += "1969 , 7 "
    if (Data[Counter] == "A7"):
            CString += "1974 , 7 "
    if (Data[Counter] == "A7#"):
            CString += "1978 , 7 "
    if (Data[Counter] == "B7"):
            CString += "1982 , 7 "
    if (Data[Counter] == "C8"):
            CString += "1985 , 7 "
    if (Data[Counter] == "C8#"):
            CString += "1988 , 7 "
    if (Data[Counter] == "D8"):
            CString += "1992 , 7 "
    if (Data[Counter] == "D8#"):
            CString += "1995 , 7 "
    if (Data[Counter] == "E8"):
            CString += "1998 , 7 "
    if (Data[Counter] == "F8"):
            CString += "2001 , 7 "
    if (Data[Counter] == "F8#"):
            CString += "2004 , 7 "
    if (Data[Counter] == "G8"):
            CString += "2006 , 7 "
    if (Data[Counter] == "G8#"):
            CString += "2009 , 7 "
    if (Data[Counter] == "A8"):
            CString += "2011 , 7 "
    if (Data[Counter] == "A8#"):
            CString += "2013 , 7 "
    if (Data[Counter] == "B8"):
            CString += "2015 , 7 "
        

    if (Data[Counter] == "END"):
            CString += "0 };"
    else:
        CString += ","
    
            

    Counter += 1



DefineData = "#define {}Length {}"
OutFile.write("//Source Generated By Liquid GBMS Converter" + "\n" + CString + "\n" + "\n" + DefineData.format(SongName,Length * 2))

OutFile.close

print("Done !")

print("Thank You For Using This Software")

