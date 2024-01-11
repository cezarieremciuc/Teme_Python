from argparse import ArgumentParser
from Cut import Cut
import sys


def listOfStr(arg):
    return arg.split(',')


def parseArguments():
    cutParser = ArgumentParser()

    groupByteCharField = cutParser.add_argument_group("Required arguments")
    groupByteCharField = groupByteCharField.add_mutually_exclusive_group(required=True)

    groupByteCharField.add_argument(
        "-b", "--bytes",
        type=listOfStr,
        help="Select only these bytes"
    )

    groupByteCharField.add_argument(
        "-c", "--characters",
        type=listOfStr,
        help="select only these characters"
    )

    groupByteCharField.add_argument(
        "-f", "--fields",
        type=listOfStr,# type=lambda arg: [range for range in arg.split(',')],  
        help="select only these fields; also print any line that contains no delimiter character, unless the -s option is specified"
    )
    
    cutParser.add_argument(
        "-d", "--delimiter",
        default='\t',
        help="use DELIM instead of TAB for field delimiter"
    )

    cutParser.add_argument(
        "--complement",
        action="store_true",
        default=False,
        help="complement the set of selected bytes, characters or fields"
    )

    cutParser.add_argument(
        "-s", "--only-delimited",
        action="store_true",
        default=False,
        help="do not print lines not containing delimiters"
    )

    cutParser.add_argument(
        "--output-delimiter",
        default='\t',
        help="use STRING as the output delimiter the default is to use the input delimiter"
    )

    cutParser.add_argument(
        "-z", "--zero-terminated",
        action="store_true",
        default=False,
        help="line delimiter is NUL, not newline"
    )

    cutParser.add_argument(
        "-v","--version",
        action="store_true",
        help="show program's version number and exit"
    )
    
    cutParser.add_argument("FILE", nargs="*")
    
    parsedArgs = cutParser.parse_args()
        
    return (cutParser, parsedArgs)


def isInt(str):
    try: 
        int(str)
    except ValueError:
        return False
    else:
        return True


def getValueListFromRange(range):
    return [x for x in range.split('-')]


def validateIndexes(args):
    indexes = list()
    errorMsg = ''
    isValid = True  

    if not (args.bytes is None) :
        for range in args.bytes:
            indexes.extend(getValueListFromRange(range))

    if not (args.characters is None) :
        for range in args.characters:
            indexes.extend(getValueListFromRange(range))

    if not (args.fields is None) :
        for range in args.fields:
            indexes.extend(getValueListFromRange(range))
    try:
        indexes.remove('')
    except:
        pass

    if any(not isInt(index) for index in indexes):
        isValid = False
        errorMsg = 'ranges can be only (k)-(n) / (k),(n) / (n) with k,n integers equal or greater than 1'
    elif '0' in indexes:
        isValid = False
        errorMsg = 'ranges can be only (k)-(n) / (k),(n) / (n) with k,n integers equal or greater than 1'
    else:
        indexes = [int(x) for x in indexes]
    return (isValid, errorMsg)


def validateDelimiter(args):
    errorMsg = ''
    isValid = True  

    if args.delimiter != '\t':
        if not (args.bytes is None) or not (args.characters is None):
            isValid = False
            errorMsg = '-d --delimiter is an option for -f --fields'
        else:
            if args.fields is None:
                isValid = False
                errorMsg = '-d --delimiter is an option for -f --fields'
    return (isValid, errorMsg)


def validateOnlyDelimited(args):
    errorMsg = ''
    isValid = True  

    if args.only_delimited:
        if not (args.bytes is None) or not (args.characters is None):
            isValid = False
            errorMsg = '--only-delimited is an option for -f --fields'
        else:
            if args.fields is None:
                isValid = False
                errorMsg = '--only-delimited is an option for -f --fields'
    return (isValid, errorMsg)


def main():
    cutParser, parsedArgs = parseArguments()
    # print(parsedArgs)

    if parsedArgs.version:
        version = {}
        with open("version.py") as fileHandle:
            exec(fileHandle.read(), version)
        print(f"CUT version {version['__version__']}")
        exit(0)

    validIndexes, errorMsg = validateIndexes(parsedArgs)

    if not validIndexes:
        sys.stderr.write('error: %s\n' % ('-b | -c | -f ' + errorMsg))
        cutParser.print_usage()
        exit(1)

    validDelimiter, errorMsg = validateDelimiter(parsedArgs)
    
    if not validDelimiter:
        sys.stderr.write(f'error: {errorMsg}\n')
        cutParser.print_usage()
        exit(1)

    validOnlyDelimited, errorMsg = validateOnlyDelimited(parsedArgs)

    if not validOnlyDelimited:
        sys.stderr.write(f'error: {errorMsg}\n')
        cutParser.print_usage()
        exit(1)

    try:
        Cut(parsedArgs)()
    except Exception as error:
        print(error)
        return -1
    
    return 0           
        

if __name__ == "__main__": 
    main()      