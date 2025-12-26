from mcp.server.fastapi import MCPFastAPI
from tools.weather import get_weather
from tools.aqi import get_aqi
from tools.cost_of_living import get_cost_of_living

app = MCPFastAPI(name="city-info-tools")

# Register tools
app.tool()
async def get_aqi(city: str) -> dict:
    """
    Get air quality index for a city
    """
    return {
        "city": city,
        "aqi": 145,
        "level": "Moderate"
    }


app.tool()
async def get_cost_of_living(city: str) -> dict:
    """
    Get monthly cost of living estimate
    """
    return {
        "city": city,
        "monthly_cost_inr": 35000,
        "rent_included": True
    }


app.tool()
async def get_weather(city: str) -> dict:
    """
    Get current weather for a city
    """
    return {
        "city": city,
        "temperature_c": 32,
        "condition": "Sunny"
    }

