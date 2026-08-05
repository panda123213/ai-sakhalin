class Matrix:
    def __init__(self,rows):
        self.rows=rows
        self.n_rows=len(rows)
        self.n_cols=len(rows[0]) if rows else 0

    def __repr__(self):
        return '\n'.join(str(row) for row in self.rows)

    def shape(self):
        return(self.n_rows,self.n_cols)


    def __add__(self, other):
    # 1. Проверяем, что размеры матриц совпадают
        if self.n_rows != other.n_rows or self.n_cols != other.n_cols:
            raise ValueError("Матрицы должны быть одинакового размера")
    
    # 2. Складываем поэлементно
        new_rows = []
        for i in range(self.n_rows):
            row = []
            for j in range(self.n_cols):
               row.append(self.rows[i][j] + other.rows[i][j])
            new_rows.append(row)
    
        return Matrix(new_rows)

    def mul_vec(self,vec):
        if len(vec) != self.n_cols:
            raise ValueError("Длина вектора не равна числу столбцов матрицы")
        result = []
        for row in self.rows:
            total =0
            for i in range(len(vec)):
                total += row[i]*vec[i]
            result.append(total)
        return result

    def __add__(self, other):
        if self.n_cols != other.n_cols or self.n_rows != other.n_rows:
            raise ValueError('матрицы должны быть одинакового размера')
        new_rows=[]
        for i in range(self.n_rows):
            row=[]
            for j in range(self.n_cols):
                row.append(self.rows[i][j]+other.rows[i][j])
            new_rows.append(row)
        return Matrix(new_rows)

    def __sub__(self, other):
        if self.n_rows != other.n_rows or self.n_cols != other.n_cols:
            raise ValueError("Матрицы должны быть одинакового размера")
        new_rows = []
        for i in range(self.n_rows):
            row = []
            for j in range(self.n_cols):
                row.append(self.rows[i][j] - other.rows[i][j])
            new_rows.append(row)
        return Matrix(new_rows)

    def mul_mat(self,other):
        if self.n_cols!= other.n_rows:
            raise ValueError('Число столбцов первой матрицы должно равняться числу строк второй')
        new_rows=[]
        for i in range (self.n_rows):
            row=[]
            for j in range (other.n_cols):
                total=0
                for k in range(self.n_cols):
                    total += self.rows[i][k] * other.rows[k][j]
                row.append(total)
            new_rows.append(row)
        return Matrix(new_rows)


    def transpose(self):
        new_rows = []
        for j in range(self.n_cols):
            new_row = []
            for i in range(self.n_rows):
                new_row.append(self.rows[i][j])
            new_rows.append(new_row)
        return Matrix(new_rows)


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print("Сложение:")
print(m1 + m2)

print("Вычитание:")
print(m1 - m2)

print("Умножение:")
print(m1.mul_mat(m2))

print("Транспонирование m1:")
print(m1.transpose())