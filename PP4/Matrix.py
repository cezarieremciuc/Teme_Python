class Matrix():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = [[i+j for j in range(width)] for i in range(height)]
 
    # def determinant(self):
    #     """
    #     Calculates the determinant of a 1x1 or 2x2 matrix.
    #     """
    #     if not self.is_square():
    #         raise(ValueError, "Cannot calculate determinant of non-square matrix.")
    #     if self.h > 2:
    #         raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
            
    #     a = self.g[0][0]
    #     b = self.g[0][1]
    #     c = self.g[1][0]
    #     d = self.g[1][1]   
    #     return (a * d - b * c) 

    def __getitem__(self, indexes):
        return self.matrix[indexes[0]][indexes[1]]
    
    def __setitem__(self, indexes, value):
        self.matrix[indexes[0]][indexes[1]] = value

    def isSquared(self):
        return self.width == self.height

    def __repr__(self):
        matrixStr = ""
        for row in self.matrix:
            matrixStr += " ".join(["{} ".format(x) for x in row])
            matrixStr += "\n"
        return matrixStr

    def getTransposed(self):
        transposedMatrix = []
        for j in range(self.width):
            new_row = []
            for i in range(self.height):
                new_row.append(self.matrix[i][j])
            transposedMatrix.append(new_row)
        return transposedMatrix

    # Adding another matrix to self matrix
    def __add__(self, matrixToAdd):
        if self.height != matrixToAdd.height or self.width != matrixToAdd.width:
            raise(ValueError,"Matrixes can only be added if the dimensions are the same") 
        resultMatrix = [] 
        row = []
    
        for i in range(self.height):
            row = [] 
            for j in range(self.width):
                row.append(self.matrix[i][j] + matrixToAdd.matrix[i][j]) 
            resultMatrix.append(row)
    
        return resultMatrix
        
    def __mul__(self, matrix2):       
        def getLinesProduct(lineMatrix1, lineMatrix2Transposed):
            return sum([rowElementMatrix1 * rowElementMatrix2Transposed for rowElementMatrix1,rowElementMatrix2Transposed in zip(lineMatrix1,lineMatrix2Transposed)])

        result = [[0 for j in range(self.width)] for i in range(self.height)]
        matrix2Transposed = matrix2.getTransposed()
        for i in range(self.height):
            for j in range(len(matrix2Transposed)):
                result[i][j] = getLinesProduct(self.matrix[i], matrix2Transposed[j])
        return result

    def mapMatrix(self, addNumberFunction):
        resultMatrix = [[addNumberFunction(self.matrix[i][j]) for j in range(len(self.matrix[0]))] for i in range(0, len(self.matrix))]
        return resultMatrix        