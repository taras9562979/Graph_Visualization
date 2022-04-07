import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import math
import pickle

nodes = []  # Left-clicks on 'canvas' become graph vertices; their (x,y)-coordinates are saved as tuples into 'nodes' list
            # 'flag_mode' must be set to False (corresponds to 'Insert' clicked on the menu)
edges = []  # Two right-clicks on vertices represent an edge connecting them (as a 2-digit tuple)
colors_nodes = []  # Displays current Colors of the Nodes
colors_edges = []  # Displays current Colors of the Edges
nodes_names = []   # Displays current Names of the Nodes
shapes = []        # displays current Shapes of the Nodes (default = Circle; also Square,Triangle)
lengths = []       # displays current lengths of the Edges
edges_weights = [] # displays Weights of Edges as floats
edges_names = []   # displays Names of Edges 
node_sizes = []    # displays current Node's Size

data = (10,900,600,25,5)
radius,field_width,field_height,epsilon,delta = data
# radius -> initial radius of the Node
# epsilon -> the width of a strip around Edge on each side
# delta ->  is a margin for assuming that coordinates are the same

colors = ('wheat','deep pink','navy')
default_canvas_bg,default_node_color,default_edge_color = colors

coords = (0,0)
first_point_x,first_point_y = coords

indexes = (0,0,0,0)
first_node_index,node_moving_number,node_coloring_number,vertex_number = indexes
# first_node_index ->  
# node_moving_number -> The number of a node that was selected for moving
# node_coloring_number ->
# vertex_number -> 

flags = (False,False,False,False,False)
flag,flag_mode,flag_moving_selected,flag_edit_name,flag_vertex_shapes = flags
color_flags = (False,False)
flag_edge_coloring,flag_coloring = color_flags
delete_flags = (False,False)
flag_delete_node,flag_delete_edge = delete_flags
edge_flags = (False,False)
flag_edge_weight,flag_edge_name = edge_flags
node_flags = (False)
flag_node_size = node_flags
# flag -> False -> no nodes is selected for drawing edges(right-click); True -> one edge node is already selected
# flag_mode -> False -> Insert Mode; True -> Move Mode
# flag_moving_selected -> False #False is no nodes selected for moving; True is a node selected for moving (move mode)
# flag_coloring ->      True: Paint Node Mode is On
# flag_edge_coloring -> True: Paint Edge Mode is On
# flag_delete_node -> 
# flag_edit_name -> 
# flag_vertex_shapes ->
#flag_delete_edge - >
#flag_node_size -> True: changing Node Size mode 

selected_node_shape ='Circle' # this global variable is used to know the shape of selected node for entry in Edit Vertex Shapes
selected_node_size = radius  # default size of the Node

def move_node():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_edge,flag_delete_node
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_mode = True
    flag_coloring = False
    flag_edge_coloring = False
    flag_delete_node = False
    flag_edit_name = False
    flag_delete_edge = False
    flag_edge_weight = False
    flag_edge_name = False
    flag_node_size = False
    print('Move Mode')

def move_node_key(event):
    move_node()

def return_to_insert():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_edge,flag_delete_node
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_mode = False
    flag_coloring = False
    flag_edge_coloring = False
    flag_delete_node = False
    flag_edit_name = False
    flag_delete_edge = False
    flag_edge_weight = False
    flag_edge_name = False
    flag_node_size = False
    print('Insert Mode')

def insert_mode_key(event):
    return_to_insert()

def paint_node():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_edge,flag_delete_node
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_coloring = True
    flag_edge_coloring = False
    flag_mode = True
    flag_delete_node = False
    flag_edit_name = False
    flag_delete_edge = False
    flag_edge_weight = False
    flag_edge_name = False
    flag_node_size = False
    print('Paint Node Mode')

def paint_node_key(event):
    paint_node()

def paint_edge():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_edge,flag_delete_node
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_coloring = False
    flag_edge_coloring = True
    flag_mode = True
    flag_delete_node = False
    flag_edit_name = False
    flag_delete_edge = False
    flag_edge_weight = False
    flag_edge_name = False
    flag_node_size = False
    print('Paint Edge Mode')

