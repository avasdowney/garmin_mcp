import os
from datetime import date as dt_date, timedelta
from typing import Optional
from fastmcp import FastMCP
from garminconnect import Garmin
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mcp = FastMCP()

class MCPException(Exception):
    pass

def get_garmin_client():
    """
    Initializes and returns a Garmin client using credentials from environment variables.
    Raises MCPException if credentials are missing.
    """
    username = os.getenv("GARMIN_USERNAME")
    password = os.getenv("GARMIN_PASSWORD")
    if not username or not password:
        raise MCPException("GARMIN_USERNAME and GARMIN_PASSWORD must be set in the .env file.")
    client = Garmin(username, password)
    client.login()
    return client

@mcp.tool(
    "user_summary",
    description="Get user summary for a given date."
)
async def user_summary(date: Optional[str] = None):
    """
    Get user summary for a given date (defaults to yesterday if not provided).
    Args:
        date (Optional[str]): The date in ISO format (YYYY-MM-DD). Defaults to yesterday.
    Returns:
        dict: Success status, date, and summary data.
    Raises:
        MCPException: If an error occurs during data retrieval.
    """
    summary_date = (dt_date.fromisoformat(date or dt_date.today().isoformat()) - timedelta(days=1)).isoformat()
    try:
        client = get_garmin_client()
        summary = client.get_user_summary(summary_date)
        return {"success": True, "date": summary_date, "summary": summary}
    except Exception as e:
        raise MCPException(str(e))

@mcp.tool(
    "user_activities",
    description="Get list of user activities."
)
async def user_activities(start: Optional[str] = None, limit: Optional[int] = 10):
    """
    Get a list of user activities starting from a given date.
    Args:
        start (Optional[str]): The start date in ISO format. Defaults to 30 days ago.
        limit (Optional[int]): Maximum number of activities to return. Defaults to 10.
    Returns:
        dict: Success status and list of activities.
    Raises:
        MCPException: If an error occurs during data retrieval.
    """
    try:
        client = get_garmin_client()
        start_date = dt_date.fromisoformat(start) if start else dt_date.today() - timedelta(days=30)
        activities = client.get_activities(start_date, limit)
        return {"success": True, "activities": activities}
    except Exception as e:
        raise MCPException(str(e))

@mcp.tool(
    "user_activity_activity_id",
    description="Get details for a specific activity."
)
async def user_activity(activity_id: str):
    """
    Get details for a specific activity by activity ID.
    Args:
        activity_id (str): The ID of the activity.
    Returns:
        dict: Success status, activity ID, and activity details.
    Raises:
        MCPException: If an error occurs during data retrieval.
    """
    try:
        client = get_garmin_client()
        activity = client.get_activity_details(activity_id)
        return {"success": True, "activity_id": activity_id, "activity": activity}
    except Exception as e:
        raise MCPException(str(e))

@mcp.tool(
    "user_sleep",
    description="Get user sleep data."
)
async def user_sleep(date: Optional[str] = None):
    """
    Get user sleep data for a given date (defaults to yesterday if not provided).
    Args:
        date (Optional[str]): The date in ISO format. Defaults to yesterday.
    Returns:
        dict: Success status, date, and sleep data.
    Raises:
        MCPException: If an error occurs during data retrieval.
    """
    try:
        client = get_garmin_client()
        sleep_date = dt_date.fromisoformat(date) if date else dt_date.today() - timedelta(days=1)
        sleep_data = client.get_sleep_data(sleep_date.isoformat())
        return {"success": True, "date": sleep_date.isoformat(), "sleep": sleep_data}
    except Exception as e:
        raise MCPException(str(e))

@mcp.tool(
    "user_heart_rate",
    description="Get user heart rate data."
)
async def user_heart_rate(date: Optional[str] = None):
    """
    Get user heart rate data for a given date (defaults to yesterday if not provided).
    Args:
        date (Optional[str]): The date in ISO format. Defaults to yesterday.
    Returns:
        dict: Success status, date, and heart rate data.
    Raises:
        MCPException: If an error occurs during data retrieval.
    """
    try:
        client = get_garmin_client()
        hr_date = dt_date.fromisoformat(date) if date else dt_date.today() - timedelta(days=1)
        heart_rate = client.get_heart_rates(hr_date.isoformat())
        return {"success": True, "date": hr_date.isoformat(), "heart_rate": heart_rate}
    except Exception as e:
        raise MCPException(str(e))

@mcp.tool(
    "user_steps",
    description="Get user step count data."
)
async def user_steps(date: Optional[str] = None):
    """
    Get user step count data for a given date (defaults to yesterday if not provided).
    Args:
        date (Optional[str]): The date in ISO format. Defaults to yesterday.
    Returns:
        dict: Success status, date, and steps data.
    Raises:
        MCPException: If an error occurs during data retrieval.
    """
    try:
        client = get_garmin_client()
        steps_date = dt_date.fromisoformat(date) if date else dt_date.today() - timedelta(days=1)
        steps_data = client.get_steps_data(steps_date.isoformat())
        return {"success": True, "date": steps_date.isoformat(), "steps": steps_data}
    except Exception as e:
        raise MCPException(str(e))

@mcp.tool(
    "user_weight",
    description="Get user weight data."
)
async def user_weight(date: Optional[str] = None):
    """
    Get user weight data for a given date (defaults to yesterday if not provided).
    Args:
        date (Optional[str]): The date in ISO format. Defaults to yesterday.
    Returns:
        dict: Success status, date, and weight data.
    Raises:
        MCPException: If an error occurs during data retrieval.
    """
    try:
        client = get_garmin_client()
        weight_date = dt_date.fromisoformat(date) if date else dt_date.today() - timedelta(days=1)
        weight_data = client.get_body_composition(weight_date.isoformat())
        return {"success": True, "date": weight_date.isoformat(), "weight": weight_data}
    except Exception as e:
        raise MCPException(str(e))

# To run as an MCP tool server (HTTP transport):
mcp.run(transport="stdio")
