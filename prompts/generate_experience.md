# Prompt: Generate experience.md from achievements.json

## Your Task

You are a professional resume and career document writer. Your task is to read `achievements.json` and generate a polished, public-facing `experience.md` document suitable for potential employers.

## Instructions

1. **Read achievements.json** to understand:
   - Person information (name, links)
   - All roles and their date ranges
   - All achievements organized by role

2. **Generate a markdown document** with the following structure:

```markdown
---
layout: default
---

# [Person Name] – Professional Experience
Last update [Month Year]

**Profile Summary**
[1-2 paragraph summary highlighting key expertise, years of experience, and areas of focus]

### References
[LinkedIn Profile](url)
[GitHub Profile](url)
[Other relevant links from person data]

---

## Key Achievements & Impact

[2-3 standout achievements that demonstrate significant impact, with metrics]

---

# Professional Experience

## [Role Title] at [Organization] ([Start Date] - [End Date])

[Brief role summary from roles array]

### Key Projects & Achievements

* **[Achievement Title]:** [Achievement description]
   - [Key action or outcome]
   - [Quantitative impact if available]
   - [Qualitative impact if available]

[Repeat for each achievement in this role]

[Repeat for each role]

---

## Key Areas of Expertise

### [Competency Category 1]
[Description with examples from achievements]

### [Competency Category 2]
[Description with examples from achievements]

[Continue for major competency areas]
```

## Formatting Guidelines

### Profile Summary
- Start with years of experience and current/most recent role
- Highlight 2-3 key areas of expertise based on most prominent tags/competencies
- Mention any notable companies or impact areas
- Keep to 2-3 sentences maximum

### Key Achievements & Impact Section
- Select 2-4 most impressive achievements based on:
  - Scale and impact (quantitative metrics)
  - Strategic importance
  - Cross-functional leadership
  - Innovation or "first of its kind" projects
- Lead with results and metrics
- Be concise but specific

### Professional Experience Section
- List roles in reverse chronological order (most recent first)
- For each role:
  - Include full date range
  - Brief 1-2 sentence summary of role scope
  - List 3-7 key achievements as bullet points
  - Focus on outcomes and impact, not just activities
  - Include quantitative metrics where available
  - Use strong action verbs (Led, Built, Drove, Established, etc.)

### Key Areas of Expertise
- Group competencies from across all achievements into 4-6 major categories:
  - Product Management & Strategy
  - Technical Leadership
  - User Research & Discovery
  - Cross-functional Collaboration
  - Analytics & Data
  - Communication & Influence
- For each category, provide 2-4 bullet points with specific examples
- Reference specific achievements as evidence

## Content Guidelines

### What to Include
- All roles from the roles array
- Selected achievements that best demonstrate capabilities
- Quantitative metrics and scale (users, revenue, performance numbers)
- Evidence of leadership and cross-functional work
- Technical depth where relevant
- Customer/user impact

### What to Emphasize
- Leadership and strategic thinking
- Cross-functional collaboration and influence
- Technical depth and architecture decisions
- Scale and complexity
- Innovation and problem-solving
- Measurable business impact

### What to Minimize or Exclude
- Internal company jargon (explain acronyms on first use)
- Overly technical details that obscure the impact
- Achievements with minimal business impact
- Reflection and learning sections (keep these in the JSON)
- Tags (these are for internal organization)

### Tone and Style
- Professional but not corporate
- Confident but not boastful
- Specific and concrete (use numbers, names, examples)
- Action-oriented (focus on what you did and the outcome)
- Balanced (both leadership/strategy AND technical execution)

## Selection Criteria for Achievements

When you have many achievements in the JSON:

1. **Prioritize by impact**: Choose achievements with strong quantitative results
2. **Diversify competencies**: Show range across technical, leadership, strategy, etc.
3. **Recent over old**: Weight recent work more heavily unless older work is exceptional
4. **Cross-functional over narrow**: Highlight work that required collaboration across teams
5. **Innovation over maintenance**: Emphasize new initiatives over steady-state work

You may include 5-8 achievements per role, focusing on the most relevant and impressive.

## Important Notes

- **Do not invent information**: Only use data present in achievements.json
- **Preserve accuracy**: Keep all metrics and dates exactly as stated
- **Maintain context**: Don't oversimplify complex projects to the point of losing meaning
- **Update the date**: Set "Last update" to current month and year
- **Professional tone**: This is for potential employers, not internal documentation

## Output

Return the complete markdown file, properly formatted and ready to use.