def get_current_data():
    print('--------------------------------------------------------')
    print('Nodes ->  ',nodes)
    print('Node Colors -> ',colors_nodes)
    print('Node Names ->  ',nodes_names)
    print('Node Shapes ->  ',shapes)
    print('Node Sizes ->  ',node_sizes)

    print('Edges ->  ',edges)
    print('Edge Lengths ->  ',lengths)
    print('Edge Colors -> ',colors_edges)
    print('Edges Weights ->  ',edges_weights)
    print('Edges Names ->  ',edges_names)
    print('--------------------------------------------------------')

def get_current_data_key(event):
    get_current_data()

def pickling_data():
    filename = filedialog.asksaveasfilename()
    pickle_out = open(filename,'wb')
    pickle.dump(nodes,pickle_out)
    pickle.dump(edges,pickle_out)
    pickle.dump(lengths,pickle_out)
    pickle.dump(colors_nodes,pickle_out)
    pickle.dump(colors_edges,pickle_out)
    pickle.dump(nodes_names,pickle_out)
    pickle.dump(shapes,pickle_out)
    pickle.dump(edges_weights,pickle_out)
    pickle.dump(edges_names,pickle_out)
    pickle.dump(node_sizes,pickle_out)
    pickle_out.close()
    print(filename)
    print('Current Data has been saved')

def save_mode_key(event):
    pickling_data()

def loading_data():
    global nodes,edges,colors_nodes,nodes_names,shapes,lengths,node_sizes
    global colors_edges,edges_weights,edges_names
    filename =  filedialog.askopenfilename()
    print(filename)
    pickle_in = open(filename,'rb')
    nodes = pickle.load(pickle_in)
    edges = pickle.load(pickle_in)
    lengths = pickle.load(pickle_in)
    colors_nodes = pickle.load(pickle_in)
    colors_edges = pickle.load(pickle_in)
    nodes_names = pickle.load(pickle_in)
    shapes = pickle.load(pickle_in)
    edges_weights = pickle.load(pickle_in)
    edges_names = pickle.load(pickle_in)
    node_sizes = pickle.load(pickle_in)
    draw_graph()
    print('Data has been loaded')

def load_mode_key(event):
    loading_data()

def delete_edge(edge_number):
    del edges[edge_number]
    del lengths[edge_number]
    del edges_weights[edge_number]
    del colors_edges[edge_number]
    del edges_names[edge_number]

def delete_node(node_number):
    length = len(edges)
    i = 0
    while i<length:
        edge = edges[i]
        if ((edge[0]==node_number) or (edge[1]==node_number)):
        # node_number -> Node to be deleted together with all connecting edges,
        # for ex. if node_number=2, edges [i,2] and [2,i] are to be deleted
            del edges[i]
            del lengths[i]
            del colors_edges[i]
            del edges_weights[i]
            del edges_names[i]
            i -= 1
            length = len(edges)
        i += 1
      
    for i,edge in enumerate(edges):
        if edge[0]>node_number:
            edges[i][0]=edges[i][0]-1
        if edge[1]>node_number:
            edges[i][1]=edges[i][1]-1
    for i, node in enumerate(nodes):
        if i==node_number:
            del nodes[i]
            del colors_nodes[i]
            del nodes_names[i]
            del shapes[i]
            del node_sizes[i]
            print(node,'  was deleted')

    draw_graph()

def delete_nodes_mode():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_edge,flag_delete_node
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_delete_node = True
    flag_mode = True
    flag_coloring = False
    flag_edge_coloring = False
    flag_edit_name = False
    flag_delete_edge=False
    flag_edge_weight = False
    flag_edge_name = False
    flag_node_size = False
    print('Delete Nodes Mode')

