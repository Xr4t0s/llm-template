"""
MCP Documentation Server - Refactored
Orchestrates complete project creation for decentralized applications

Tools:
1. generate_lore - Project narrative and identity
2. generate_documentation - 5 markdown files for GitBook
3. generate_tweets - Social media content for X/Twitter
4. generate_logo - Design brief for logo
5. generate_banner - Design brief for banner
6. generate_x_assets - Design briefs for all X/Twitter assets
7. generate_website - Production-ready HTML landing page
8. generate_complete_package - All-in-one orchestration
"""

from mcp.server.fastmcp import FastMCP
from typing import Optional, List

# -------------------------------------------------
# MCP SERVER INITIALIZATION
# -------------------------------------------------
mcp = FastMCP("documentation-server-v2")

# -------------------------------------------------
# TOOL 1: GENERATE LORE
# -------------------------------------------------
@mcp.tool()
def generate_lore(
    project_name: str,
    project_type: str,
    goal: str,
    tone: str = "professional",
    has_mascot: bool = False,
    user_input: str = ""
) -> str:
    """
    Generate unified project identity and narrative.
    
    Creates the foundation for all marketing and documentation content.
    
    Args:
        project_name: Name of the project
        project_type: Type (defi, nft, dao, token, gaming, utility, etc.)
        goal: Primary objective of the project
        tone: Narrative tone (professional, playful, meme, serious, edgy)
        has_mascot: Whether to create a mascot character
        user_input: Additional context or custom ideas
    
    Returns:
        Prompt to send to LLM for lore generation
    """

    mascot_section = """
### MASCOT CHARACTER
- Name and personality
- Visual description
- Role in the narrative
- Catchphrase or signature move
""" if has_mascot else ""

    prompt = f"""
You are a brand strategist for Web3 projects.

# PROJECT BRIEF
- Name: {project_name}
- Type: {project_type}
- Goal: {goal}
- Tone: {tone}
- Has Mascot: {"Yes" if has_mascot else "No"}

# USER INPUT
{user_input if user_input else "Standard Web3 project branding"}

---

# TASK
Create a unified, consistent project lore (400-600 words) that serves as the foundation for ALL future content.

## OUTPUT STRUCTURE

### 1. CORE IDENTITY
What is {project_name} in the simplest terms? (2-3 sentences)

### 2. ORIGIN STORY
How did {project_name} come to be? (1 paragraph, memorable)

### 3. VISION & MISSION
- What we're building
- Why it matters
- Who benefits

### 4. CORE VALUES
3-4 guiding principles

### 5. TARGET AUDIENCE
Who is this for? (specific)

### 6. UNIQUE SELLING PROPOSITION
What makes {project_name} different?

{mascot_section}

### 7. TONE OF VOICE
- How we communicate
- Words we use
- Words we avoid
- Example phrases

### 8. KEY MESSAGING PILLARS
3-5 main themes to emphasize

---

# REQUIREMENTS
- Total: 400-600 words
- Be specific and memorable
- Ensure internal consistency
- Make it distinctive and ownable
- Align with {tone} tone

Generate the lore now. Output ONLY the lore content, nothing else.
"""

    return prompt


