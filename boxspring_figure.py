from pysketcher import drawing_tool, Wall, Rectangle, Composition, Spring

def set_figure_size(L, S_max, box_size):
        drawing_tool.set_coordinate_system(xmin=0, xmax=11*box_size, ymin=-(L+S_max+box_size), ymax=0.3)
        drawing_tool.set_linecolor('black')
        
def draw_figure(L, S, box_size):
        roof = Wall(x=[0,11*box_size], y=[0, 0], thickness=0.3)
        box = Rectangle(lower_left_corner=(5*box_size, -(box_size+L+S)), width=box_size, height = box_size) 
        spring = Spring(start=(5.5*box_size, -(L+S)) ,length=(L+S), width = 2, bar_length = 0.5)
        
        fig = Composition({'roof': roof,'spring': spring, 'box': box})
        
        fig.draw()
        drawing_tool.display()
        drawing_tool.erase()
    
def demo():
    L = 10 
    S_max = 5
    box_size = 4
            
    set_figure_size(L, S_max, box_size)
    
    import numpy
    S = numpy.linspace(5, -5, 100)
    for stretch in S:
        draw_figure(L, stretch, box_size)
    
if __name__ == '__main__':
    demo()