#!/usr/bin/env python3
"""
Generate experience.md from achievements.json

This script reads structured achievement data and generates a polished,
public-facing markdown document for potential employers.

Usage:
    python generate_experience_md.py [--input achievements.json] [--output experience.md]
"""

import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


def load_achievements(filepath: Path) -> Dict[str, Any]:
    """Load achievements from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def format_date_range(start_date: str, end_date: str = None) -> str:
    """Format date range for display."""
    if not start_date and not end_date:
        return ""

    if start_date and end_date:
        return f"{start_date} - {end_date}"
    elif start_date:
        return f"{start_date} - Present"
    else:
        return ""


def get_role_achievements(data: Dict[str, Any], role_id: str) -> List[Dict[str, Any]]:
    """Get all achievements for a specific role."""
    return [a for a in data['achievements'] if a['role_id'] == role_id]


def format_achievement(achievement: Dict[str, Any]) -> str:
    """Format a single achievement as markdown."""
    lines = []

    # Title
    lines.append(f"* **{achievement['title']}:** {achievement['problem']}")

    # Actions (select top 2-3 most important)
    if achievement['actions']:
        for action in achievement['actions'][:3]:
            lines.append(f"   - {action}")

    # Quantitative impact
    if achievement['impact'].get('quantitative'):
        for metric in achievement['impact']['quantitative']:
            lines.append(f"   - {metric}")

    # Qualitative impact (select most important)
    if achievement['impact'].get('qualitative'):
        for outcome in achievement['impact']['qualitative'][:2]:
            lines.append(f"   - {outcome}")

    lines.append("")  # Empty line after achievement
    return "\n".join(lines)


def generate_profile_summary(data: Dict[str, Any]) -> str:
    """Generate profile summary from data."""
    # Count years of experience from roles
    roles = data['roles']
    if not roles:
        return "Experienced product and analytics professional."

    # Get most recent role
    recent_role = roles[0]

    # Extract common competencies
    all_competencies = []
    for achievement in data['achievements']:
        all_competencies.extend(achievement.get('competencies', []))

    # Get top competencies (simplified - just take first few unique ones)
    top_competencies = list(dict.fromkeys(all_competencies))[:3]

    summary = f"Seasoned product and analytics professional with extensive experience in "
    summary += f"{', '.join(top_competencies[:2]).lower()}"
    summary += f". Currently {recent_role['title']} with expertise in data-driven decision making, "
    summary += "technical product management, and cross-functional leadership."

    return summary


def generate_key_achievements_section(data: Dict[str, Any]) -> str:
    """Generate Key Achievements & Impact section."""
    lines = ["## Key Achievements & Impact", ""]

    # Select top 3 achievements based on having quantitative impact and multiple tags
    scored_achievements = []
    for achievement in data['achievements']:
        score = 0
        # Score based on quantitative metrics
        score += len(achievement['impact'].get('quantitative', []))
        # Score based on number of competencies (indicates complexity)
        score += len(achievement.get('competencies', [])) * 0.5
        # Score based on tags
        score += len(achievement.get('tags', [])) * 0.3

        scored_achievements.append((score, achievement))

    # Sort by score and take top 3
    scored_achievements.sort(reverse=True, key=lambda x: x[0])
    top_achievements = [a for score, a in scored_achievements[:3]]

    for achievement in top_achievements:
        lines.append(f"### {achievement['title']}")
        lines.append(achievement['problem'])
        lines.append("")

        # Add key outcomes
        if achievement['impact'].get('quantitative'):
            lines.append("**Impact:**")
            for metric in achievement['impact']['quantitative']:
                lines.append(f"- {metric}")

        if achievement['impact'].get('qualitative'):
            for outcome in achievement['impact']['qualitative'][:2]:
                lines.append(f"- {outcome}")

        lines.append("")

    return "\n".join(lines)


def generate_professional_experience_section(data: Dict[str, Any]) -> str:
    """Generate Professional Experience section."""
    lines = ["# Professional Experience", ""]

    # Process each role
    for role in data['roles']:
        # Role header
        date_range = format_date_range(role.get('start_date'), role.get('end_date'))
        lines.append(f"## {role['title']} at {role['organization']} ({date_range})")
        lines.append("")

        # Role summary
        if role.get('summary'):
            lines.append(role['summary'])
            lines.append("")

        # Get achievements for this role
        role_achievements = get_role_achievements(data, role['id'])

        if role_achievements:
            lines.append("### Key Projects & Achievements")
            lines.append("")

            for achievement in role_achievements:
                lines.append(format_achievement(achievement))

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def generate_expertise_section(data: Dict[str, Any]) -> str:
    """Generate Key Areas of Expertise section."""
    lines = ["## Key Areas of Expertise", ""]

    # Collect all competencies
    competency_dict = {}
    for achievement in data['achievements']:
        for comp in achievement.get('competencies', []):
            if comp not in competency_dict:
                competency_dict[comp] = []
            competency_dict[comp].append(achievement['title'])

    # Group related competencies (simplified - just list top ones)
    lines.append("### Product Management & Strategy")
    pm_skills = [k for k in competency_dict.keys() if 'product' in k.lower() or 'strategy' in k.lower() or 'stakeholder' in k.lower()]
    for skill in pm_skills[:4]:
        lines.append(f"* **{skill}**: Demonstrated in {', '.join(competency_dict[skill][:2])}")
    lines.append("")

    lines.append("### Technical Leadership")
    tech_skills = [k for k in competency_dict.keys() if 'technical' in k.lower() or 'infrastructure' in k.lower() or 'architecture' in k.lower()]
    for skill in tech_skills[:4]:
        lines.append(f"* **{skill}**: Demonstrated in {', '.join(competency_dict[skill][:2])}")
    lines.append("")

    lines.append("### Collaboration & Influence")
    collab_skills = [k for k in competency_dict.keys() if 'cross-functional' in k.lower() or 'leadership' in k.lower() or 'collaboration' in k.lower()]
    for skill in collab_skills[:4]:
        lines.append(f"* **{skill}**: Demonstrated in {', '.join(competency_dict[skill][:2])}")
    lines.append("")

    return "\n".join(lines)


def generate_experience_md(data: Dict[str, Any]) -> str:
    """Generate the complete experience.md content."""
    lines = []

    # Front matter
    lines.append("---")
    lines.append("layout: default")
    lines.append("---")
    lines.append("")

    # Header
    person = data['person']
    lines.append(f"# {person['name']} – Professional Experience")
    lines.append(f"Last update {datetime.now().strftime('%B %Y')}")
    lines.append("")

    # Profile Summary
    lines.append("**Profile Summary**")
    lines.append(generate_profile_summary(data))
    lines.append("")

    # References
    lines.append("### References")
    lines.append(f"[LinkedIn Profile]({person.get('linkedin', '')})")
    lines.append("")
    lines.append(f"[GitHub Profile]({person.get('github', '')})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Key Achievements & Impact
    lines.append(generate_key_achievements_section(data))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Professional Experience
    lines.append(generate_professional_experience_section(data))
    lines.append("")

    # Key Areas of Expertise
    lines.append(generate_expertise_section(data))

    return "\n".join(lines)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Generate experience.md from achievements.json'
    )
    parser.add_argument(
        '--input',
        type=Path,
        default=Path('achievements.json'),
        help='Input JSON file (default: achievements.json)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('experience_generated.md'),
        help='Output markdown file (default: experience_generated.md)'
    )

    args = parser.parse_args()

    # Load data
    print(f"Loading achievements from {args.input}...")
    data = load_achievements(args.input)

    # Generate markdown
    print("Generating experience.md...")
    content = generate_experience_md(data)

    # Write output
    print(f"Writing to {args.output}...")
    with open(args.output, 'w') as f:
        f.write(content)

    print("Done!")


if __name__ == '__main__':
    main()
