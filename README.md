# Garmin MCP Tool Server

This project provides a custom MCP (Model Context Protocol) tool server for accessing your Garmin health and activity data. It exposes endpoints for querying steps, heart rate, sleep, weight, and activities, and is designed to be used with GitHub Copilot's MCP integration.

## What is this project?

- A Python-based MCP tool server that connects to your Garmin account and provides endpoints for:
  - User summary
  - Activities and activity details
  - Sleep data and sleep score
  - Heart rate data
  - Step count
  - Weight/body composition

## How to start the MCP server

1. **Install dependencies**  
   In your project directory, run:
   ```
   pip install -r requirements.txt
   ```

2. **Set up your Garmin credentials**  
   Create a `.env` file in the project root with:
   ```
   GARMIN_USERNAME=your_email@example.com
   GARMIN_PASSWORD=your_password
   ```

3. **Start the MCP server**  
   Run the following command in your WSL/Ubuntu terminal:
   ```
   python garmin_mcp_server.py
   ```
   The server will start in `stdio` mode, ready for Copilot to connect.

## Example prompts to get started

- "What was my sleep score yesterday?"
- "Show my step count for July 19, 2025."
- "What is my average heart rate at night?"
- "List my activities from last week."
- "Get my weight data for the past month."
- "Show details for activity ID 123456789."