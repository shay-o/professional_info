# Career Achievements System

A structured workflow for capturing career stories, converting them to structured data, and generating polished professional documents.

## Overview

This system maintains two layers:
- **Raw layer**: Natural language stories you write in markdown
- **Structured layer**: JSON data automatically generated from raw stories
- **Public layer**: Polished documents generated from structured data

### Data Flow

```
achievements_raw.md (private)
    ↓ [LLM with convert_to_json.md prompt]
achievements.json (public)
    ↓ [LLM with generate_experience.md prompt OR Python script]
experience.md (public)
```

## Repository Structure

```
professional_info_private/          # Private repository
├── achievements_raw.md             # Your informal achievement stories
├── professional_info_private.md    # General career notes
├── readme.md                       # Private repo documentation
└── prompts/
    └── convert_to_json.md          # Prompt for converting stories to JSON

professional_info/                  # Public repository
├── achievements.json               # Structured achievement data
├── experience.md                   # Public-facing experience document
├── experience_backup_YYYY-MM-DD.md # Backup of previous version
├── generate_experience_md.py       # Python script to generate experience.md
├── README.md                       # This file
└── prompts/
    ├── generate_experience.md      # Prompt for generating experience.md
    ├── cover_letter_prompt.md      # (Future) Cover letter generation
    └── interview_prompt.md         # (Future) Interview prep
```

## Quick Start

### 1. Add a New Achievement Story

Edit `../professional_info_private/achievements_raw.md` and add your story using the template:

```markdown
**Working title**
[Short descriptive title]

**Role / org / timeframe**
- Role: [Your role]
- Organization: [Company name]
- Timeframe: [Start - End]

**Context / situation**
[What was happening?]

**Problem / challenge**
[What needed to be solved?]

**What I actually did**
[Your specific actions]

**Impact / results**
- Quantitative: [Numbers, metrics]
- Qualitative: [Outcomes, feedback]

**Skills / themes**
[Key competencies]

**Evidence / links**
[Supporting materials]

**Reflection**
[What you learned]

**Tags**
[Keywords for filtering]
```

### 2. Convert to JSON

Use an LLM (Claude, ChatGPT, etc.) with the conversion prompt:

1. Read `../professional_info_private/prompts/convert_to_json.md`
2. Provide the LLM with:
   - The conversion prompt
   - Your current `achievements.json` file
   - Your new raw achievement story
3. The LLM will output an updated `achievements.json` with your new achievement appended
4. Save the updated JSON to `achievements.json`

**Important**: The LLM will append to existing achievements, not replace them.

### 3. Generate experience.md

You have two options:

#### Option A: Use LLM (More Flexible)

1. Read `prompts/generate_experience.md`
2. Provide the LLM with:
   - The generation prompt
   - Your `achievements.json` file
3. The LLM will output a complete `experience.md`
4. Review and save

#### Option B: Use Python Script (More Consistent)

```bash
cd /Users/jamesoreilly/Documents/Projects/professional_info

# Generate with default settings
python3 generate_experience_md.py

# Or specify input/output files
python3 generate_experience_md.py --input achievements.json --output experience_generated.md
```

**Note**: The script outputs to `experience_generated.md` by default. Review it before replacing `experience.md`.

## JSON Schema

The `achievements.json` file follows this structure:

```json
{
  "version": "1.0",
  "last_updated": "YYYY-MM-DD",
  "person": {
    "name": "Your Name",
    "linkedin": "URL",
    "github": "URL"
  },
  "roles": [
    {
      "id": "unique-role-id",
      "title": "Job Title",
      "organization": "Company",
      "start_date": "YYYY-MM",
      "end_date": "YYYY-MM" or null,
      "summary": "Role description"
    }
  ],
  "achievements": [
    {
      "id": "unique-achievement-id",
      "role_id": "role-id",
      "title": "Achievement Title",
      "timeframe": "YYYY - YYYY",
      "context": "Situation description",
      "problem": "Challenge description",
      "actions": ["Action 1", "Action 2"],
      "impact": {
        "quantitative": ["Metric 1", "Metric 2"],
        "qualitative": ["Outcome 1", "Outcome 2"]
      },
      "competencies": ["Skill 1", "Skill 2"],
      "story": "Personal reflection",
      "tags": ["tag1", "tag2"],
      "evidence_links": ["url1"],
      "reflection": "What was learned"
    }
  ]
}
```

## Workflow Tips

### Writing Good Achievement Stories

- **Be specific**: Include numbers, names, technologies
- **Show impact**: What changed as a result of your work?
- **Include context**: Why was this challenging or important?
- **Capture reflection**: What did you learn? What would you do differently?
- **Add evidence**: Links to presentations, demos, documents

### Maintaining the System

1. **Write stories immediately**: Don't wait until you need to update your resume
2. **Commit to git regularly**: Track changes to both raw stories and JSON
3. **Review quarterly**: Update experience.md every few months
4. **Tag consistently**: Use consistent tags to make filtering easier

### Using Tags Effectively

Useful tag categories:
- **Type**: leadership, technical, strategy, customer-facing
- **Skills**: AI, migration, infrastructure, analytics
- **Products**: Product names, technologies
- **Scale**: startup, enterprise, high-scale
- **Outcome**: launched, optimized, established, grew

## Advanced Usage

### Filtering by Tags

When generating experience.md, you can ask the LLM to focus on specific tags:

"Generate experience.md focusing on achievements tagged with 'leadership' and 'technical'"

### Custom Outputs

The structured JSON can be used for:
- Tailored resumes for specific roles
- Cover letters highlighting relevant experience
- Interview preparation (organized by competency)
- LinkedIn profile updates
- Performance reviews

### Future Enhancements

Planned additions:
- Cover letter generation prompt
- Interview preparation prompt
- Embeddings for interactive "interview me" app
- Filtering/search by competency, date, or tag
- Export to different formats (PDF, HTML)

## Troubleshooting

### JSON Syntax Errors

If the LLM produces invalid JSON:
1. Copy the output to a JSON validator (jsonlint.com)
2. Fix syntax errors (usually missing commas or quotes)
3. Or ask the LLM to fix it: "The JSON has a syntax error on line X, please fix it"

### Duplicate IDs

Achievement IDs must be unique. Format: `{topic-keyword}-{year}`
- Good: "edge-enrichment-2023", "omnivore-migration-2022"
- Bad: "project1", "achievement"

### Lost Information

If generated experience.md is missing details:
1. Check that the information exists in achievements.json
2. Adjust the generation prompt to emphasize those details
3. Or manually edit experience.md (it's okay to polish the output)

## Backup Strategy

- `experience_backup_YYYY-MM-DD.md` files are created before major updates
- Git commit history provides version control
- Keep raw stories indefinitely - they're the source of truth

## Questions or Issues?

This is your personal system - adapt it as needed! The key principle: write stories informally, structure them once, use them many times.