# -------------------------------------------------
# TOOL 2: GENERATE DOCUMENTATION
# -------------------------------------------------
@mcp.tool()
def generate_documentation(
    project_name: str,
    lore: str,
    tone: str,
    project_type: str,
    goal: str
) -> str:
    """
    Generate 5 complete markdown documentation files for GitBook.
    
    Creates production-ready docs: Introduction, Vision, Roadmap, Tokenomics, FAQ.
    
    Args:
        project_name: Project name
        lore: Project narrative (from generate_lore)
        tone: Writing tone
        project_type: Type of project
        goal: Primary goal
    
    Returns:
        Prompt for LLM to generate JSON array of documentation files
    """

    prompt = f"""
You are a technical documentation writer for Web3 projects.

# PROJECT CONTEXT
- Name: {project_name}
- Type: {project_type}
- Goal: {goal}
- Tone: {tone}

# PROJECT LORE
{lore}

---

# TASK
Generate EXACTLY 5 complete, production-ready markdown files for GitBook.

Each file: 800-1500 words, proper markdown structure, NO placeholders, NO TODOs.

## FILES TO GENERATE

1. **01_introduction.md**
   - What is {project_name}
   - Key features (3-5 bullet points)
   - Why it matters
   - Quick start overview

2. **02_vision.md**
   - Vision statement
   - Core philosophy
   - Long-term mission
   - Community values
   - What makes it unique

3. **03_roadmap.md**
   - Project phases/timeline
   - Key milestones
   - Short-term and long-term goals
   - Future expansion plans

4. **04_tokenomics.md**
   {"- Full tokenomics breakdown" if project_type in ["defi", "token", "dao"] else "- Project utility and economic model"}
   - Distribution (if applicable)
   - Utility/incentives
   - Supply or participation logic

5. **05_faq.md**
   - 10-15 frequently asked questions
   - Clear, concise answers
   - Cover basics, technical aspects, community, roadmap

---

# OUTPUT FORMAT (MANDATORY JSON ARRAY)

You MUST output ONLY a valid JSON array. No explanations, no text outside JSON.

[
  {{
    "filename": "01_introduction.md",
    "content": "<full markdown content>"
  }},
  {{
    "filename": "02_vision.md",
    "content": "<full markdown content>"
  }},
  {{
    "filename": "03_roadmap.md",
    "content": "<full markdown content>"
  }},
  {{
    "filename": "04_tokenomics.md",
    "content": "<full markdown content>"
  }},
  {{
    "filename": "05_faq.md",
    "content": "<full markdown content>"
  }}
]

# CONTENT REQUIREMENTS
- 800-1500 words per file
- Proper markdown: titles, subtitles, lists
- Emojis in titles (more if tone is "meme" or "playful")
- Be specific, concrete, actionable
- Consistent {tone} tone throughout

Generate the JSON array now.
"""

    return prompt


# -------------------------------------------------
# TOOL 3: GENERATE TWEETS
# -------------------------------------------------
@mcp.tool()
def generate_tweets(
    project_name: str,
    lore: str,
    tone: str,
    count: int = 20,
    include_threads: bool = True
) -> str:
    """
    Generate Twitter/X-optimized posts and content.
    
    Creates ready-to-post tweets with hooks, hashtags, and engagement tactics.
    
    Args:
        project_name: Project name
        lore: Project narrative (from generate_lore)
        tone: Tweet tone (matches project tone)
        count: Number of tweets (10-30)
        include_threads: Whether to include thread prompts
    
    Returns:
        Prompt for LLM to generate tweets
    """

    threads_section = """
## BONUS: 3 TWEET THREADS
For each thread, provide:
- Thread hook (engaging first tweet)
- 4-5 tweets in sequence
- Each tweet < 280 characters
- Clear value/narrative arc
- CTA at the end

Example format:
THREAD 1: [Topic]
Tweet 1: [Hook]
Tweet 2: [Development]
Tweet 3: [More context]
Tweet 4: [Key insight]
Tweet 5: [CTA]
""" if include_threads else ""

    prompt = f"""
You are a social media expert specializing in Web3 Twitter growth.

# PROJECT CONTEXT
- Name: {project_name}
- Tone: {tone}

# PROJECT LORE
{lore}

---

# TASK
Generate {count} ready-to-post Twitter/X posts.

## DISTRIBUTION
- 40% engagement/community posts
- 30% educational/informative posts
- 20% announcement/update posts
- 10% meme/fun posts (if tone allows)

## FORMAT FOR EACH POST

POST #{"{"}N{"}"}
Type: [Engagement/Educational/Announcement/Meme]
---
[Tweet content - max 280 characters]
[2-3 relevant hashtags]
---

## REQUIREMENTS PER TWEET
- Max 280 characters
- Strong hook in first line
- Clear value or entertainment
- 2-3 hashtags maximum
- Include emojis strategically
- Mix educational + entertaining
- Some time-sensitive, some evergreen
- Include CTAs where appropriate
- Use active voice
- Ask questions to drive replies

## TWITTER BEST PRACTICES
- Lead with curiosity or value
- Numbers increase engagement
- Questions drive comments
- Use line breaks for readability
- Reference {tone} tone consistently
- Make threads shareable

{threads_section}

Generate the {count} tweets now. Output ONLY the tweets, no explanations.
"""

    return prompt


