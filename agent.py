from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

# SYSTEM PROMPT
system_prompt_path = os.path.join(os.path.dirname(__file__), "system_prompt.txt")
with open(system_prompt_path, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# STATE INIT
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# LLM INIT

tool_list = [search_flights, search_hotels, calculate_budget]

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
).bind_tools(tool_list)

#AGENT
def agent_node(state: AgentState):
    messages = state["messages"]
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
    response = model.invoke(messages)

    #LOG
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"\n[!] Đang gọi bộ công trợ: {tc['name']} - Tham số: {tc['args']}...")
            
    return {"messages": [response]}

#BUILD GRAPH
graph_builder = StateGraph(AgentState)
graph_builder.add_node("agent", agent_node)

tool_node = ToolNode(tool_list)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "agent")
graph_builder.add_conditional_edges(
    "agent",
    tools_condition,
    ["tools", END]
)
graph_builder.add_edge("tools", "agent")

memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

# LOOP

if __name__ == "__main__":
    print("="*60)
    print("TravelBuddy AI Agent")
    print("="*60)
    print("Gõ 'quit' để thoát")
    print("="*60)


    while True:
        user_input = input("Bạn: ").strip()
        if user_input.lower() == "quit":
            break

        print("\nTravelBuddy đang suy nghĩ...")
        response = graph.invoke(
            {"messages": [HumanMessage(content=user_input)]},
            config={"configurable": {"thread_id": "1"}}
        )
        raw_content = response["messages"][-1].content
        
        if isinstance(raw_content, list):
            final = "".join([block["text"] for block in raw_content if isinstance(block, dict) and "text" in block])
        else:
            final = raw_content

            
        print(f"\nTravelBuddy: {final}")