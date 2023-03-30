from langchain.agents.load_tools import get_all_tool_names
from langchain.agents import Tool
from langflow.interface.custom_types import PythonFunction
from langchain.tools.json.tool import JsonSpec


OTHER_TOOLS = {"JsonSpec": JsonSpec}
CUSTOM_TOOLS = {"Tool": Tool, "PythonFunction": PythonFunction}
ALL_TOOLS_NAMES = set(
    get_all_tool_names() + list(CUSTOM_TOOLS.keys()) + list(OTHER_TOOLS.keys())
)