# -------------------------------------------------
# TOOL 4: GENERATE LOGO
# -------------------------------------------------
@mcp.tool()
def generate_logo(
    project_name: str,
    lore: str,
    tone: str,
    visual_vibe: str = "modern",
    color_palette: List[str] = ["indigo", "lime"],
    style_guide: str = ""
) -> str:
    """
    Generate detailed logo design brief.
    
    Creates specifications for a designer or AI image generator.
    
    Args:
        project_name: Project name
        lore: Project narrative
        tone: Brand tone
        visual_vibe: Visual aesthetic (modern, minimal, bold, retro, cyberpunk)
        color_palette: Primary and secondary colors
        style_guide: Additional design guidelines
    
    Returns:
        Prompt for LLM to generate logo brief
    """

    colors = " + ".join(color_palette)

    prompt = f"""
You are a professional brand designer specializing in Web3 projects.

# PROJECT CONTEXT
- Name: {project_name}
- Tone: {tone}
- Visual Vibe: {visual_vibe}
- Colors: {colors}

# PROJECT LORE
{lore}

---

# TASK
Create a detailed logo design brief (500-700 words) for a designer or AI tool.

## SECTIONS

### 1. PURPOSE & CONTEXT
Where will this logo be used? (favicon, social avatars, documentation)

### 2. DESIGN BRIEF
Detailed visual description for a designer or AI tool like Midjourney/DALL-E

### 3. TECHNICAL SPECIFICATIONS
- Primary size: 1000x1000px
- Icon-only version: needs to work at 16x16px to 1000x1000px
- Favicon: 512x512px
- App Icon: 1024x1024px
- Formats: PNG, SVG, JPG

### 4. COLOR & STYLE
- Primary colors: {colors}
- Must work in single-color (B&W)
- Must work in full color
- No gradients (keep it clean)
- Modern, distinctive, memorable

### 5. KEY REQUIREMENTS
- Instantly recognizable
- Scalable to any size
- Reflects {tone} tone
- Aligns with {visual_vibe} aesthetic
- Unique and ownable
- Professional yet approachable

### 6. VARIATIONS NEEDED
- Full logo with text
- Icon-only version
- Black version (for dark backgrounds)
- White version (for light backgrounds)
- Single-color version

### 7. MOOD & FEEL
The emotional tone this logo should convey

### 8. DON'T INCLUDE
- Clichés
- Generic Web3 symbols
- Overused gradients
- Too many elements

### 9. AI GENERATION PROMPT
A detailed Midjourney/DALL-E prompt for designers using AI

---

# OUTPUT FORMAT

Structure your response with clear sections:

## LOGO DESIGN BRIEF: {project_name}

### Purpose & Context
[Details]

### Design Brief
[Visual description]

### Technical Specifications
[Sizes and formats]

### Color & Style Requirements
[Specific colors and styling]

### Key Requirements
[Must-haves]

### Variations Needed
[List]

### Mood & Feel
[Emotional tone]

### Elements to Avoid
[Don'ts]

### AI Prompt (for Midjourney/DALL-E)
[Detailed prompt]

---

# ADDITIONAL GUIDELINES
{style_guide if style_guide else "Follow the visual vibe and tone specified above"}

Generate the logo brief now. Output ONLY the brief content.
"""

    return prompt