def delete_edges_mode():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_delete_edge,flag_delete_node
    global flag_edge_coloring,flag_coloring
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_delete_node = False
    flag_mode = True
    flag_coloring = False
    flag_edge_coloring = False
    flag_edit_name = False
    flag_delete_edge=True
    flag_edge_weight = False
    flag_edge_name = False
    flag_node_size = False
    print('Delete Edges Mode')
    
def edit_node_name():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_node,flag_delete_edge
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_delete_node = False
    flag_mode = True
    flag_coloring = False
    flag_edge_coloring = False
    flag_edit_name = True
    flag_delete_edge=False
    flag_edge_weight = False
    flag_edge_name = False
    flag_node_size = False
    print('Edit Node Name Mode')

def edit_edge_weight():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_node,flag_delete_edge
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_delete_node = False
    flag_mode = True
    flag_coloring = False
    flag_edge_coloring = False
    flag_edit_name = False
    flag_delete_edge = False
    flag_edge_weight = True
    flag_edge_name = False
    flag_node_size = False
    print('Edit Edge Weight')

def edit_edge_name():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_node,flag_delete_edge
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_delete_node = False
    flag_mode = True
    flag_coloring = False
    flag_edge_coloring = False
    flag_edit_name = False
    flag_delete_edge = False
    flag_edge_weight = False
    flag_edge_name = True
    flag_node_size = False
    print('Edit Edge Name')

def edit_node_size():
    global flag_mode,flag_edit_name,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_node,flag_delete_edge
    global flag_edge_name,flag_edge_weight
    global flag_node_size
    flag_vertex_shapes = False
    flag_delete_node = False
    flag_mode = True
    flag_coloring = False
    flag_edge_coloring = False
    flag_edit_name = False
    flag_delete_edge = False
    flag_edge_weight = False
    flag_edge_name = False
    flag_node_size = True
    print('Edit Node Size')

