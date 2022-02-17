'''
Pattern based on rows and cols input by user 
'''
#!not working currently

# rows,cols = map(int,input("Enter rows and cols: ").split())
# rows,cols = [int(x) for x in input("Enter rows and cols: ").split()]
rows= input('Rows : ')
cols = input('cols: ')
print(rows,cols)

for i in range(rows):
    for j in range(cols):
        print('*')
    print('\n')
        
        