# -------------------------------------------------
# TOOL 5: GENERATE BANNER
# -------------------------------------------------
@mcp.tool()
def generate_banner(
    project_name: str,
    lore: str,
    tone: str,
    visual_vibe: str = "modern",
    color_palette: List[str] = ["indigo", "lime"],
    tagline: str = "",
    style_guide: str = ""
) -> str:
    """
    Generate detailed banner design brief for social media headers.
    
    Creates specifications for Twitter, Telegram, Discord banners.
    
    Args:
        project_name: Project name
        lore: Project narrative
        tone: Brand tone
        visual_vibe: Visual aesthetic
        color_palette: Primary and secondary colors
        tagline: Project tagline (optional)
        style_guide: Additional design guidelines
    
    Returns:
        Prompt for LLM to generate banner brief
    """

    colors = " + ".join(color_palette)

    prompt = f"""
You are a professional brand designer specializing in Web3 social media assets.

# PROJECT CONTEXT
- Name: {project_name}
- Tone: {tone}
- Visual Vibe: {visual_vibe}
- Colors: {colors}
- Tagline: {tagline if tagline else "Create an appropriate tagline"}

# PROJECT LORE
{lore}

---

# TASK
Create a detailed banner design brief (400-600 words) for a designer or AI tool.

## SECTIONS

### 1. PURPOSE & CONTEXT
Used as header banner for:
- Twitter profile (1500x500px)
- Telegram channel (1590x400px)
- Discord server (960x540px)
- Website header

### 2. DESIGN BRIEF
Detailed visual description capturing the essence of {project_name}

### 3. TECHNICAL SPECIFICATIONS
- Twitter: 1500x500px
- Telegram: 1590x400px
- Discord: 960x540px (minimum 320x180px)
- Format: PNG or JPG
- Resolution: 72-300 DPI

### 4. COLOR & STYLE
- Primary colors: {colors}
- Gradient direction and intensity
- Effects: glow, shadow, blur
- Typography: bold, modern, readable

### 5. KEY ELEMENTS
- Project name (large, readable)
- Tagline or key message (optional)
- Visual elements representing the project
- Logo placement (top corner)
- Safe zones for text overlays

### 6. MOOD & FEEL
- Dynamic and energetic
- Premium yet approachable
- Should feel current and professional
- Reflects {tone} tone

### 7. COMPOSITION
- Hero visual that captures essence
- Eye-catching and shareable
- Balanced composition
- Clear focal point

### 8. DON'T INCLUDE
- Overly busy backgrounds
- Too many competing elements
- Generic stock photos
- Outdated designs

### 9. AI GENERATION PROMPT
Detailed Midjourney/DALL-E prompt for designers using AI

---

# OUTPUT FORMAT

Structure clearly:

## BANNER DESIGN BRIEF: {project_name}

### Purpose & Context
[Details]

### Design Brief
[Visual description]

### Technical Specifications
[Sizes and formats]

### Color & Style
[Colors, gradients, effects]

### Key Elements
[What must be included]

### Mood & Feel
[Emotional tone]

### Composition Tips
[Layout guidance]

### Elements to Avoid
[Don'ts]

### AI Prompt (Midjourney/DALL-E)
[Detailed prompt]

---

# ADDITIONAL GUIDELINES
{style_guide if style_guide else "Follow the visual vibe and tone specified above"}

Generate the banner brief now. Output ONLY the brief content.
"""

    return prompt


