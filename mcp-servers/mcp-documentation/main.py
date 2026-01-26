"""
MCP Documentation Server
Orchestrates documentation generation for decentralized applications

Tools:
1. generate_documentation - Creates 5 markdown files for GitBook
2. generate_lore - Assembles project identity into consistent narrative
3. generate_social_content - Creates 10-20 social media posts
"""

from mcp.server.fastmcp import FastMCP
from typing import Dict, List

# -------------------------------------------------
# MCP SERVER INITIALIZATION
# -------------------------------------------------
mcp = FastMCP("documentation-server")

# -------------------------------------------------
# TOOL 1: GENERATE DOCUMENTATION
# -------------------------------------------------
@mcp.tool()
def generate_documentation(
    project_name: str,
    lore: str,
    tone: str,
    project_type: str,
    goal: str,
    has_mascot: bool = False,
    tagline: str = ""
) -> str:
    """
    Generate complete documentation as multiple markdown files.

    IMPORTANT:
    - This tool DOES NOT write files itself.
    - It returns a PROMPT that will be sent to the LLM.
    - The LLM MUST output a strict JSON array of files.
    - Each file MUST contain a `path` and `content`.
    """
    
    prompt = f"""
You are an autonomous documentation generation agent.

You are NOT conversational.
You do NOT explain your reasoning.
You do NOT ask questions.
You do NOT add commentary, summaries, or meta text.

Your ONLY task is to generate documentation files.

--------------------------------
PROJECT CONTEXT
--------------------------------

Project Name: {project_name}
Project Type: {project_type}
Primary Goal: {goal}
Tone: {tone}
Tagline: {tagline if tagline else "Generate an appropriate tagline"}
Has Mascot: {"Yes" if has_mascot else "No"}

--------------------------------
PROJECT LORE
--------------------------------

{lore}

--------------------------------
TASK
--------------------------------

Generate EXACTLY 5 complete markdown documentation files.

Each file must be:
- Fully written
- Production-ready
- Suitable for GitBook or similar documentation platforms
- Written in a consistent "{tone}" tone

--------------------------------
FILES TO GENERATE
--------------------------------

1. ./docs/step1/01_introduction.md
   - Project introduction
   - What is {project_name}
   - Key features (3–5 bullet points)
   - Why the project matters
   - Quick start overview

2. ./docs/step1/02_vision.md
   - Vision statement
   - Core philosophy
   - Long-term mission
   - Community values
   - What makes the project unique

3. ./docs/step1/03_roadmap.md
   - Clear project phases or timeline
   - Key milestones
   - Short-term and long-term goals
   - Future expansion plans

4. ./docs/step1/04_tokenomics.md
   {"Generate full tokenomics breakdown" if project_type in ["defi", "token", "dao"] else "Explain project utility and economic model (no token)"}
   - Distribution (if applicable)
   - Utility / incentives
   - Supply or participation logic

5. ./docs/step1/05_faq.md
   - 10–15 frequently asked questions
   - Clear and concise answers
   - Cover basics, technical aspects, community, and roadmap

--------------------------------
STRICT OUTPUT FORMAT (MANDATORY)
--------------------------------

You MUST output ONLY a valid JSON array.
You MUST NOT wrap the output in an object.
You MUST NOT include explanations or text outside JSON.
You MUST NOT stringify the JSON.

The output MUST follow EXACTLY this structure:

[
  {{
    "path": "./docs/step1/01_introduction.md",
    "content": "<full markdown content here>"
  }},
  {{
    "path": "./docs/step1/02_vision.md",
    "content": "<full markdown content here>"
  }},
  {{
    "path": "./docs/step1/03_roadmap.md",
    "content": "<full markdown content here>"
  }},
  {{
    "path": "./docs/step1/04_tokenomics.md",
    "content": "<full markdown content here>"
  }},
  {{
    "path": "./docs/step1/05_faq.md",
    "content": "<full markdown content here>"
  }}
]

--------------------------------
CONTENT REQUIREMENTS
--------------------------------

- Each file: 800-1500 words
- Proper markdown structure (titles, subtitles, lists)
- Emojis ONLY in titles, and more if tone is "meme" or "community"
- No placeholders
- No TODOs
- No generic filler content
- Be specific, concrete, and actionable

Generate the JSON array now.

--------------------------------
LAST REQUIREMENTS
--------------------------------
After having done create those files, DO NOT CALL MPC, if files are ready, FINISH. 

"""
    
    return prompt


