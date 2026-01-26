"""
MCP server – DA Lore & Assets Engine
"""

from mcp.server.fastmcp import FastMCP

# -------------------------------------------------
# MCP SERVER
# -------------------------------------------------
mcp = FastMCP("DA-Lore-Engine")


# -------------------------------------------------
# RESOURCE — LORE TEMPLATE
# -------------------------------------------------
@mcp.resource("template://da-lore")
def da_lore_template() -> str:
    """
    Base lore template for a decentralized application.
    """
    return """
You are designing the lore of a decentralized application (DA).

The lore must include:
- Vision & philosophy
- Origin story
- Core values
- Relationship with users
- Long-term mission

Tone:
- visionary
- serious
- mythological but grounded in tech
"""


# -------------------------------------------------
# PROMPT — LORE GENERATION
# -------------------------------------------------
@mcp.prompt()
def lore_prompt(project_name: str, domain: str, tone: str = "visionary") -> str:
    return f"""
Generate a complete lore for a decentralized application.

Project name: {project_name}
Domain: {domain}
Tone: {tone}

The output must be structured and immersive.
"""


# -------------------------------------------------
# TOOL — GENERATE LORE
# -------------------------------------------------
@mcp.tool()
def generate_lore(
    project_name: str,
    domain: str,
    tone: str = "visionary"
) -> str:
    """
    Generate the lore of a decentralized application.
    This tool encapsulates:
    - a lore template resource
    - a lore prompt
    """

    # 1. Load template (resource)
    template = da_lore_template()

    # 2. Build instruction (prompt)
    instruction = lore_prompt(
        project_name=project_name,
        domain=domain,
        tone=tone
    )

    # 3. Final payload for LLM (the LLM is outside MCP)
    return f"""
{template}

--- INSTRUCTION ---
{instruction}
"""


# -------------------------------------------------
# PROMPT — IMAGE DESCRIPTION
# -------------------------------------------------
@mcp.prompt()
def image_prompt(
    project_name: str,
    theme: str,
    style: str = "cinematic sci-fi"
) -> str:
    return f"""
Generate a detailed visual description for an image.

Project: {project_name}
Theme: {theme}
Style: {style}

The description must be suitable for an image generation model.
"""


# -------------------------------------------------
# TOOL — GENERATE IMAGE DESCRIPTION
# -------------------------------------------------
@mcp.tool()
def generate_image_prompt(
    project_name: str,
    theme: str,
    style: str = "cinematic sci-fi"
) -> str:
    """
    Generate an image prompt for DA branding / lore illustration.
    """

    return image_prompt(
        project_name=project_name,
        theme=theme,
        style=style
    )


# -------------------------------------------------
# RUN SERVER
# -------------------------------------------------
if __name__ == "__main__":
    mcp.run(
        transport="sse",
    )
