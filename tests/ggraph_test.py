from graphs.graph import GGraph


def test_GGraph():
    
    relations = [{
                'id': 1000,    # unique Pers_id
                'name': 'John Smith',
                'primary': True,
                'related_to': [
                    {'name': 'Jane Smith', 'relation': 'husband'},
                    {'name': 'Michael Smith', 'relation': 'son'},
                    {'name': 'Kelly Smith', 'relation': 'step daughter'},
                ]
            },
             {
                'id': 1001,
                'name': 'Jane Smith',
                'related_to': [
                    {'name': 'John Smith', 'relation': 'wife'},
                    {'name': 'Michael Smith', 'relation': 'son'},
                    {'name': 'Kelly Smith', 'relation': 'daughter'},
                    {'name': 'Richard Barnes', 'relation': 'father'},
                    {'name': 'Kelly Barnes', 'relation': 'mother'},
                ]
            },
        ]

    visGraph = GGraph(people=relations)

    #print(visGraph.__dict__.keys())
    print(visGraph.get_graph())

if __name__ == "__main__":
    test_GGraph()