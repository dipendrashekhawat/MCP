from mcp.server.fastmcp import FastMCP

#Create an MCP Server
mcp = FastMCP("Weather Service")

# Tool
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a specified location"""
    return f"Weather in {location}: Sunny, 28°C"

# Resource
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource."""
    return f"Weather data for {location}: Sunny, 28°C"

# Prompt
@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""


# Run the server
if __name__ == "__main__":
    mcp.run()
    # mcp.run(transport="sse", port=3000)