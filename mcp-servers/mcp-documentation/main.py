"""
MCP Documentation Server
Orchestrates documentation generation for decentralized applications

Tools:
1. generate_documentation - Creates 5 markdown files for GitBook
2. generate_lore - Assembles project identity into consistent narrative
3. generate_social_content - Creates 10-20 social media posts
4. generate_visuals - Creates design briefs for Logo, Banner, Meme, BuyBot, DEXScreener
5. generate_landing_page - Creates production-ready HTML landing page
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
# TOOL 4: GENERATE VISUALS
# -------------------------------------------------
@mcp.tool()
def generate_visuals(
    project_name: str,
    lore: str,
    tone: str,
    visual_vibe: str = "bold",
    color_palette: List[str] = ["indigo", "lime"],
    mascot_description: str = "",
    visuals_to_generate: List[str] = ["logo", "banner", "meme", "buybot_image", "dexscreener_image"],
    style_guide: str = ""
) -> str:
    """
    Generate visual design prompts and specifications for Web3 project assets.

    Creates detailed briefs for each visual asset that can be used with
    image generation AI or handed to a designer.

    Args:
        project_name: Name of the project
        lore: Project narrative and identity
        tone: Brand tone (serious, playful, meme, professional)
        visual_vibe: Visual aesthetic (bold, minimal, retro, futuristic, neon, cyberpunk)
        color_palette: Primary and secondary colors
        mascot_description: Description of mascot (if applicable)
        visuals_to_generate: List of visuals needed
        style_guide: Additional style guidelines
    """

    visual_specs = {
        "logo": "Primary logo for all branding purposes",
        "banner": "Social media banner for Twitter/Telegram headers",
        "meme": "Shareable meme image that resonates with Web3 community",
        "buybot_image": "Image showcasing the buy/trade bot functionality",
        "dexscreener_image": "Professional chart/graph image for DEX Screener listing"
    }

    visuals_guidelines = "\n".join([
        f"- **{v.upper()}**: {visual_specs.get(v, 'Custom visual')}"
        for v in visuals_to_generate
    ])

    color_scheme = " + ".join(color_palette)
    mascot_info = f"\n**Mascot Reference**: {mascot_description}" if mascot_description else ""

    prompt = f"""
You are a creative art director and visual designer specializing in Web3 and crypto projects.

Your mission: create detailed, actionable visual briefs for all assets needed by {project_name}.

# PROJECT CONTEXT
**Name**: {project_name}
**Tone**: {tone}
**Visual Vibe**: {visual_vibe}
**Color Palette**: {color_scheme}
{mascot_info}

# PROJECT LORE (BRAND IDENTITY)
{lore}

# ADDITIONAL STYLE GUIDELINES
{style_guide if style_guide else "No additional guidelines provided"}

---

# YOUR TASK
Generate detailed visual design briefs for the following assets:

{visuals_guidelines}

For EACH visual, provide:
1. **Purpose & Context**: What is this visual for and where will it be used?
2. **Design Brief**: Detailed description for a designer or AI image generator
3. **Dimensions & Specs**: Exact sizing requirements
4. **Color & Style**: Specific color usage, gradients, effects
5. **Key Elements**: What must be included
6. **Mood & Feel**: Emotional tone and energy
7. **Don'ts**: What to avoid
8. **AI Prompt**: A detailed prompt for Midjourney, DALL-E, or similar tools (if applicable)

---

# VISUAL SPECIFICATIONS

## 1. LOGO
**Purpose**: Primary brand mark, favicon, social avatars
**Dimensions**: 
- Primary: 1000x1000px (square)
- Favicon: 512x512px
- App Icon: 1024x1024px

**Design Brief**:
- Must work at all sizes (from 16x16px to 1000x1000px)
- Should be memorable and distinctive
- Must work in single-color (black/white) and full color
- Should reflect the {tone} tone and {visual_vibe} aesthetic
- Primary colors: {color_scheme}
- Consider simplicity for favicon/small sizes
- Must be instantly recognizable

**Variations Needed**:
- Full logo with text
- Icon-only version
- Inverted/dark version
- Favicon format

---

## 2. BANNER
**Purpose**: Twitter/Telegram header, Discord server banner, website header
**Dimensions**: 
- Twitter: 1500x500px
- Telegram: 1590x400px
- Discord: 960x540px (min: 320x180px)

**Design Brief**:
- Hero visual that captures the essence of {project_name}
- Must include project name prominently
- Can include tagline/key message
- Should be eye-catching and shareable
- Use {color_scheme} color palette
- Reflect {visual_vibe} aesthetic
- Leave safe zones for text overlays
- Should work with logo placement in top corner

**Key Elements**:
- Project name (large, readable)
- Optional: tagline or key message
- Visual elements that represent the project
- Should feel premium yet approachable
- Dynamic composition, not static

---

