from typing import Literal

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


# state
class State(TypedDict):
    graph_str: str


# nodes
def node1(state: State) -> State:
    """this node greets the user"""
    return {"graph_str": state["graph_str"] + "Welcome to LangGraph Tutorial, Node1"}


def node2(state: State) -> State:
    """this node greets the user"""
    return {"graph_str": state["graph_str"] + "Welcome to LangGraph Tutorial, Node2"}


def node3(state: State) -> State:
    """this node greets the user"""
    return {"graph_str": state["graph_str"] + "Welcome to LangGraph Tutorial, Node3"}


# edges
def next_step(state: State) -> Literal["node2", "node3"]:
    """guide the state/graph to the next node"""
    state_str = state["graph_str"]
    array_state_str = state_str.split(" ")

    if array_state_str[0] == "hello":
        return "node2"

    return "node3"


# put the graph together

builder = StateGraph(State)

builder.add_node("node1", node1)
builder.add_node("node2", node2)
builder.add_node("node3", node3)

builder.add_edge(START, "node1")
builder.add_conditional_edges("node1", next_step)
builder.add_edge("node2", END)
builder.add_edge("node3", END)

graph = builder.compile()
