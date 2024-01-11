import sys


def getInputStream(path):
    if path == '-':
        return sys.stdin
    return open(path, encoding='utf-8')


def getOutputStream(path):
    return sys.stdout


class Cut:  
    def __init__(self, args):     
        self.byteRanges = args.bytes
        self.characterRanges = args.characters
        self.fieldRanges = args.fields
        self.delimiter = args.delimiter
        self.complement = args.complement
        self.onlyDelimited = args.only_delimited
        self.outputDelimiter = args.output_delimiter if hasattr(args, 'output_delimiter') else args.delimiter
        self.lineDelimiter = '' if args.zero_terminated else '\n'
        self.linesOut = list()

        if len(args.FILE) == 0:
            self.fileStreams = [sys.stdin]
        else:
            self.fileStreams = [getInputStream(file) for file in args.FILE]   
        self.rangeDirection = ['to', 'from', 'at']


    def getIndexByLength(self, index, length, rangeDirection):
        # to (0 => => index)
        if rangeDirection == self.rangeDirection[0]:
            if index <= length:
                return index
            else:
                return length
            
        # from (index => => length)
        if rangeDirection == self.rangeDirection[1]:
            if index <= length:
                return index
            else:
                return None
            
        # at (index fixed pos)
        if rangeDirection == self.rangeDirection[2]:
            if index <= length - 1:
                return index
            else:
                return None
            
    def getUtf8Len(self, str):
        return len(str.encode('utf-8'))

    def getLineCutByBytes(self, line, complement):
        lineResult = ''
        display = list()

        for index, char in enumerate(line):
            bytesLen = self.getUtf8Len(char)
            displayReps = [(complement, index)] * bytesLen
            display.extend(displayReps)
        lineLen = len(line)

        for range in self.byteRanges:
            if range.find('-') >= 0:
                if range.startswith('-'):
                    endIndex = self.getIndexByLength(int(range[1:]), lineLen, self.rangeDirection[0])

                    for index, char in enumerate(line):
                        if index < endIndex:
                            display = [(not complement,indexByte) if (index1 == index) else (comp, indexByte) for index1, (comp, indexByte) in enumerate(display)]
                elif range.endswith('-'):
                    startIndex = self.getIndexByLength(int(range[:-1]), lineLen, self.rangeDirection[1])

                    for index, char in enumerate(line):
                        # over the limit
                        if not (startIndex is None):
                            if index >= startIndex - 1:
                                display = [(not complement,indexByte) if (index1 == index) else (comp, indexByte) for index1, (comp, indexByte) in enumerate(display)]
                else: 
                    hyphenPos = range.find('-')
                    startIndex = self.getIndexByLength(int(range[:hyphenPos]), lineLen, self.rangeDirection[1])
                    endIndex = self.getIndexByLength(int(range[hyphenPos + 1:]), lineLen, self.rangeDirection[0])

                    for index, char in enumerate(line):
                        if startIndex - 1 <= index < endIndex:
                            display = [(not complement,indexByte) if (index1 == index) else (comp, indexByte) for index1, (comp, indexByte) in enumerate(display)]
            else:  
                index = self.getIndexByLength(int(range) - 1, lineLen, self.rangeDirection[2])

                # over the limit
                if not (index is None):
                    display = [(not complement,indexByte) if (index1 == index) else (comp, indexByte) for index1, (comp, indexByte) in enumerate(display)]

            lineResult = "".join(char for index, char in enumerate(line) if any((indexB == index and comp != complement) for (comp, indexB) in display))
        return lineResult   
    
    
    def getLineCutByCharacters(self, line, complement):
        lineResult = ''
        display = [complement for char in line]
        lineLen = len(line)

        for range in self.characterRanges:
            if range.find('-') >= 0:
                if range.startswith('-'):
                    endIndex = self.getIndexByLength(int(range[1:]), lineLen, self.rangeDirection[0])

                    for index, char in enumerate(line):
                        if index < endIndex:
                            display[index] = not complement
                elif range.endswith('-'):
                    startIndex = self.getIndexByLength(int(range[:-1]), lineLen, self.rangeDirection[1])

                    for index, char in enumerate(line):
                        # over the limit
                        if not (startIndex is None):
                            if index >= startIndex - 1:
                                display[index] = not complement
                else: 
                    hyphenPos = range.find('-')
                    startIndex = self.getIndexByLength(int(range[:hyphenPos]), lineLen, self.rangeDirection[1])
                    endIndex = self.getIndexByLength(int(range[hyphenPos + 1:]), lineLen, self.rangeDirection[0])

                    for index, char in enumerate(line):
                        if startIndex - 1 <= index < endIndex:
                            display[index] = not complement
            else:
                index = self.getIndexByLength(int(range) - 1, lineLen, self.rangeDirection[2])

                # over the limit
                if not (index is None):
                    display[index] = not complement
            lineResult = "".join(char for index, char in enumerate(line) if display[index])
        return lineResult
    

    def getLineCutByFields(self, line, complement):
        lineResult = ''
        fieldsList = line.split(self.delimiter)
        display = [complement for field in fieldsList]
        fieldsLen = len(fieldsList)

        for range in self.fieldRanges:
            if range.find('-') >= 0:
                if range.startswith('-'):
                    endIndex = self.getIndexByLength(int(range[1:]), fieldsLen, self.rangeDirection[0])

                    for index, field in enumerate(fieldsList):
                        if index < endIndex:
                            display[index] = not complement
                elif range.endswith('-'):
                    startIndex = self.getIndexByLength(int(range[:-1]), fieldsLen, self.rangeDirection[1])

                    for index, field in enumerate(fieldsList):
                        # over the limit
                        if not (startIndex is None):
                            if index >= startIndex - 1:
                                display[index] = not complement
                else: 
                    hyphenPos = range.find('-')
                    startIndex = self.getIndexByLength(int(range[:hyphenPos]), fieldsLen, self.rangeDirection[1])
                    endIndex = self.getIndexByLength(int(range[hyphenPos + 1:]), fieldsLen, self.rangeDirection[0])

                    # over the limit
                    if not (startIndex is None):
                        for index, field in enumerate(fieldsList):
                            if startIndex - 1 <= index < endIndex:
                                display[index] = not complement
            else:
                index = self.getIndexByLength(int(range) - 1, fieldsLen, self.rangeDirection[2])
                
                # over the limit
                if not (index is None):
                    display[index] = not complement

            if not(self.onlyDelimited and fieldsLen == 1):
                lineResult = self.outputDelimiter.join(field for index, field in enumerate(fieldsList) if display[index])
        return lineResult
        

    def dump(self, inputStream, outputStream):       
        for line in inputStream.readlines():           
            lineOut = line.strip()

            if self.byteRanges is not None and len(self.byteRanges) > 0:
                lineOut = self.getLineCutByBytes(line, self.complement)

            if self.characterRanges is not None and len(self.characterRanges) > 0:
                lineOut = self.getLineCutByCharacters(line, self.complement)

            if self.fieldRanges is not None and len(self.fieldRanges) > 0:
                lineOut = self.getLineCutByFields(line, self.complement)
            self.linesOut.append(lineOut.replace('\n', ' '))    
        result = self.lineDelimiter.join(lineOut for lineOut in self.linesOut)

        print(result)


    def __iter__(self):
        return iter(self.fileStreams)


    def __call__(self, output='-'):
        output = getOutputStream(output)

        for fileStream in self:
            self.dump(fileStream, output)