# -------------------------------------------------
# TOOL 6: GENERATE X ASSETS
# -------------------------------------------------
@mcp.tool()
def generate_x_assets(
    project_name: str,
    lore: str,
    tone: str,
    visual_vibe: str = "modern",
    color_palette: List[str] = ["indigo", "lime"],
    include_assets: List[str] = ["pfp", "header", "meme", "buybot", "dexscreener"],
    style_guide: str = ""
) -> str:
    """
    Generate all X/Twitter visual asset design briefs.
    
    Creates detailed specifications for: PFP, Header, Meme, BuyBot, DEXScreener.
    
    Args:
        project_name: Project name
        lore: Project narrative
        tone: Brand tone
        visual_vibe: Visual aesthetic
        color_palette: Primary and secondary colors
        include_assets: Which assets to generate (all by default)
        style_guide: Additional design guidelines
    
    Returns:
        Prompt for LLM to generate asset briefs in JSON format
    """

    colors = " + ".join(color_palette)
    
    assets_list = "\n".join([f"- {a.upper()}" for a in include_assets])

    prompt = f"""
You are a creative art director for Web3 projects specializing in X/Twitter assets.

# PROJECT CONTEXT
- Name: {project_name}
- Tone: {tone}
- Visual Vibe: {visual_vibe}
- Colors: {colors}

# PROJECT LORE
{lore}

---

# TASK
Create detailed design briefs for ALL X/Twitter visual assets.

## ASSETS TO CREATE
{assets_list}

---

# ASSET SPECIFICATIONS

### 1. PFP (PROFILE PICTURE)
**Dimensions**: 400x400px (displayed at 48x48px, 200x200px, 400x400px)
**Purpose**: Main profile avatar
**Requirements**:
- Simple and recognizable at small sizes
- Works as a square
- High contrast
- Memorable and distinctive
- Reflects brand identity

### 2. HEADER (BANNER)
**Dimensions**: 1500x500px
**Purpose**: Twitter profile header
**Requirements**:
- Eye-catching and shareable
- Includes project name/tagline
- Space for logo (safe zone)
- Dynamic composition
- Reflects {tone} tone

### 3. MEME
**Dimensions**: 1080x1080px (square)
**Purpose**: Viral engagement and community entertainment
**Requirements**:
- Funny, relatable, shareable
- Resonates with Web3/crypto audience
- Subtle {project_name} branding
- High engagement potential
- Can be time-sensitive or evergreen

### 4. BUYBOT IMAGE
**Dimensions**: 1200x800px (landscape)
**Purpose**: Market the bot functionality and automation
**Requirements**:
- Showcase speed, ease, security
- Modern and professional
- Can include interface mockups
- Inspire confidence and excitement
- Clear value proposition

### 5. DEXSCREENER IMAGE
**Dimensions**: 1200x600px
**Purpose**: DEX Screener listing thumbnail
**Requirements**:
- Professional and trustworthy
- Data-focused aesthetic
- Can include chart visualization
- Positive visual cues
- Conveys legitimacy and growth

---

# OUTPUT FORMAT (MANDATORY JSON)

Return ONLY a valid JSON array. No explanations, no text outside JSON.

[
  {{
    "asset": "PFP",
    "brief": "<detailed brief for PFP>"
  }},
  {{
    "asset": "HEADER",
    "brief": "<detailed brief for Header>"
  }},
  {{
    "asset": "MEME",
    "brief": "<detailed brief for Meme>"
  }},
  {{
    "asset": "BUYBOT",
    "brief": "<detailed brief for BuyBot>"
  }},
  {{
    "asset": "DEXSCREENER",
    "brief": "<detailed brief for DEXScreener>"
  }}
]

---

# PER-ASSET BRIEF STRUCTURE

For each asset, include:

**Purpose & Context**: Where/how this will be used
**Design Brief**: Detailed visual description
**Dimensions**: Exact size requirements
**Color & Style**: Specific colors, effects
**Key Elements**: What must be included
**Mood & Feel**: Emotional tone
**Don'ts**: What to avoid
**AI Prompt**: Detailed prompt for Midjourney/DALL-E

---

# GENERAL REQUIREMENTS
- Be specific and concrete
- All assets should be cohesive but unique
- Consider practical use cases
- Make briefs actionable for AI and human designers
- Ensure brand consistency
- Use hex color codes where possible

# ADDITIONAL GUIDELINES
{style_guide if style_guide else "Follow the visual vibe and tone specified above"}

Generate the X assets briefs now. Output ONLY the JSON array.
"""

    return prompt


