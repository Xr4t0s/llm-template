"""
MCP Documentation Server
Orchestrates documentation generation for decentralized applications

Tools:
1. generate_documentation - Creates 5 markdown files for GitBook
2. generate_lore - Assembles project identity into consistent narrative
3. generate_social_content - Creates 10-20 social media posts
4. generate_landing_page - Creates production-ready HTML landing page
5. generate_image_prompts - Creates AI image generation prompts for project assets
"""
from mcp.server.fastmcp import FastMCP
from typing import Dict, List, Optional

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
# TOOL 4: GENERATE LANDING PAGE
# -------------------------------------------------
@mcp.tool()
def generate_landing_page(
    project_name: str,
    lore: str,
    tone: str,
    goal: str = "convert",
    target_audience: str = "Web3 users",
    primary_cta: str = "Get Started",
    secondary_cta: str = "Learn More",
    key_features: Optional[List[str]] = None,
    sections: List[str] = ["hero", "problem", "solution", "features", "how_it_works", "social_proof", "faq", "final_cta", "footer"],
    include_seo: bool = True,
    include_faq_count: int = 6,
    color_palette: List[str] = ["indigo", "lime"]
) -> str:
    """
    Generate a production-ready HTML/CSS landing page for a Web3 project.

    Creates a complete, single-file HTML landing page with embedded CSS,
    ready to upload to Hostinger or any web host.

    Args:
        project_name: Name of the project
        lore: Project narrative and identity
        tone: Brand tone (ex: premium, aggressive, funny, mysterious, clean, degen, serious)
        goal: Landing page objective (convert, whitelist, waitlist, mint, presale, download, utility)
        target_audience: Who this page is for
        primary_cta: Main CTA button text
        secondary_cta: Secondary CTA button text
        key_features: List of key features/benefits (optional)
        sections: Sections to include in the landing page
        include_seo: Whether to generate SEO meta tags
        include_faq_count: Number of FAQs to generate
        color_palette: Color scheme for the design
    """

    if key_features is None:
        key_features = [
            "Fast onboarding",
            "Real utility",
            "Community-first design",
            "Secure by default",
            "Built for scale"
        ]

    section_specs = {
        "hero": "Hero section with hook, subheadline, CTAs, and a quick credibility line",
        "problem": "Problem statement: what sucks today and why users care",
        "solution": "Your unique solution and the key promise",
        "features": "3-6 feature cards with benefits (not just features)",
        "how_it_works": "Step-by-step explanation (3 steps max, super clear)",
        "tokenomics": "Token utility + distribution summary (only if relevant)",
        "roadmap": "Short roadmap with milestones (Now / Next / Later)",
        "social_proof": "Community, stats, testimonials placeholders, partners, logos",
        "faq": "FAQs that remove friction and objections",
        "final_cta": "A strong closing section that pushes action",
        "footer": "Footer links: docs, socials, legal, contact"
    }

    sections_guidelines = "\n".join([
        f"- **{s.upper()}**: {section_specs.get(s, 'Custom section')}"
        for s in sections
    ])

    features_guidelines = "\n".join([f"- {f}" for f in key_features])

    color_scheme = " + ".join(color_palette)

    prompt = f"""
You are a senior Web3 frontend developer and conversion expert.

Your mission: create a PRODUCTION-READY, SINGLE-FILE HTML landing page that can be uploaded directly to Hostinger.

# PROJECT CONTEXT
**Name**: {project_name}
**Tone**: {tone}
**Goal**: {goal}
**Target audience**: {target_audience}
**Color Palette**: {color_scheme}

# PROJECT LORE (IDENTITY / STORY)
{lore}

# KEY FEATURES / BENEFITS
{features_guidelines}

# SECTIONS TO GENERATE
{sections_guidelines}

---

# YOUR TASK
Generate a COMPLETE, PRODUCTION-READY HTML file with embedded CSS.

## TECHNICAL REQUIREMENTS
- Single HTML file with all CSS in <style> tags
- Fully responsive (mobile-first design)
- Modern, clean design using the {color_scheme} color palette
- No external dependencies (no Bootstrap, no frameworks)
- Optimized for fast loading
- Cross-browser compatible
- Semantic HTML5
- Accessible (ARIA labels where needed)

## DESIGN REQUIREMENTS
- Modern Web3 aesthetic
- Clean, professional layout
- Smooth scrolling
- Hover effects on interactive elements
- Mobile hamburger menu
- Gradient backgrounds using {color_scheme} colors
- Professional typography (use Google Fonts via CDN)
- Card-based layouts for features
- Proper spacing and white space
- Call-to-action buttons that stand out

## COPYWRITING RULES
- Hook must be strong (first line should hit hard)
- Speak benefits > features
- Minimal fluff, max clarity
- Use short sentences
- Keep the tone **{tone}** consistently
- Include trust signals (security, transparency, community)
- Avoid vague claims unless backed by specifics
- Make it skimmable: headings, bullets, blocks

## CTA RULES
- Primary CTA text: **{primary_cta}**
- Secondary CTA text: **{secondary_cta}**
- CTA should appear multiple times (hero + middle + final)
- CTAs should be prominent and use contrasting colors

## SEO REQUIREMENTS
{"- Include complete meta tags (title, description, keywords, Open Graph, Twitter Card)" if include_seo else "- Include basic meta tags"}
- Proper heading hierarchy (H1, H2, H3)
- Alt text for all images (use placeholder descriptions)
- Semantic HTML structure

## FAQ REQUIREMENTS
- Generate {include_faq_count} FAQs
- Must include: "Is it safe?", "How do I start?", "What makes you different?"
- Use accordion-style layout (expandable/collapsible)
- Add simple JavaScript for accordion functionality

---

# OUTPUT FORMAT

Return ONLY the complete HTML code, starting with <!DOCTYPE html> and ending with </html>.

The HTML must include:
1. Complete <!DOCTYPE html> declaration
2. <head> section with:
   - Meta tags (charset, viewport, SEO)
   - Title tag
   - Google Fonts link
   - Embedded CSS in <style> tags
3. <body> section with:
   - Navigation bar (sticky)
   - All requested sections in order
   - Footer
4. Embedded JavaScript for:
   - Mobile menu toggle
   - FAQ accordion
   - Smooth scrolling
   - Any interactive elements

## IMPORTANT
- Return ONLY the HTML code, no explanations
- Use placeholder images from https://via.placeholder.com/
- Make it ready to save as index.html and upload immediately
- Ensure all links are placeholder hrefs (#)
- Add HTML comments to mark each section clearly
- Use proper indentation for readability

Generate the complete HTML file now.
"""

    return prompt


