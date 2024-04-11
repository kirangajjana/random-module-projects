row1=['❤️','❤️','❤️','❤️']
row2=['❤️','❤️','❤️','❤️']
row3=['❤️','❤️','❤️','❤️']
row4=['❤️','❤️','❤️','❤️']
matrix=[row1,row2,row3,row4]
print(matrix)
#this is a program where will store the money behind the emoji
row=int(input("enter where you want to store your money in which row"))
element=int(input("enter where you want to enter your money"))
matrix[row][element]='X'
print(f"{row1}\n {row2}\n {row3}\n {row4}\n")