class GGraph:
    """
    A class to represent a base graph object and used to generate a gJGF template for Gravis to
    render a relationship network graph. This should be instantiated with a dict representing
    relationships among people. This will be used to create nodes and edges in the graph. 

    """
    EDGE_MIN_SIZE = 1
    EDGE_MAX_SIZE = 3
    EDGE_LABEL_SIZE = 8
    NODE_MIN_SIZE = 1
    NODE_LABEL_SIZE = 10
    ARROW_SIZE = 3
    BORDER_COLOR = 'black'
    BORDER_SIZE = '2px'
    # Color Scheme chosen from Material Design color palettes - https://m2.material.io/design/color/the-color-system.html#tools-for-picking-colors
    PURPLE_50_A100 = '#EA80FC' # For primary node
    PINK_50_A100 = '#FF80AB'   # For secondary nodes
    BLUE_50_A100 = '#82B1FF'   # For tertiary nodes
    GREEN_50_A700 = '#00C853'   # For primary/secondary edges and arrows
    GREEN_50_A100 = '#B9F6CA'   # For tertiary edges and arrows

    def __init__(self, people: dict=None, **kwargs) -> None:

        self.directed = True
        self.label = 'Family Chart'
        # Below attributes can be overridden during instantiation
        # Nodes -
        self.node_color = self.BLUE_50_A100
        self.node_size = self.NODE_MIN_SIZE * 2
        self.node_border_color = 'black'
        self.node_label_color = 'black'
        self.node_label_size = self.NODE_LABEL_SIZE + 1
        # Edges -
        self.edge_size = self.EDGE_MIN_SIZE
        self.edge_color = self.GREEN_50_A100
        self.edge_label_color = 'black'
        self.edge_label_size = self.EDGE_LABEL_SIZE
        # Arrows -
        self.arrow_color = self.GREEN_50_A100
        self.arrow_size = self.ARROW_SIZE
        # Others -
        self.background_color = 'white'
        self.primary = False    # flag to indicate primary person exists. Only one primary is allowed in a GGraph object

        allowed_keys = list(self.__dict__.keys())
        reject_keys = [(k, v) for k, v in kwargs.items()
                                if k not in allowed_keys]
        self.__dict__.update((k, v) for k, v in kwargs.items()
                                if k in allowed_keys)
        if reject_keys:
            raise ValueError(f'Undefined keys found: {reject_keys}')

        self.graph = self._add_graph()

        if people is not None:
            # Add nodes first from people dictionary
            for _, person in people:
                self.graph = self._add_nodes(person)
            # Iterate again to create edges 
            for _, relations in people:
                self.graph += self._add_edges(relations)

    def get_graph(self):

        return self.graph
    
    def _add_graph(self):
        network = dict()
        network['graph'] = dict()
        graph = network['graph']
        graph['directed'] = self.directed
        graph['label'] = "Family Chart"
        #graph['metadata'] = dict()
        graph['metadata'] = {
            'background_color': self.background_color,
            'edge_size': self.edge_size,
            'edge_label_size': self.edge_label_size,
            'edge_label_color': self.edge_label_color,
            'edge_color': self.edge_color,
            'arrow_color': self.arrow_color,
            'arrow_size': self.arrow_size,
            'node_size': self.node_size,
            'node_color': self.node_color,
            'node_border_color': self.node_border_color,
            'node_label_color': self.node_label_color,
            'node_label_size': self.node_label_size,
        }

        return network

    def _add_nodes(self, person):
        
        nodes = self.graph['nodes']
        if nodes != None and person['id'] in nodes.keys():
                raise ValueError(f"{person['id']} already exists")
        else:
            # Validate primary person
            if self.primary and person['primary']:
                raise ValueError(f"Primary person already exists, {person['id']}, {person['name']} cannot be a primary person.")
            if person['primary']:
                # This is the first primary person found, set flag and add them
                self.primary = True
                # Create primary metadata
                metadata = {
                            'title': person['name'],
                            'size': self.NODE_MIN_SIZE * 5,
                            'color': self.PURPLE_50_A100,
                            'border_size': self.BORDER_SIZE,
                            'border_color': self.BORDER_COLOR,
                            'label_size': self.node_label_size + 2,
                            }
            else:
                # Add this person as a secondary or tertiary and create metadata accordingly
                # Use class defaults for rest of node attributes
                metadata = {
                            'title': person['name'],
                            }
            if nodes == None:   # If this is the first node, create a new dict else add to existing nodes
                nodes = dict()
            
            nodes[person['id']] = metadata
        
        self.graph['nodes'] = nodes

    def _add_edges(self, relation):

        pass