# -------------------------------------------------
# TOOL 7: GENERATE WEBSITE
# -------------------------------------------------
@mcp.tool()
def generate_website(
    project_name: str,
    lore: str,
    tone: str,
    goal: str = "convert",
    primary_cta: str = "Get Started",
    secondary_cta: str = "Learn More",
    color_palette: List[str] = ["indigo", "lime"],
    include_seo: bool = True,
    include_faq: bool = True,
    faq_count: int = 6
) -> str:
    """
    Generate production-ready HTML landing page.
    
    Single-file HTML with embedded CSS, ready to upload to any host.
    
    Args:
        project_name: Project name
        lore: Project narrative
        tone: Brand tone
        goal: Page objective (convert, whitelist, waitlist, mint, presale)
        primary_cta: Main button text
        secondary_cta: Secondary button text
        color_palette: Color scheme
        include_seo: Include SEO meta tags
        include_faq: Include FAQ section
        faq_count: Number of FAQs
    
    Returns:
        Prompt for LLM to generate complete HTML file
    """

    colors = " + ".join(color_palette)
    hex_colors = {
        "indigo": "#4F46E5",
        "lime": "#84CC16",
        "blue": "#3B82F6",
        "purple": "#A855F7",
        "pink": "#EC4899"
    }
    
    primary_color = hex_colors.get(color_palette[0].lower(), "#4F46E5")
    secondary_color = hex_colors.get(color_palette[1].lower(), "#84CC16")

    seo_section = """
- Complete meta tags (title, description, keywords)
- Open Graph tags (social sharing)
- Twitter Card tags
- Structured data (JSON-LD)
- Proper heading hierarchy (H1, H2, H3)
- Alt text for all images
""" if include_seo else "- Basic meta tags"

    faq_section = f"""
## FAQ SECTION
- {faq_count} frequently asked questions
- Accordion-style layout (expandable)
- Questions: "Is it safe?", "How do I start?", "What makes you different?", etc.
- Simple JavaScript for toggle functionality
""" if include_faq else ""

    prompt = f"""
You are a senior Web3 frontend developer and conversion expert.

# PROJECT CONTEXT
- Name: {project_name}
- Tone: {tone}
- Goal: {goal}
- Primary CTA: {primary_cta}
- Secondary CTA: {secondary_cta}
- Colors: {colors}

# PROJECT LORE
{lore}

---

# TASK
Generate a COMPLETE, PRODUCTION-READY HTML landing page.

Single file, all CSS embedded, ready to upload to Hostinger or any web host.

## TECHNICAL REQUIREMENTS
- Single HTML file (no external files)
- Fully responsive (mobile-first)
- No external dependencies (no Bootstrap)
- Cross-browser compatible
- Fast loading
- Semantic HTML5
- Accessible (ARIA labels)

## DESIGN REQUIREMENTS
- Modern Web3 aesthetic
- Colors: {colors}
- Primary: {primary_color}
- Secondary: {secondary_color}
- Smooth scrolling and animations
- Hover effects on interactive elements
- Mobile hamburger menu
- Professional typography (Google Fonts via CDN)
- Card-based layouts
- Proper spacing and white space

## COPYWRITING REQUIREMENTS
- Strong hook (first line hits hard)
- Speak benefits, not just features
- Short sentences, minimal fluff
- Tone: {tone}
- Include trust signals
- Make it skimmable (headings, bullets, blocks)

## CTA REQUIREMENTS
- Primary text: "{primary_cta}"
- Secondary text: "{secondary_cta}"
- CTAs appear: hero + middle + final section
- Prominent, contrasting colors

## SEO REQUIREMENTS
{seo_section}

{faq_section}

## SECTIONS TO INCLUDE
1. Navigation bar (sticky)
2. Hero section (hook + CTAs)
3. Problem statement
4. Solution/unique value
5. Features (3-5 feature cards)
6. How it works (3 steps max)
7. Social proof / stats
{f"8. FAQ (accordion style)" if include_faq else "8. Testimonials"}
9. Final CTA section
10. Footer (links, socials, legal)

---

# OUTPUT FORMAT

Return ONLY complete HTML code. No markdown, no explanations.

MUST start with: <!DOCTYPE html>
MUST end with: </html>

Structure:
- <!DOCTYPE html>
- <head> with meta tags, title, Google Fonts link, embedded CSS in <style>
- <body> with navbar, all sections, footer
- Embedded JavaScript for: mobile menu, FAQ accordion, smooth scroll

---

# IMPORTANT NOTES
- NO markdown formatting (not ```html)
- NO external stylesheets or scripts
- NO placeholder links (use # for now)
- Use https://via.placeholder.com/ for images
- Add HTML comments marking each section
- Proper indentation for readability
- Ready to save as index.html immediately

Generate the complete HTML file now.
"""

    return prompt


