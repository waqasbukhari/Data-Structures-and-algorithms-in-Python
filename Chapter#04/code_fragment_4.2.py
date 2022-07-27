def draw_line(marks, label=''):
    print('-' * marks + ' ' + label)

def draw_interval(n):
    if n<1:
        return
    draw_interval(n-1)
    draw_line(n)
    draw_interval(n-1)    
    
def english_ruler(inches):
    for j in range(inches):
        draw_line(4, label=str(j))
        draw_interval(3)
    draw_line(4, label=str(inches))
    
    
if __name__ == "__main__":
    english_ruler(4)