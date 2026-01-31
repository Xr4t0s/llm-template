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
# TOOL 5: GENERATE BANNER (WEB3 MINIMALIST)
# -------------------------------------------------

def generate_banner(
    project_name: str,
    lore: str,
    tone: str,
    visual_vibe: str = "modern",
    color_palette: list = None,
    tagline: str = "",
    style_guide: str = ""
) -> str:
    """
    Generate minimal banner design brief for Web3 projects.
    
    Philosophy: Typography + Color > Visual Noise
    
    Args:
        project_name: Project name
        lore: Project narrative
        tone: Brand tone
        visual_vibe: Visual aesthetic (minimal, geometric, gradient, dark, light)
        color_palette: [primary_color, secondary_color]
        tagline: Project tagline (required for impact)
        style_guide: Additional guidelines
    
    Returns:
        Banner design brief prompt
    """
    
    if color_palette is None:
        color_palette = ["#6366f1", "#00ff88"]
    
    primary_color = color_palette[0]
    secondary_color = color_palette[1] if len(color_palette) > 1 else primary_color
    
    if not tagline:
        tagline = "The project tagline that captures essence in 3-5 words"
    
    prompt = f"""You are a Web3 brand designer with zero tolerance for visual noise.

# BANNER PHILOSOPHY
**Less is more. Typography is the hero. Color creates mood. Subtlety wins.**

The banner doesn't explain the project—it feels like the project.

---

# PROJECT DNA
- **Name:** {project_name}
- **Tone:** {tone}
- **Aesthetic:** {visual_vibe}
- **Primary:** {primary_color}
- **Secondary:** {secondary_color}
- **Tagline:** "{tagline}"

# LORE
{lore}

---

# CORE CONSTRAINT: MINIMAL DESIGN

✓ Bold typography as primary element
✓ Intentional color play (primary + secondary interaction)
✓ Subtle background texture or gradient (not the focus)
✓ Strategic negative space
✓ Readable at ANY scale
✓ Works in dark mode AND light mode
✗ Stock imagery
✗ Photographic elements
✗ Decorative patterns
✗ Multiple visual elements competing
✗ Busy backgrounds
✗ Gradients that distract from text

---

# DESIGN BRIEF

## 1. LAYOUT HIERARCHY
**Tier 1 (Hero):** {project_name} (largest, boldest)
**Tier 2 (Impact):** "{tagline}" (supporting, elegant)
**Tier 3 (Balance):** Subtle background + color interplay

**Composition:** Asymmetrical balance. Text occupies 60-70% visual weight.

## 2. TYPOGRAPHY STRATEGY
- **Primary Font:** Modern, geometric sans-serif (Helvetica Neue, Inter, Montserrat Bold)
- **Project Name:** 
  - Size: Dominant, fills 40-50% of banner width
  - Weight: 700-900 (extra bold)
  - Color: {primary_color} OR white/black with {primary_color} accent
  - Tracking: -2 to 0 (tight, powerful)

- **Tagline:**
  - Size: 30-40% of name size
  - Weight: 400-500 (elegant, readable)
  - Color: {secondary_color} OR neutral (white/gray)
  - Line height: 1.3-1.4 (breathing room)

## 3. COLOR COMPOSITION
**Primary Color Strategy:**
- {primary_color} dominates: text, accents, or background
- Fills 60-70% of visual space
- Creates instant brand recognition

**Secondary Color Strategy:**
- {secondary_color} acts as rhythm
- Used for: tagline, accent lines, or subtle background elements
- Never fights for attention
- Creates depth without complexity

**Background:**
- Solid color (preferred) OR minimal gradient
- Gradient angle: Subtle (if used)
- Ensure 3:1 contrast ratio minimum for text readability

## 4. BACKGROUND OPTIONS (pick ONE)

### Option A: Solid Primary + Text Secondary
- Full background: {primary_color}
- Text: White/light with {secondary_color} accent word
- Simple. Bold. Unmistakable.

### Option B: Solid Secondary + Text Primary
- Full background: {secondary_color}
- Text: {primary_color} (strong contrast)
- Creates energy through color opposition

### Option C: Dark/Light Base + Color Accent
- Background: Black or white (depending on tone)
- Text: {primary_color} for project name
- Tagline: {secondary_color}
- Most minimal. Most professional.

### Option D: Subtle Gradient
- From primary to darker version
- Direction: Top-left to bottom-right OR top to bottom
- Gradient stop: 20-30% transition (subtle, not flashy)
- Preserves minimalist feel

## 5. ACCENT ELEMENTS (OPTIONAL, use sparingly)

**Allowed:**
- Single horizontal/vertical line in secondary color (geometric divider)
- Subtle opacity shape (10-20% opacity) in corner (triangle, circle)
- Minimal icon reference (if it relates directly to essence)
- Dots or dashes (rhythm element, max 3 total)

**Forbidden:**
- Patterns or textures
- Photography
- Multiple competing shapes
- Decorative elements that don't serve purpose
- Blurs, glows, or effects (except single accent line)

## 6. SAFE ZONES & SPECIFICATIONS

**Twitter Header (1500x500px):**
- Text center: Safe zone 200-1300px horizontal
- Vertical: Center at 250px
- Logo: Top-left corner (if included, 80x80px max)

**Telegram Channel (1590x400px):**
- Same horizontal safety
- Vertical: Center at 200px
- Tight composition (height constraint)

**Discord Server (960x540px):**
- Minimum safe zone for text: 100-860px
- Vertical: 100-440px
- Works at thumbnail size (320x180px)

**Website Banner (flexible):**
- Adapt to container width
- Maintain aspect ratio minimum 16:9 or 21:9
- Responsive: text scales proportionally

## 7. MOOD ARCHITECTURE

The banner should communicate:
- **Instantly:** What is this? (from logo + name)
- **In 2 seconds:** What's the vibe? (from colors + tagline)
- **In 5 seconds:** Why should I care? (from tone conveyed through design)

Not from words. From **visual language alone.**

## 8. CONTRAST & READABILITY
- Text color vs background: 4.5:1 minimum (WCAG AA standard)
- Test on mobile (Twitter thumbnail size)
- Test in grayscale (check if it still reads)
- Test on both light and dark contexts

## 9. VARIATIONS REQUIRED

1. **Primary orientation** (designed above)
2. **Dark mode variant** (if background is light, flip)
3. **Logo-left version** (if logo needs repositioning)
4. **Tagline-only version** (project name + tagline centered)

## 10. DESIGN RULES (NON-NEGOTIABLE)

✓ Typography is 70%+ of the design
✓ Color creates emotion, text creates meaning
✓ Every element has a job (no decoration)
✓ Negative space is intentional
✓ Readable at 50% size (mobile)
✓ Works in single color (B&W test)
✓ Professional yet bold
✓ Memorable in 3 seconds

---

# MIDJOURNEY / AI GENERATION PROMPT

"Minimal Web3 banner for {project_name}. 
Bold typography center-stage: '{project_name}' and '{tagline}'. 
Background: {visual_vibe} composition in {primary_color} and {secondary_color}.
Zero clutter. {tone} aesthetic.
Emphasis on readability and color contrast.
Modern sans-serif font, geometric and clean.
No photography, no patterns, no visual noise.
Color-driven design, text-first composition.
Professional, bold, minimal.
Aspect ratio 3:1 (social media standard)."

---

# DELIVERABLES CHECKLIST
- [ ] Main banner (1500x500px for Twitter)
- [ ] Telegram variant (1590x400px)
- [ ] Discord variant (960x540px)
- [ ] Dark mode version
- [ ] Light mode version
- [ ] High-res export (300 DPI)
- [ ] Web-optimized (72 DPI)
- [ ] PNG + JPG formats

---

# COLOR INTERACTION EXAMPLES

**If primary = Indigo, secondary = Lime:**
- Option A: Full indigo background, lime accent word in tagline
- Option B: Full lime background, indigo bold text
- Option C: Black background, indigo project name, lime tagline

Choose ONE. Don't layer both heavily.

---

# FINAL PHILOSOPHY

"A great banner doesn't need explanation. The viewer understands instantly through color and type. Anything else is noise. Kill the noise."

{style_guide if style_guide else ""}

Generate only the final design brief. Be direct. Be visual. Be ruthlessly minimal."""

    return prompt