def get_left_click(event):
    global flag_mode,node_moving_number,flag_moving_selected,field_width,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_edge_weight,flag_edge_name
    global flag_node_size
    global vertex_number,node_coloring_number
    global selected_node_shape,selected_node_size
    global epsilon,delta,radius
    x = event.x
    y = event.y

    if not flag_mode:
        nodes.append([x,y])
        colors_nodes.append(default_node_color)
        #colors_edges.append(default_edge_color)
        nodes_names.append('Empty')
        shapes.append('Circle')
        node_sizes.append(radius)
        #lengths.append('X')
        print('Nodes ->  ',nodes)
        #print('Node Color ->  ',colors_nodes)
        #print('Edge Color ->  ',colors_edges)
        #print('Nodes Names ->  ',nodes_names)
        #print('Node Shapes ->  ',shapes)
    else:
        # run through the list of nodes and determine which one is selected
        for node in nodes:
            distance=math.sqrt((node[0]-x)**2+(node[1]-y)**2)
            if distance <= radius:
                if flag_delete_node and (not flag_edit_name):
                    node_number = nodes.index(node)
                    delete_node(node_number)
                if (not flag_delete_node) and (not flag_edit_name):
                    if not flag_coloring:
                        node_moving_number=nodes.index(node)
                        flag_moving_selected = True
                    if flag_coloring:
                        node_coloring_number=nodes.index(node)
                        [rgb,hx]= colorchooser.askcolor()
                        #print('rgb = ',rgb)
                        #print('hx = ',hx)
                        if hx!=None:
                            colors_nodes[node_coloring_number] = hx
                        print('Node Color ->  ',colors_nodes[node_coloring_number])        
                if flag_edit_name:
                    node_number = nodes.index(node)
                    answer = simpledialog.askstring("Input", "Enter the name of the Node",initialvalue=nodes_names[node_number],parent=field)
                    if answer is not None:
                        print("Node Name ->  ", answer)
                        nodes_names[node_number] = answer
                if flag_vertex_shapes:
                    flag_moving_selected = False
                    vertex_number = nodes.index(node)
                    selected_node_shape=shapes[vertex_number]
                    print('Node Shape ->  ',selected_node_shape)

                    d = MyDialog(field)
                    if d.result!=None:  # not a Cancel button
                        if d.result==0:
                            shapes[vertex_number] = 'Circle'
                        if d.result==1:
                            shapes[vertex_number] = 'Square'
                        if d.result==2:
                            shapes[vertex_number] = 'Triangle'    
                        # result - built-in response variable in simpledialog Class
                        # 0 -> Square, 1 -> Circle, 2 -> Triangle
                    #print("d.result = " + str(d.result))
                    #print('Vertex Number ->  ',vertex_number)
                if flag_node_size:
                    flag_moving_selected = False
                    vertex_number = nodes.index(node)
                    selected_node_size=node_sizes[vertex_number]
                    print('Node Size ->  ',selected_node_size)

                    size_dialog = Node_Size_Dialog(field)
                    if size_dialog.result!=None:  # not a Cancel button
                        if size_dialog.result==0:
                            node_sizes[vertex_number] = radius
                        if size_dialog.result==1:
                            node_sizes[vertex_number] = 2*radius
                        if size_dialog.result==2:
                            node_sizes[vertex_number] = 3*radius
                        if size_dialog.result==3:
                            node_sizes[vertex_number] = int(0.1*scale_value*radius)           

        for i,edge in enumerate(edges):
            node_beginning=edge[0]
            node_end=edge[1]
            x1=nodes[node_beginning][0]
            y1=nodes[node_beginning][1]
            x2=nodes[node_end][0]
            y2=nodes[node_end][1]
            average_x = (x1+x2)/2
            if abs(x2-x1)>delta:
                slope=(y2-y1)/(x2-x1)
                y_on_the_edge=slope*(x-x1)+y1
            else:
                slope = 0
                y_on_the_edge=y # as it can be any number
            #if (abs(y-y_on_the_edge)<=epsilon) and (x>=min(x1,x2)-delta) and (x<=max(x1,x2)+delta):
            general = abs(y-y_on_the_edge)<=epsilon
            vertical = abs(x-average_x)<=5*radius
            regular = (x>=min(x1,x2)+max(radius,delta)) and (x<=max(x1,x2)-max(radius,delta))
            if general:
                if flag_delete_edge: 
                    print('Edge (',node_beginning,' ',node_end,') was deleted')
                    delete_edge(i)
                    break
                # use max(radius,delta) to disable Edge Painting when clicked on the Node
                # as there is a conflict with other edges connected to that Node
                if (flag_edge_coloring and vertical) or (flag_edge_coloring and regular):
                    print('Edge (',node_beginning,' ',node_end,') was chosen for repainting')
                    [rgb,hx]= colorchooser.askcolor()
                    if hx!=None:
                        colors_edges[i] = hx
                        print('Edge Color ->  ',colors_edges[i])
                    break
                if (flag_edge_weight and vertical) or (flag_edge_weight and regular):
                    print('Edge (',node_beginning,' ',node_end,') was chosen for Weight update')
                    answer = simpledialog.askstring("Input", "Enter the Weight of the Edgee",initialvalue=edges_weights[i],parent=field)
                    if answer is not None:
                        print("Edge Weight ->  ", answer)
                        edges_weights[i] = float(answer)
                if (flag_edge_name and vertical) or (flag_edge_name and regular):
                    print('Edge (',node_beginning,' ',node_end,') was chosen for Name update')
                    answer = simpledialog.askstring("Input", "Enter the Weight of the Edgee",initialvalue=edges_names[i],parent=field)
                    if answer is not None:
                        print("Edge Name ->  ", answer)
                        edges_names[i] = answer
                                                      
    draw_graph()

