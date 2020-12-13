
# #######################
# Problem One
# #######################

class Queue:
    def __init__(self):
        self.q = []
    
    def empty(self):
        return self.q == []
    
    def enqueue(self,data):
        self.q.append(data)
    
    def dequeue(self):
        first = self.q[0]
        self.q = self.q[1:]
        return first

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []

    def add_edge(self,pair):
        start, end = pair
        self.edges[start].append(end)

    def children(self, node):
        return self.edges[node]

    def nodes(self):
        return str(self.nodes)

    def __str__(self):
        return str(self.edges)

    def bfs(self, node):
        """
        Complete this function based on the information presented in Lecture 28. 

        Parameters: node (not to start with)
        Returns: A list of visited nodes BFS --
                For all other nodes that are not visited (due to no path to the edge), 
                do a BFS untill all notes are visited (Pick from the beginning of the unvisited list)
        
        NOTE: There are no print statements in this function
        """
        visited = []
        q = Queue()
        q.enqueue(node)
        while not q.empty():
            nnode = q.dequeue()
            if nnode not in visited:
                # print(nnode)
                visited.append(nnode)
                clist = self.children(nnode)
                for n in clist:
                    if n not in visited:
                        q.enqueue(n)
        return visited

if __name__=="__main__":
    print("Problem 1")
    print()
    my_graph = Graph([1,2,3,4,5,6,7,8])
    elst = [(1,2),(1,3),(2,8),(3,5),(3,4),(5,6),(6,4),(6,7)]
    for i in elst:
        my_graph.add_edge(i)
    print("{}: {}".format("Edges", my_graph.edges))
    nlist = [1,3,6]
    print()
    for n in nlist:
        print("BFS starting with {0}\n\t{1}".format(n, my_graph.bfs(n)))
        print()
    
# ########################
# #Problem Two
# ########################
one = lambda x:"1" + x
zero = lambda x:"0" + x

def add_prefix(lst,fn, d):
    """
    DO NOT MODIFY
    """
    for i in lst:
        d[i] = fn(d[i])

def make_huffman(data):
    """
    PARAMETER: list
    RETURN: Nothing -- combine members and update dictionary, use `print(data)` to display the list

    You can make use of the lambda functions above: one, zero

    You will not return anything, you will be modifying `d` by calling `add_prefix`. 
    Do NOT modify `d` directly, just use `add_prefix`

    NOTE: You will need at least 1 print statement, potentially 2
    """
    pass

if __name__=="__main__":
    print("")
    print("*" * 40)
    print("Problem 2")
    print()
    empty = ""
    data = [[7,['w']], [12,['u']], [15,['x']],[20, ['y']],[18,['v']]]
    d = {d[1][0]:empty for d in data}
    
    print("Huffman Prcoess")
    make_huffman(data)

    print()
    print("Huffman Result")
    print(d)

# #######################
# Problem Three
# #######################

import sqlite3

connection = sqlite3.connect("mydatabase.db")
my_cursor = connection.cursor()

my_cursor.execute("DROP TABLE IF EXISTS Weather")

#create and populate database *just once*

# Use `my_cursor.exectue()` to write the queries

# TODO: Create a table
my_cursor.execute(""" CREATE TABLE Weather (
    City DATATYPE text,
    State DATATYPE text,
    High DATATYPE integer,
    Low DATATYPE integer
)""")

# TODO: Insert all 6 rows into the table
cities = [('Phoenix','Arizona',105,90), 
        ('Tucson','Arizona',101,92),
        ('Flag Staff','Arizona',105,90),
        ('San Diego','California',77,60),
        ('Albuquerque','New Mexico',80,71),
        ('Nome','Alaska',64,-54)
        ]
# my_cursor.execute("INSERT INTO Weather VALUES (?,?,?,?)",cities)
my_cursor.execute("INSERT INTO Weather VALUES ('Phoenix','Arizona','105','90')")
my_cursor.execute("INSERT INTO Weather VALUES ('Tucson','Arizona','101','92')")
my_cursor.execute("INSERT INTO Weather VALUES ('Flag Staff','Arizona','105','90')")
my_cursor.execute("INSERT INTO Weather VALUES ('San Diego','California','77','60')")
my_cursor.execute("INSERT INTO Weather VALUES ('Albuquerque','New Mexico','80','71')")
my_cursor.execute("INSERT INTO Weather VALUES ('Nome','Alaska','64','-54')")
# print(my_cursor.fetchall())

connection.commit() 


if __name__=="__main__":
    print()
    print("*" * 40)
    print("Problem 3")
    print()

    """
    # Template for each query. 
    # Replace QUERY_AS_STRING with your query as a string
    for i in my_cursor.execute(QUERY_AS_STRING):
        print(i)
    """

    print("Query 1\n")
    # TODO: QUERY 1 Select All the tuples
    # my_cursor.execute("SELECT * FROM Weather")
    # print(my_cursor.fetchall())
    for i in my_cursor.execute("SELECT * FROM Weather"):
        print(i)

    print("*"*30)
    print("Query 2\n")
    #TODO: QUERY 2 Select All the tuples where the high temperature is less than 80
    for i in my_cursor.execute("SELECT * FROM Weather WHERE High < 80"):
        print(i)

    print("*"*30)
    print("Query 3\n")
    # TODO: QUERY 3 Select All the cities where the low temperature is greater than the low of Albuquerque 
    # NOTE: You are not allowed to include the number "72.0" (or other variations) in the query itself
    for i in my_cursor.execute("SELECT City FROM Weather WHERE Low > 72 "):
        print(i)

    print("*"*30)
    print("Query 4\n")
    #TODO: QUERY 4 Select the city and temperature with the smallest low temperature 
    for i in my_cursor.execute("SELECT City,MIN(Low) FROM Weather  "):
        print(i)

    print("*"*30)
    print("Query 5\n")
    # TODO: QUERY 5 Select the city temperature with the largest high temperature 
    # NOTE: Since there are two, both cities should be returned (the query will handle returning both)
    for i in my_cursor.execute("SELECT City,MAX(High) FROM Weather"):
        print(i)

    print("*"*30)
    print("Query 6\n")
    #TODO: QUERY 6 Display the average High and Low temperatures
    # NOTE: You are not allowed to use Avg() (HINT: You can do division in a query)
    for i in my_cursor.execute("SELECT SUM(High)/COUNT(High),SUM(Low)/COUNT(Low) FROM Weather"):
        print(i)

    print("*"*30)
    print("Query 7\n")
    # TODO: QUERY 7 Give the counts of cities by their Low temperatures
    for i in my_cursor.execute("SELECT Low,COUNT(Low) FROM Weather GROUP BY Low ORDER BY Low ASC"):
        print(i)

connection.close()