# -------------------------------------------------
# TOOL 6: GENERATE X ASSETS (WEB3 MINIMALIST)
# -------------------------------------------------

def generate_x_assets(
    project_name: str,
    lore: str,
    tone: str,
    visual_vibe: str = "modern",
    color_palette: list = None,
    include_assets: list = None,
    style_guide: str = ""
) -> str:
    """
    Generate minimal X/Twitter asset design briefs for Web3.
    
    Philosophy: Design Consistency > Noise. Each asset is a variation on one theme.
    
    Args:
        project_name: Project name
        lore: Project narrative
        tone: Brand tone
        visual_vibe: Visual aesthetic (minimal, geometric, gradient, bold, dark)
        color_palette: [primary_color, secondary_color]
        include_assets: Which assets to generate (default: all)
        style_guide: Additional guidelines
    
    Returns:
        JSON string with asset briefs
    """
    
    if color_palette is None:
        color_palette = ["#6366f1", "#00ff88"]
    
    if include_assets is None:
        include_assets = ["pfp", "header", "meme", "buybot", "dexscreener"]
    
    primary = color_palette[0]
    secondary = color_palette[1] if len(color_palette) > 1 else primary
    
    prompt = f"""You are a Web3 art director obsessed with visual consistency and minimal design.

# PHILOSOPHY
**One DNA. Multiple expressions. Zero visual noise.**

Each asset echoes the same brand language—typography, color interaction, geometric precision. No decoration. No photographic elements. Pure design.

---

# PROJECT DNA
- **Name:** {project_name}
- **Tone:** {tone}
- **Aesthetic:** {visual_vibe}
- **Primary:** {primary}
- **Secondary:** {secondary}

# LORE
{lore}

---

# CORE PRINCIPLE: DESIGN LANGUAGE

All assets share:
✓ Same typography family (geometric sans-serif)
✓ Same color philosophy ({primary} + {secondary})
✓ Same spacing/alignment rules
✓ Minimal, geometric approach
✓ No clutter, no decoration
✓ Instant brand recognition

---

# OUTPUT FORMAT: VALID JSON ONLY

Return ONLY this JSON structure (no other text):

{{
  "project": "{project_name}",
  "color_system": {{
    "primary": "{primary}",
    "secondary": "{secondary}"
  }},
  "design_language": "Minimal geometric Web3 aesthetic. Typography-driven. Color-focused. Zero visual noise.",
  "assets": [
    {{
      "asset": "PFP",
      "dimensions": "400x400px",
      "brief": "..."
    }},
    {{
      "asset": "HEADER",
      "dimensions": "1500x500px",
      "brief": "..."
    }},
    {{
      "asset": "MEME",
      "dimensions": "1080x1080px",
      "brief": "..."
    }},
    {{
      "asset": "BUYBOT",
      "dimensions": "1200x800px",
      "brief": "..."
    }},
    {{
      "asset": "DEXSCREENER",
      "dimensions": "1200x600px",
      "brief": "..."
    }}
  ]
}}

---

# ASSET BRIEFS (DETAILED)

## 1. PFP (Profile Picture)
**Dimensions:** 400x400px (displays at 48x48, 200x200, 400x400)
**Purpose:** Avatar. Instant brand recognition at any scale.

**Design Philosophy:**
- **Core Element:** A single geometric mark derived from your logo/brand symbol
- **Execution:** Clean, bold, 1:1 square
- **Color:** Primary color fills the mark. Secondary as accent (optional, minimal)
- **Background:** Solid color (either primary, secondary, or neutral dark/light)
- **Typography:** ZERO text in PFP. Icon only.
- **Scalability:** Must read perfectly at 48px (Twitter thumbnail)

**Key Requirements:**
✓ Logo evolution or variation (not the same as main logo)
✓ High contrast
✓ Works at tiny scales
✓ Memorable silhouette
✓ No inner detail below 48px
✓ No gradients, no effects

**Mood:** Bold, confident, ownable

**AI Prompt:**
"Minimal Web3 profile avatar for {project_name}. Geometric symbol, {tone} aesthetic. Primary color {primary}. Single mark, no text. Perfect at 48px and 400px. Clean, sharp, iconic. No gradients, no effects. Professional yet bold."

**Variations:**
1. Primary on white background
2. White on primary background
3. Secondary accent version (if multi-color needed)

---

## 2. HEADER (Banner)
**Dimensions:** 1500x500px
**Purpose:** Twitter profile visual statement

**Design Philosophy:**
- **Text:** {project_name} + tagline/descriptor
- **Typography:** Large, bold, geometric sans-serif (same as PFP)
- **Color Strategy:** Primary dominates (60%+). Secondary for accent.
- **Background:** Solid or minimal gradient (option to choose one)
- **Additional Elements:** Subtle geometric shape OR accent line (1 only)

**Layout Options:**
A) Text left-aligned, color-blocked background right
B) Text centered, full primary background, secondary accent line
C) Text offset, secondary background with primary text overlay
(Designer chooses best fit for {tone})

**Key Requirements:**
✓ {project_name} occupies 40% width minimum
✓ Readable at 300px width (Twitter mobile)
✓ One color interaction ({primary} + {secondary})
✓ Consistent typography with PFP
✓ Safe zones for logo (if needed)
✓ No photography, no patterns

**Mood:** {tone}. Professional. Memorable.

**AI Prompt:**
"Web3 Twitter header for {project_name}. Dimensions 1500x500px. Bold typography: project name large. {visual_vibe} composition. Primary {primary}, secondary {secondary}. Minimal background, color-driven. {tone} aesthetic. No photos, no patterns. Emphasis on text and color contrast. Readable at mobile size."

**Variations:**
1. Light mode (dark text, light background)
2. Dark mode (light text, dark background)
3. Logo-left variant
4. Centered composition

---

## 3. MEME
**Dimensions:** 1080x1080px (square)
**Purpose:** Community engagement, viral potential, personality

**Design Philosophy:**
- **Approach:** Minimal text-based OR geometric visual humor
- **Brand Integration:** {project_name} branding subtle but present
- **Tone:** Reflects {tone} (if serious → dry humor; if playful → bold humor)
- **Color:** Uses {primary} and {secondary} (not full palette)
- **Style:** Clean layout, readable fonts, high contrast

**Content Types (choose 1 per meme):**
A) **Text-based:** Bold statement + {project_name} watermark
   - Typography: Large, geometric sans-serif
   - Text: 2-4 words max
   - Color: Primary text on secondary OR white on primary background
   
B) **Geometric humor:** Abstract shapes with layered meaning
   - Shapes: Circles, triangles, lines
   - Colors: Primary + secondary interplay
   - Concept: Subtle, clever, Web3-native
   
C) **Data visual:** Chart/graph element + humorous caption
   - Background: Primary or secondary
   - Text: Witty observation about crypto/Web3
   - Brand: Subtle corner watermark

**Key Requirements:**
✓ Readable at mobile scroll speed
✓ Clear focal point
✓ On-brand color + typography
✓ Memorable in 1 second
✓ Encourages sharing/engagement
✓ No photography, no complex patterns
✓ {project_name} watermark (small, strategic)

**Mood:** Engaging. Clever. On-brand.

**AI Prompt:**
"Minimal Web3 meme asset for {project_name}. Square 1080x1080px. {tone} humor. Bold typography. Primary {primary}, secondary {secondary}. Geometric or text-based composition. High contrast, readable at scroll speed. Clean, clever, shareable. No photos. {project_name} watermark. Modern sans-serif font."

**Variations:**
- Quarterly rotation (5-10 templates for community to use)
- Different humor styles (technical, absurdist, motivational)

---

## 4. BUYBOT (Product Showcase)
**Dimensions:** 1200x800px (landscape)
**Purpose:** Product feature highlight, trust-building, action CTA

**Design Philosophy:**
- **Focus:** Speed, automation, security
- **Layout:** Left-heavy (text/benefit), right visual (bot concept)
- **Typography:** {project_name} + 3-4 key benefits (maximum)
- **Color:** Primary accent on secondary OR inverse
- **Visual:** Minimal bot representation (geometric/abstract, NOT realistic)

**Content Hierarchy:**
1. **Project name** (top, large, {primary} color)
2. **Core benefit** (1 line, {secondary} color)
3. **3 Feature bullets:** Speed • Security • Automation (small, clean)
4. **Visual element:** Geometric bot icon OR abstract flow diagram (right side, 40% space)

**Visual Approach:**
- **Option A:** Abstract flowing lines representing automation (geometric, minimal)
- **Option B:** Stylized bot silhouette (geometric, not cute or cartoony)
- **Option C:** Data points/nodes with connecting lines (network aesthetic)

**Key Requirements:**
✓ Clear, scannable layout
✓ Communicates value instantly
✓ Professional + approachable
✓ Uses brand colors strategically
✓ Typography matches header/PFP
✓ Minimal visual elements
✓ No photorealism, no clutter

**Mood:** Confident. Trustworthy. Innovative.

**AI Prompt:**
"Web3 product showcase image for {project_name} buybot. Landscape 1200x800px. Bold typography on left (project name + 1 benefit). Right side: minimal geometric bot visualization. Primary {primary}, secondary {secondary}. Clean, modern, professional. Emphasizes speed and automation through design. No photos. Geometric aesthetic only. {tone} feeling. High contrast text."

**Variations:**
1. "Buy automation" focus
2. "Security & speed" focus
3. "Easy integration" focus

---

## 5. DEXSCREENER (DEX Listing Thumbnail)
**Dimensions:** 1200x600px (16:9 landscape)
**Purpose:** Token listing showcase, legitimacy, growth signal

**Design Philosophy:**
- **Data-focused:** Suggests growth, stability, trust
- **Layout:** Professional, minimal clutter
- **Color:** Primary + secondary used strategically
- **Typography:** {project_name} prominent, secondary metric/tagline
- **Visual:** Subtle uptrend indicator OR abstract growth visualization

**Content Elements:**
1. **Project name** (large, {primary}, top-left area)
2. **Contract/Ticker** (small, secondary, supporting text)
3. **One key metric** (volume, liquidity, holders—optional, minimal)
4. **Visual accent:** Subtle uptrend line OR geometric growth symbol (right/bottom)
5. **Tagline or differentiator** (1 line, secondary color)

**Visual Approach:**
- **Option A:** Minimal uptrend line ({secondary} color, subtle, not flashy)
- **Option B:** Abstract ascending shapes/dots (geometric, representing growth)
- **Option C:** Geometric patterns suggesting stability (grids, lines, balanced)

**Background:** 
- Solid {primary} OR solid {secondary} OR gradient (minimal, subtle transition)
- Must ensure 4.5:1 contrast for all text

**Key Requirements:**
✓ Professional, trustworthy aesthetic
✓ Readable in thumbnail (300px width)
✓ Clear hierarchy: Name > Metric > Visual
✓ Suggests legitimacy and growth
✓ Uses brand colors as markers
✓ Minimal, not cluttered
✓ No photorealism

**Mood:** Professional. Stable. Trustworthy. Growth-oriented.

**AI Prompt:**
"DEX Screener token listing thumbnail for {project_name}. Landscape 1200x600px. Professional, minimal design. Bold {project_name} on primary {primary} or secondary {secondary} background. Subtle growth indicator (uptrend line or ascending shapes). Clean, data-focused aesthetic. {tone} tone. No photos, no clutter. High contrast. Communicates trust and growth through minimal design."

**Variations:**
1. High volume version
2. High liquidity version
3. Community-driven version

---

# DESIGN SYSTEM RULES (ACROSS ALL ASSETS)

**Typography:**
- Font: Modern geometric sans-serif (Inter, Montserrat, Helvetica Neue)
- Weight: 700+ for headers, 400-500 for secondary
- Spacing: Generous, never cramped
- Alignment: Clean alignment grid

**Color Application:**
- Primary: 60-70% of visual weight
- Secondary: 20-30% accent or contrast
- Neutral: 10-20% (white/black/gray)
- Never blend colors (keep them distinct)

**Spacing & Grids:**
- 8px grid system (all elements align to 8px)
- Generous padding (min 20px from edges)
- Never tight or cramped

**Effects (FORBIDDEN):**
✗ Gradients (except minimal, subtle background transitions)
✗ Shadows or blur
✗ Textures or patterns
✗ Photographic elements
✗ Decorative flourishes
✓ Simple lines (1-2px only)
✓ Geometric shapes (solid fills)
✓ Intentional negative space

**Scalability Test:**
- All assets readable at 50% size
- All text legible at thumbnail
- Logo/mark works in B&W

---

# DELIVERABLES CHECKLIST

**For Each Asset:**
- [ ] Main file (exact dimensions)
- [ ] Dark mode variant (if applicable)
- [ ] Light mode variant (if applicable)
- [ ] High-res export (300 DPI)
- [ ] Web-optimized (72 DPI)
- [ ] PNG + JPG formats

**Quality Checks:**
- [ ] Color accuracy across formats
- [ ] Text contrast ratio 4.5:1 minimum
- [ ] Readable at 50% scale
- [ ] Brand consistency across all 5 assets
- [ ] Zero visual noise
- [ ] Professional finish

---

# FINAL PHILOSOPHY

"A Web3 brand identity lives in consistency, not variety. Each asset reflects the same DNA: clean typography, purposeful color, geometric precision. The sum is stronger than individual parts. Every pixel earns its place."

{style_guide if style_guide else ""}

Generate the JSON now. Output ONLY the valid JSON structure above. No explanations, no additional text.
DO NOT CALL ANOTHER TOOL !
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