# -------------------------------------------------
# TOOL 2: GENERATE LORE
# -------------------------------------------------
@mcp.tool()
def generate_lore(
    project_name: str,
    project_type: str,
    tone: str,
    has_mascot: bool,
    goal: str,
    visual_vibe: str = "bold",
    user_input: str = ""
) -> str:
    """
    Assemble project identity into one cohesive, consistent narrative.
    
    Takes scattered ideas and creates a unified lore that will be used
    across all marketing materials, documentation, and social content.
    
    Args:
        project_name: Name of the project
        project_type: Type (meme, defi, nft, dao, gaming, etc.)
        tone: Narrative tone (serious, playful, meme, professional)
        has_mascot: Whether there's a mascot character
        goal: Primary objective
        visual_vibe: Visual aesthetic (bold, minimal, retro, futuristic)
        user_input: Any additional context or ideas from user
    """
    
    mascot_section = """
# MASCOT CHARACTER
If the project has a mascot, create:
- Name and personality
- Visual description (for future asset generation)
- Role in the project narrative
- Catchphrase or signature move
""" if has_mascot else ""
    
    prompt = f"""
You are a brand strategist and storyteller for Web3 projects.

# PROJECT BRIEF
- **Name**: {project_name}
- **Type**: {project_type}
- **Primary Goal**: {goal}
- **Tone**: {tone}
- **Visual Vibe**: {visual_vibe}
- **Has Mascot**: {"Yes - develop a character" if has_mascot else "No"}

# USER INPUT
{user_input if user_input else "No additional context provided"}

---

# YOUR TASK
Create a unified, consistent project lore that will serve as the foundation for ALL future content.

## OUTPUT STRUCTURE

### 1. CORE IDENTITY (2-3 sentences)
The absolute essence of {project_name}. What is it in the simplest terms?

### 2. ORIGIN STORY (1 paragraph)
How did {project_name} come to be? Keep it concise but memorable.

### 3. VISION & MISSION (3-5 bullet points)
- What we're building
- Why it matters
- Who benefits

### 4. CORE VALUES (3-4 values)
The principles that guide {project_name}

### 5. TARGET AUDIENCE
Who is this for? Be specific.

### 6. UNIQUE SELLING PROPOSITION
What makes {project_name} different from similar projects?

{mascot_section}

### 7. TONE OF VOICE GUIDELINES
- How we communicate
- Words we use
- Words we avoid
- Example phrases

### 8. KEY MESSAGING PILLARS (3-5 themes)
The main themes to emphasize in all communications

---

# REQUIREMENTS
- Keep total output to 400-600 words
- Be specific and memorable
- Ensure internal consistency
- Make it distinctive and ownable
- Align with {tone} tone and {visual_vibe} aesthetic
- This will be used as the source of truth for all content

Generate the unified lore now.
"""
    
    return prompt


# -------------------------------------------------
# TOOL 3: GENERATE SOCIAL CONTENT
# -------------------------------------------------
@mcp.tool()
def generate_social_content(
    project_name: str,
    lore: str,
    tone: str,
    platforms: List[str] = ["twitter", "telegram"],
    count: int = 15,
    content_types: List[str] = ["announcement", "engagement", "educational"]
) -> str:
    """
    Generate 10-20 social media posts optimized for X (Twitter) and Telegram.
    
    Creates ready-to-post content that maintains brand consistency and
    maximizes engagement.
    
    Args:
        project_name: Name of the project
        lore: Project narrative and identity
        tone: Social media tone
        platforms: Platforms to optimize for (twitter, telegram, discord)
        count: Number of posts to generate (10-20)
        content_types: Types of posts (announcement, meme, engagement, educational)
    """
    
    platform_specs = {
        "twitter": "280 characters, hashtags, hooks, viral potential",
        "telegram": "Longer form, community-focused, can include emojis and formatting",
        "discord": "Casual, conversational, community announcements"
    }
    
    platform_guidelines = "\n".join([
        f"- **{platform.upper()}**: {platform_specs.get(platform, 'General social media')}"
        for platform in platforms
    ])
    
    content_type_examples = {
        "announcement": "New features, updates, milestones",
        "engagement": "Questions, polls, community callouts",
        "educational": "Explaining features, benefits, how-tos",
        "meme": "Funny, relatable, shareable content",
        "hype": "Excitement building, countdowns, teasers"
    }
    
    content_guidelines = "\n".join([
        f"- **{ctype.upper()}**: {content_type_examples.get(ctype, 'General content')}"
        for ctype in content_types
    ])
    
    prompt = f"""
You are a social media manager for Web3 projects, specializing in viral content.

# PROJECT CONTEXT
**Name**: {project_name}
**Tone**: {tone}

# PROJECT LORE
{lore}

# TARGET PLATFORMS
{platform_guidelines}

# CONTENT TYPES TO CREATE
{content_guidelines}

---

# YOUR TASK
Generate {count} social media posts that are ready to publish immediately.

## DISTRIBUTION
Create a balanced mix:
- 40% engagement/community posts
- 30% educational/informative posts
- 20% announcement/update posts
- 10% meme/fun posts

## OUTPUT FORMAT
For each post, provide:

```
POST #{"{"}number{"}"}
Platform: [Twitter/Telegram/Both]
Type: [announcement/engagement/educational/meme]
---
[Post content here]
[Include hashtags for Twitter]
[Include emojis where appropriate]
---
```

## REQUIREMENTS FOR EACH POST
- **Twitter posts**: Max 280 chars, must include 2-3 relevant hashtags
- **Telegram posts**: 300-800 chars, more detailed, community-focused
- Maintain {tone} tone consistently
- Reference project lore naturally
- Include clear call-to-action (when appropriate)
- Use emojis strategically (not excessively)
- Mix educational value with entertainment
- Create posts that spark conversations
- Some posts should be time-sensitive ("This week...", "Coming soon...")
- Some posts should be evergreen (timeless value)

## SOCIAL MEDIA BEST PRACTICES
- Start with a hook (first 10 words matter most)
- Create curiosity or provide value immediately
- Use active voice
- Be conversational, not corporate
- Include numbers when possible (increases engagement)
- Ask questions to drive comments
- Create shareable moments

Generate {count} posts now.
"""
    
    return prompt


# -------------------------------------------------
# RUN SERVER
# -------------------------------------------------
if __name__ == "__main__":
    mcp.run(
        transport="sse",
    )