def get_right_click(event):
    global radius,flag, first_point_x, first_point_y, flag_mode, first_node_index
    x = event.x
    y = event.y
    for node in nodes:  # node is a dynamic tuple running through all the tuples in 'nodes' list created so far
        distance=math.sqrt((node[0]-x)**2+(node[1]-y)**2)
        if distance > radius:
            continue  
        if not flag_mode:  # so that edges can be created only in Insert Mode
            if not flag:   # no node of the future edge was selected by right-click yet
                first_point_x = x
                first_point_y = y
                first_node_index = nodes.index(node) 
                flag = True
            else:
                second_node_index=nodes.index(node)
                edges.append([first_node_index,second_node_index])
                L = math.sqrt((first_point_x-x)**2 + (first_point_y-y)**2)
                L = int(L//1)
                lengths.append(L)
                edges_weights.append(0.0)
                edges_names.append('edge')
                colors_edges.append(default_edge_color)

                first_point_x = 0
                first_point_y = 0
                flag = False
                print('Edges ->  ',edges) 
    draw_graph() 

def moving_mouse(event):
    global node_moving_number,flag_moving_selected,flag_mode
    if flag_mode and flag_moving_selected and not flag_edge_coloring:
        x=event.x
        y=event.y
        if x<0: x = 0
        if y<0: y = 0
        nodes[node_moving_number][0]=x
        nodes[node_moving_number][1]=y
        draw_graph()

def releasing_mouse(event):
    global node_moving_number,flag_moving_selected,flag_mode
    if flag_mode and flag_moving_selected:
        flag_moving_selected = False
        node_moving_number = 0
        draw_graph()
    
def draw_graph():   # drawing graph directly from code
    global radius,flag_vertex_shapes,vertex_number,L
   
    canvas.delete('all')
    for e,edge in enumerate(edges):
        i = edge[0]
        j = edge[1]
        x1 = nodes[i][0] 
        y1 = nodes[i][1]
        x2 = nodes[j][0]
        y2 = nodes[j][1]
        average_x = (x1+x2)/2
        average_y = (y1+y2)/2
        canvas.create_text(average_x+15,average_y+15,text=lengths[e])
        canvas.create_line(x1,y1,x2,y2,width=3,fill=colors_edges[e],arrow=tk.LAST,arrowshape=(20,30,15))   
        L = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        L = int(L//1)
        lengths[e] = L
    for i,node in enumerate(nodes):
        if shapes[i]=='Circle':
            x = node[0]
            y = node[1]
            color_node_index=nodes.index(node)
            #canvas.create_oval(x-radius,y-radius,x+radius,y+radius,fill=colors_nodes[color_node_index])
            canvas.create_oval(x-node_sizes[i],y-node_sizes[i],x+node_sizes[i],y+node_sizes[i],fill=colors_nodes[color_node_index])
            canvas.create_text(x,y-25,text=nodes_names[i])
        if shapes[i]=='Square':
            x = node[0]
            y = node[1]
            color_node_index=nodes.index(node)
            #canvas.create_rectangle(x-radius,y-radius,x+radius,y+radius,fill=colors_nodes[color_node_index])
            canvas.create_rectangle(x-node_sizes[i],y-node_sizes[i],x+node_sizes[i],y+node_sizes[i],fill=colors_nodes[color_node_index])
            canvas.create_text(x,y-25,text=nodes_names[i])
        if shapes[i]=='Triangle':
            x = node[0]
            y = node[1]
            color_node_index=nodes.index(node)
            #canvas.create_polygon(x-radius,y+radius,x,y-radius,x+radius,y+radius,fill=colors_nodes[color_node_index])
            canvas.create_polygon(x-node_sizes[i],y+node_sizes[i],x,y-node_sizes[i],x+node_sizes[i],y+node_sizes[i],fill=colors_nodes[color_node_index])
            canvas.create_text(x,y-25,text=nodes_names[i])

def vertex_shapes():
    global flag_mode,flag_edit_name,flag_moving_selected,flag_vertex_shapes
    global flag_edge_coloring,flag_coloring
    global flag_delete_edge,flag_delete_node
    global flag_edge_weight,flag_edge_name
    global flag_node_size
    flag_vertex_shapes = True
    flag_delete_node = False
    flag_mode = True
    flag_moving_selected = False
    flag_coloring = False
    flag_edge_coloring = False
    flag_edit_name = False
    flag_delete_edge=False
    flag_edge_weight = False
    flag_edge_name = False
    flag_node_size = False
    print('Edit Node Shape Mode')

def to_help():
    hlp = tk.Tk()
    hlp.title('Info')
    hlp.geometry('500x300')

    txt = tk.Text(hlp,font=('Times',15,'bold'),bg='lightgreen',fg='brown')
    txt.insert(1.0,'Ctrl-i -> Insert Mode\nCtrl-m -> Move Mode\nCtrl-p -> Paint Mode\n')
    txt.insert(2.0,'Ctrl-s -> Save Mode\nCtrl-l -> Load Mode\nCtrl-g -> Get Current Data\n')
    txt.pack()
    hlp.mainloop()


class MyDialog(tk.simpledialog.Dialog):
    global selected_node_shape
    tracer=0 # checks values inside simpledialog

    def body(self, master): # self-activates(callback) when simpledialog is created
        global selected_node_shape

        if selected_node_shape=='Circle': selected_node_shape_number = 0
        if selected_node_shape=='Square': selected_node_shape_number = 1
        if selected_node_shape=='Triangle': selected_node_shape_number = 2

        self.tracer = selected_node_shape_number
        # to make sure that the choice does NOT automatically returns to default 
        
        def show_choice():
            #print("Choice")
            #print('i.get() ->  ',i.get())
            self.tracer=i.get()

        i = tk.IntVar() # this int values is tied to the Radiobutton
        i.set(selected_node_shape_number)

        self.e1 = tk.Radiobutton(master,text='Circle',variable=i,value=0,command=show_choice)
        self.e1.pack()  
        self.e2 = tk.Radiobutton(master,text='Square',variable=i,value=1,command=show_choice)
        self.e2.pack()  
        self.e3 = tk.Radiobutton(master,text='Triangle',variable=i,value=2,command=show_choice)
        self.e3.pack()

    def apply(self):
        self.result = self.tracer
        #print("Apply")   
        

class Node_Size_Dialog(tk.simpledialog.Dialog):
    global selected_node_size,i
    tracer=0 # checks values inside simpledialog

    def body(self, master): # self-activates(callback) when simpledialog is created
        global selected_node_size,i
        global selected_node_size_number
        i = tk.IntVar()

        sigma = 0.5
        r1 = selected_node_size!=radius
        r2 = selected_node_size!=2*radius
        r3 = selected_node_size!=3*radius

        if r1 and r2 and r3: selected_node_size_number = 3

        if selected_node_size==radius: selected_node_size_number = 0
        #if selected_node_size==2*radius: selected_node_size_number = 1
        if abs(selected_node_size-2*radius)<sigma : selected_node_size_number = 1
        if selected_node_size==3*radius: selected_node_size_number = 2
        
        

        self.tracer = selected_node_size_number

        def show_choice():
            global scale_value,i
            scale_value = self.scl_1.get()
            #print("Choice")
            #print('i.get() ->  ',i.get())
            self.tracer=i.get()

        def scale_moved(position):
            global scale_value,i
            global selected_node_size_number
            
            #scale_value = self.scl_1.get()
            #scale_value==10:
            scale_value = int(position)


            rr1 = (int(position)!=radius)
            rr2 = (int(position)!=(2*radius))
            rr3 = (int(position)!=3*radius)

            if (rr1 and rr2 and rr3): selected_node_size_number = 3
            
            if int(position)==(radius):   selected_node_size_number = 0
            if int(position)==(2*radius): selected_node_size_number = 1
            if int(position)==(3*radius): selected_node_size_number = 2

            '''if position==radius:   selected_node_size_number = 0
            elif position==2*radius: selected_node_size_number = 1
            elif position==3*radius: selected_node_size_number = 2
            else: selected_node_size_number = 3'''
        
            
            i.set(selected_node_size_number)
            print(type(int(position)),int(position))
            print(scale_value,' ',selected_node_size_number,'  ',radius)
            print(rr1,rr2,rr3,sep='  ')
            
        #i = tk.IntVar() # this int values is tied to the Radiobutton
        i.set(selected_node_size_number)

        self.e1 = tk.Radiobutton(master,text='Small',variable=i,value=0,command=show_choice)
        #self.e1.pack()  
        self.e1.grid(row=0,column=0)
        self.e2 = tk.Radiobutton(master,text='Medium',variable=i,value=1,command=show_choice)
        #self.e2.pack()  
        self.e2.grid(row=0,column=1)
        self.e3 = tk.Radiobutton(master,text='Large',variable=i,value=2,command=show_choice)
        #self.e3.pack()
        self.e3.grid(row=0,column=2)
        self.e4 = tk.Radiobutton(master,text='Scale Value',variable=i,value=3,command=show_choice)
        self.e4.grid(row=0,column=3)

        self.lb1=tk.Label(master,text='Selected Size')
        self.lb1.grid(row=1,column=0,columnspan=4)
        
        self.scl_1 = tk.Scale(master,orient='horizontal',width=25,from_=radius,to=3*radius,command=scale_moved)
        self.scl_1.set(selected_node_size)
        self.scl_1.grid(row=2,column=0,columnspan=4,sticky='ew')
        
    '''def get_scale_value(self):
            scale_value = self.scl_1.get()
            #print('Scale Value ->  ',scale_value)
            return scale_value'''

    def apply(self):
        self.result = self.tracer
        #print("Apply")   

field = tk.Tk()
field.title('GRAPH VISUALIZATION')

# Creating Menu
control = tk.Menu(field)
# Cascades
menu_item = tk.Menu(control)
menu_edge_data = tk.Menu(control)
menu_node_data = tk.Menu(control)
paint_menu = tk.Menu(control)

control.add_command(label='Insert',command=return_to_insert)
control.add_command(label='Move',command=move_node)

control.add_cascade(label='Paint',menu=paint_menu)
paint_menu.add_command(label='Node',command=paint_node)
paint_menu.add_command(label='Edge',command=paint_edge)

control.add_command(label='Get Data',command=get_current_data)
control.add_command(label='Save',command=pickling_data)
control.add_command(label='Load',command=loading_data)

control.add_cascade(label='Delete',menu=menu_item)
menu_item.add_command(label='Node',command=delete_nodes_mode)
menu_item.add_command(label='Edge',command=delete_edges_mode)

control.add_cascade(label='Node Data',menu=menu_node_data)
menu_node_data.add_command(label='Edit Node Shape',command=vertex_shapes)
menu_node_data.add_command(label='Edit Node Name',command=edit_node_name)
menu_node_data.add_command(label='Edit Node Size',command=edit_node_size)

control.add_cascade(label='Edge Data',menu=menu_edge_data)
menu_edge_data.add_command(label='Weight',command=edit_edge_weight)
menu_edge_data.add_command(label='Name',command=edit_edge_name)
menu_edge_data.add_command(label='Show')

control.add_command(label='Help',command=to_help)
field.config(menu=control)

canvas = tk.Canvas(field,width=field_width,height=field_height,bg=default_canvas_bg)
canvas.pack(fill='both',expand='1')
# to make canvas expand if we cross initial borders

# Mouse binds
field.bind('<Button-1>',get_left_click)          # binding function with left mouse click
field.bind('<Button-3>',get_right_click)         # binding function with right mouse click
field.bind('<B1-Motion>',moving_mouse)           # binding function with left mouse click-and-drag
field.bind('<ButtonRelease-1>',releasing_mouse)  # binding function with left mouse release

# Button combination binds
field.bind('<Control-m>',move_node_key)          
field.bind('<Control-p>',paint_node_key)         
field.bind('<Control-i>',insert_mode_key)
field.bind('<Control-g>',get_current_data_key) 
field.bind('<Control-s>',save_mode_key)
field.bind('<Control-l>',load_mode_key)        

print('Insert Mode')

field.mainloop()