# -------------------------------------------------
# TOOL 8: GENERATE COMPLETE PACKAGE (BONUS)
# -------------------------------------------------
@mcp.tool()
def generate_complete_package(
    project_name: str,
    project_type: str,
    goal: str,
    tone: str = "professional",
    has_mascot: bool = False,
    user_input: str = "",
    color_palette: List[str] = ["indigo", "lime"]
) -> str:
    """
    Orchestrate ALL tools in sequence (optional convenience function).
    
    Generates: Lore → Documentation → Tweets → Logo → Banner → X Assets → Website
    
    This tool returns instructions for using all other tools in order.
    
    Args:
        project_name: Project name
        project_type: Project type
        goal: Primary goal
        tone: Brand tone
        has_mascot: Include mascot
        user_input: Additional context
        color_palette: Color scheme
    
    Returns:
        Orchestration guide for using all tools in order
    """

    colors = " + ".join(color_palette)

    orchestration_guide = f"""
# COMPLETE PACKAGE ORCHESTRATION GUIDE

## Project: {project_name}
- Type: {project_type}
- Goal: {goal}
- Tone: {tone}
- Colors: {colors}
- Mascot: {"Yes" if has_mascot else "No"}

---

## STEP 1: GENERATE LORE (Foundation)
Use: generate_lore()
- project_name: "{project_name}"
- project_type: "{project_type}"
- goal: "{goal}"
- tone: "{tone}"
- has_mascot: {has_mascot}
- user_input: "{user_input}"

**Output**: Project narrative (save this as `lore.txt`)

---

## STEP 2: GENERATE DOCUMENTATION
Use: generate_documentation()
- project_name: "{project_name}"
- lore: [output from Step 1]
- tone: "{tone}"
- project_type: "{project_type}"
- goal: "{goal}"

**Output**: JSON array of 5 markdown files
**Save**: Create /docs/step1/ directory with these files:
- 01_introduction.md
- 02_vision.md
- 03_roadmap.md
- 04_tokenomics.md
- 05_faq.md

---

## STEP 3: GENERATE TWEETS
Use: generate_tweets()
- project_name: "{project_name}"
- lore: [output from Step 1]
- tone: "{tone}"
- count: 20
- include_threads: True

**Output**: 20 ready-to-post tweets + 3 thread ideas
**Save**: Create `tweets.txt` or tweet scheduler document

---

## STEP 4: GENERATE LOGO
Use: generate_logo()
- project_name: "{project_name}"
- lore: [output from Step 1]
- tone: "{tone}"
- visual_vibe: "modern"
- color_palette: {color_palette}

**Output**: Logo design brief
**Save**: Create `logo_brief.md`
**Next**: Share with designer or use Midjourney prompt

---

## STEP 5: GENERATE BANNER
Use: generate_banner()
- project_name: "{project_name}"
- lore: [output from Step 1]
- tone: "{tone}"
- visual_vibe: "modern"
- color_palette: {color_palette}

**Output**: Banner design brief
**Save**: Create `banner_brief.md`
**Next**: Share with designer or use AI image generator

---

## STEP 6: GENERATE X ASSETS
Use: generate_x_assets()
- project_name: "{project_name}"
- lore: [output from Step 1]
- tone: "{tone}"
- visual_vibe: "modern"
- color_palette: {color_palette}
- include_assets: ["pfp", "header", "meme", "buybot", "dexscreener"]

**Output**: JSON array of 5 asset design briefs
**Save**: Create `x_assets.json` or individual brief files
**Next**: Share briefs with designer or use AI tools

---

## STEP 7: GENERATE WEBSITE
Use: generate_website()
- project_name: "{project_name}"
- lore: [output from Step 1]
- tone: "{tone}"
- goal: "{goal}"
- primary_cta: "Get Started"
- secondary_cta: "Learn More"
- color_palette: {color_palette}
- include_seo: True
- include_faq: True

**Output**: Complete HTML landing page
**Save**: Create `index.html`
**Deploy**: Upload to Hostinger or any web host

---

## FINAL CHECKLIST

After completing all steps, you should have:

✅ Lore (brand narrative)
✅ Documentation (5 markdown files)
✅ Social content (20 tweets + 3 threads)
✅ Logo brief (ready for designer/AI)
✅ Banner brief (ready for designer/AI)
✅ X assets briefs (5 assets, ready for designer/AI)
✅ Website (production-ready HTML)

## FILE STRUCTURE
```
project-{project_name}/
├── docs/
│   ├── 01_introduction.md
│   ├── 02_vision.md
│   ├── 03_roadmap.md
│   ├── 04_tokenomics.md
│   └── 05_faq.md
├── design-briefs/
│   ├── logo_brief.md
│   ├── banner_brief.md
│   └── x_assets.json
├── content/
│   └── tweets.txt
├── website/
│   └── index.html
└── lore.txt
```

---

## NEXT STEPS

1. **Share design briefs** with designer or use AI image generators
2. **Customize website** with actual links and contact forms
3. **Schedule tweets** using Twitter scheduler or Buffer
4. **Deploy website** to Hostinger, Vercel, or Netlify
5. **Implement** documentation in GitBook or Docs
6. **Monitor engagement** and iterate based on feedback

---

Good luck with {project_name}! 🚀
"""

    return orchestration_guide


# -------------------------------------------------
# RUN SERVER
# -------------------------------------------------
if __name__ == "__main__":
    mcp.run(
        transport="sse",
    )