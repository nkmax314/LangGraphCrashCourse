from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict

# state


class State(TypedDict):
    graph_str: str


# nodes
def greeting(state: State) -> State:
    """function takes a dict and return a dict with Greeting"""
    return {
        "graph_str": state.get("graph_str", "") + " Welcome to LangGraph Crash Course"
    }


# edges

# putting our graph together

builder = StateGraph(State)

builder.add_node("greeting", greeting)

builder.add_edge(START, "greeting")
builder.add_edge("greeting", END)

graph = builder.compile()
