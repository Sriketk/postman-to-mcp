# 🚀 api-spec-to-mcp

**Supercharge your LLMs with automated MCP servers, straight from your existing API specs!**

---

Why reinvent the wheel? If you already have OpenAPI or Postman JSON specs, you’re 90% of the way to a fully functional MCP server for your LLM-powered tools. This project automates the boring stuff—turning your API definitions into ready-to-use MCP endpoints, so you can focus on building, not boilerplate.

Postmans jsons are not super restrictive like OPEN API specs, so this just creates a draft, This will need manual review. You also will not need all the tools provided you can remove the tools that you want with mcp.remove

This is using FASTMCP2.0

## ✨ How It Works

1. **Drop your API spec**  
   Point `script.py` to your OpenAPI or Postman JSON file.

2. **Auto-generate servers**  
   Run the script—`server.py` and all necessary subservers are created for you, no manual coding required.

3. **Plug in your API key**  
   Add your preferred API key to your `.env` file.

4. **Choose your LLM package**  
   Select the right LangChain package for your model, and you’re good to go!

---

## 🛠️ Features

- **Zero manual endpoint coding**  
- **Supports OpenAPI & Postman specs**  
- **Instant MCP server generation**  
- **Easy integration with LangChain LLMs**  

---

## 🚦 Quick Start
To get started running this project:

1. **Install [uv](https://github.com/astral-sh/uv) (a super-fast Python package/dependency manager):**
   ```bash
   pip install uv
   ```

2. **Create a virtual environment:**
   ```bash
   uv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install all dependencies:**
   ```bash
   uv sync
   ```

5. **Add any additional packages as needed:**
   ```bash
   uv add <package-name>
   ```

6. **Run the script:**
   ```bash
   python script.py
   ```

That's it! You're ready to go 🚀