## 3. MEME
**Purpose**: Community engagement, viral social media posts, entertainment
**Dimensions**: 
- Instagram Square: 1080x1080px
- Twitter: 1024x512px
- General: 1080x1080px (square format recommended)

**Design Brief**:
- Funny, relatable, shareable content
- Should resonate with Web3/crypto audience
- Can be humorous, irreverent, or clever
- Must feature the {project_name} branding subtly
- Use {tone} tone in visual style
- Include text overlay (meme caption style)
- Should encourage shares and comments
- Can reference crypto culture, market trends, or community inside jokes

**Mood**:
- Entertaining and shareable
- Relatable to crypto/Web3 community
- Subtle branding (not too pushy)
- High engagement potential

---

## 4. BUYBOT IMAGE
**Purpose**: Marketing the bot's functionality, app store listing, social posts
**Dimensions**: 
- Primary: 1200x800px
- Instagram Story: 1080x1920px
- Thumbnail: 1280x720px

**Design Brief**:
- Showcase ease of use and speed of the buybot
- Should convey: automation, speed, security, simplicity
- Can include interface mockups or visual metaphors
- Use {color_scheme} with high contrast for clarity
- Modern, sleek design aesthetic
- Should inspire confidence and excitement
- Consider showing: charts, upward trends, quick actions, security features

**Key Elements**:
- Visual representation of the bot in action
- User-friendly interface (real or conceptual)
- Speed/efficiency indicators
- Trust/security signals
- Clear indication of ease of use
- {project_name} branding

**Visual Style**:
- {visual_vibe} aesthetic
- Modern, professional
- High-contrast, easy to read
- Dynamic, energetic feel
- Should not look technical/intimidating

---

## 5. DEXSCREENER IMAGE
**Purpose**: DEX Screener listing thumbnail, social proof, marketing material
**Dimensions**: 
- DEX Screener: 1200x600px
- Trading interface: 1000x500px
- Social post: 1200x628px

**Design Brief**:
- Professional, data-focused visual
- Should convey: legitimacy, trading potential, community strength
- Can include: chart elements, price action visualization, community metrics
- Use {color_scheme} with green/red chart colors (standard for trading)
- Clean, professional design
- Should not look like a scam or low-effort project
- Can feature: logo, project name, key metrics

**Key Elements**:
- Project logo or name prominently
- Chart/graph visualization (can be stylized, not necessarily realistic)
- Positive visual cues (uptrends, growth indicators)
- Professional color scheme
- Trust signals (verified, community, volume)

**Visual Style**:
- Professional and trustworthy
- Data-driven aesthetic
- Clean lines and typography
- Premium feel
- Finance-focused aesthetic

---

# TONE & STYLE GUIDANCE
Across ALL visuals:
- **Tone**: {tone}
- **Aesthetic**: {visual_vibe}
- **Colors**: {color_scheme}
- **Feel**: {("Playful, fun, engaging" if tone == "playful" else "Professional, serious, credible" if tone == "serious" else "Bold, edgy, community-focused")}

---

# OUTPUT FORMAT

For each visual, structure your response as:

```
═══════════════════════════════════════════════════════
VISUAL: [NAME]
═══════════════════════════════════════════════════════

PURPOSE & CONTEXT
[Details about where and how this visual will be used]

DIMENSIONS & TECHNICAL SPECS
- Primary: [size]
- Variations: [other sizes needed]
- Format: PNG/SVG/JPG
- Resolution: [DPI if needed]

DESIGN BRIEF
[Detailed visual description for designer or AI tool]

COLOR & STYLE REQUIREMENTS
- Primary colors: [colors]
- Secondary colors: [colors]
- Gradients: [if applicable]
- Effects: [if applicable]
- Typography: [font style recommendations]

KEY ELEMENTS TO INCLUDE
- Element 1
- Element 2
- Element 3
[...]

MOOD & FEEL
[Emotional tone and energy level]

DON'T INCLUDE
- [Things to avoid]
- [Bad practices]
- [Common mistakes]

AI GENERATION PROMPT
[A detailed, specific prompt for Midjourney, DALL-E, or similar]
Example: "A sleek, modern logo of a [description]..."

DESIGNER NOTES
[Additional context or flexibility notes]

═══════════════════════════════════════════════════════
```

---

# FINAL REQUIREMENTS
- Be specific and concrete (avoid vague descriptions)
- Each visual should be unique but cohesive
- Think about how visuals will look together as a brand system
- Consider practical use cases (how will these be deployed?)
- Make briefs actionable for both AI tools AND human designers
- Ensure brand consistency across all visuals
- Use realistic hex color codes where possible
- Include technical specs for file formats

Generate the visual briefs for all requested assets now.
"""

    return prompt


# -------------------------------------------------
# TOOL 5: GENERATE LANDING PAGE
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
- No markdown like ```html, the file should ABSOLUTELY start by <!DOCTYPE html> and finish by </html>
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
# RUN SERVER
# -------------------------------------------------
if __name__ == "__main__":
    mcp.run(
        transport="sse",
    )