# -------------------------------------------------
# TOOL 5: GENERATE IMAGE PROMPTS (STEP 3)
# -------------------------------------------------


@mcp.tool()
def generate_image_prompts(
    project_name: str,
    lore: str,
    visual_vibe: str,
    tone: str,
    has_mascot: bool = False,
    mascot_description: str = "",
    asset_types: Optional[List[str]] = None,
    art_style: str = "modern digital art",
    color_palette: Optional[List[str]] = None,
    count_per_type: int = 3
) -> str:
    """
    Generate AI image generation prompts for exactly 5 project visual assets:
    - logo
    - banner
    - meme_1
    - meme_2
    - newbuy_telegram

    Returns a single instruction prompt for an LLM that MUST output a strict JSON
    object matching the required schema (no markdown, no commentary).
    """

    # Palette default
    if color_palette is None:
        color_palette = ["indigo", "lime", "black"]

    color_scheme = ", ".join(color_palette)

    # EXACTLY 5 assets (fixed set, no filtering)
    canonical_assets = [
        {
            "type": "logo",
            "name": "Logo",
            "aspect_ratio": "1:1",
            "recommended_size": "1024x1024px",
            "use_case": "Profile picture, app icon, branding",
            "recommended_tool": "Midjourney/DALL-E/Flux/SD",
            "parameters": "--ar 1:1 --style raw --v 6",
        },
        {
            "type": "banner",
            "name": "Banner",
            "aspect_ratio": "3:1",
            "recommended_size": "1500x500px",
            "use_case": "Website hero / X (Twitter) header / wide marketing header",
            "recommended_tool": "Midjourney/DALL-E/Flux/SD",
            "parameters": "--ar 3:1 --v 6",
        },
        {
            "type": "meme_1",
            "name": "Meme Template 1",
            "aspect_ratio": "1:1",
            "recommended_size": "1080x1080px",
            "use_case": "Shareable meme content for social media (template-friendly)",
            "recommended_tool": "Midjourney/DALL-E/Flux/SD",
            "parameters": "--ar 1:1 --v 6",
        },
        {
            "type": "meme_2",
            "name": "Meme Template 2",
            "aspect_ratio": "1:1",
            "recommended_size": "1080x1080px",
            "use_case": "Second meme template with different composition/layout",
            "recommended_tool": "Midjourney/DALL-E/Flux/SD",
            "parameters": "--ar 1:1 --v 6",
        },
        {
            "type": "newbuy_telegram",
            "name": "New Buy Telegram Card",
            "aspect_ratio": "1:1",
            "recommended_size": "1080x1080px",
            "use_case": "Telegram post/card image for 'New Buy' alerts (clear, readable, high contrast)",
            "recommended_tool": "Midjourney/DALL-E/Flux/SD",
            "parameters": "--ar 1:1 --style raw --v 6",
        },
    ]

    # Build strict schema example (LLM must follow)
    assets_schema_example_lines = []
    for a in canonical_assets:
        assets_schema_example_lines.append(
            f"""{{
      "type": "{a['type']}",
      "name": "{a['name']}",
      "aspect_ratio": "{a['aspect_ratio']}",
      "recommended_size": "{a['recommended_size']}",
      "use_case": "{a['use_case']}",
      "recommended_tool": "{a['recommended_tool']}",
      "parameters": "{a['parameters']}",
      "prompts": [
        {{"variation": 1, "prompt": "<Complete AI image generation prompt here, 75-150 words>"}},
        {{"variation": 2, "prompt": "<Complete AI image generation prompt here, 75-150 words>"}},
        {{"variation": 3, "prompt": "<Complete AI image generation prompt here, 75-150 words>"}}
      ]
    }}"""
        )

    assets_schema_example = ",\n    ".join(assets_schema_example_lines)

    allowed_types = ", ".join([a["type"] for a in canonical_assets])

    prompt = f"""
You are an expert AI image prompt engineer specializing in Web3 and crypto project branding.

PROJECT CONTEXT
- Name: {project_name}
- Visual Vibe: {visual_vibe}
- Art Style: {art_style}
- Tone: {tone}
- Color Palette: {color_scheme}

PROJECT LORE
{lore}

TASK
Generate exactly {count_per_type} optimized AI image generation prompt variations for EACH of the 5 assets below:
- logo
- banner
- meme_1
- meme_2
- newbuy_telegram

PROMPT RULES
- Each prompt must be 75–150 words.
- Must be cohesive as a brand family across all assets.
- Must incorporate the palette ({color_scheme}) with explicit usage instructions (dominant/accent/gradient/etc.).
- Reflect {visual_vibe} and {tone} in composition/subject/mood.
- Avoid vague terms; be concrete and visual.
- Avoid conflicting style instructions.

ASSET-SPECIFIC RULES
- logo: scalable, iconic, minimal clutter, works in black & white, readable at small sizes.
- banner: wide composition, strong focal point, leave intentional negative space for overlay text.
- meme_1: template-friendly, obvious caption zones, clean negative space, instantly readable.
- meme_2: different layout than meme_1 (different framing/composition), still template-friendly.
- newbuy_telegram: looks like a clean alert/notification card image, high contrast, readable typography space,
  includes visual hints of "new buy" / "signal" / "alert" WITHOUT using brand names of exchanges; keep it professional.

STRICTNESS (NON-NEGOTIABLE)
- You MUST output exactly 5 assets.
- The "type" field MUST be one of: {allowed_types}.
- Do NOT invent any other asset types (e.g., "documentation", "twitter_profile", etc.).
- Do NOT omit any required fields.
- If you cannot comply, output exactly: {{"assets": []}}.

OUTPUT REQUIREMENTS (VERY IMPORTANT)
- Output MUST be valid JSON and NOTHING ELSE (no markdown, no backticks, no commentary).
- Must match EXACTLY this structure:
{{
  "assets": [
    {assets_schema_example}
  ]
}}
- Keep field names EXACTLY as shown.
- For each "prompts" list: include variations 1..{count_per_type}.
- Do not add extra top-level keys. Do not remove keys.
""".strip()

    return prompt



# -------------------------------------------------
# RUN SERVER
# -------------------------------------------------
if __name__ == "__main__":
    mcp.run(
        transport="sse",
    )
