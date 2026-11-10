from langgraph.graph import END, START, StateGraph

# State


# nodes
def greeting(state: str) -> str:
    """This function greets people"""
    return state + "Welcome to LangGraph Crash Course"


# edges


# langgraph putting our graph together
builder = StateGraph(str)

# add nodes to the graph

builder.add_node("greeting", greeting)
builder.add_edge(START, "greeting")
builder.add_edge("greeting", END)

graph = builder.compile()

print(graph.invoke("hey I am new"))
