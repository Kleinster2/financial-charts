#!/usr/bin/env python3
"""Add cross-vault links between investing and technologies vault notes.

Reads each pair, adds ### Cross-vault subsection to the Related section
(or appends at end if no Related section exists). Skips if the note
already has a cross-vault link to the target vault.

Usage:
    python scripts/add_cross_vault_links.py --dry-run   # preview changes
    python scripts/add_cross_vault_links.py              # apply changes
"""

import re
import sys
from pathlib import Path

# Pairs: (investing_path, tech_stem, tech_rel_path_no_ext)
PAIRS = [
    ("investing/Actors/IBM.md", "IBM", "IBM"),
    ("investing/Actors/NanoClaw.md", "NanoClaw", "NanoClaw"),
    ("investing/Actors/PicoClaw.md", "PicoClaw", "PicoClaw"),
    ("investing/Concepts/Advanced packaging.md", "Advanced Packaging", "Advanced Packaging"),
    ("investing/Concepts/Agentic AI.md", "Agentic AI", "Agentic AI"),
    ("investing/Concepts/Agriculture.md", "Agriculture", "Agriculture"),
    ("investing/Concepts/Aluminum.md", "Aluminum", "Aluminum"),
    ("investing/Concepts/Batteries.md", "Batteries", "Batteries"),
    ("investing/Concepts/Copper.md", "Copper", "Copper"),
    ("investing/Concepts/Data center infrastructure.md", "Data Center Infrastructure", "Data Center Infrastructure"),
    ("investing/Concepts/EUV lithography.md", "EUV Lithography", "EUV Lithography"),
    ("investing/Concepts/Local-first AI.md", "Local-first AI", "Local-first AI"),
    ("investing/Concepts/Oil.md", "Oil", "Oil"),
    ("investing/Concepts/Prompt injection.md", "Prompt Injection", "Prompt Injection"),
    ("investing/Concepts/Quantum computing.md", "Quantum Computing", "Quantum Computing"),
    ("investing/Concepts/Venture capital.md", "Venture Capital", "Venture Capital"),
    ("investing/Sectors/Robotics.md", "Robotics", "Robotics"),
    ("investing/Sectors/Semiconductors.md", "Semiconductors", "Semiconductors"),
    ("investing/Sectors/Sensors.md", "Sensors", "Sensors"),
    ("investing/Sectors/Venture Capital.md", "Venture Capital", "Venture Capital"),
]

TECH_VAULT = Path("C:/Users/klein/obsidian/technologies")

# Descriptions for each direction
INVESTING_DESC = {
    "IBM": "technical history: mainframes, System/360, Watson, patent portfolio",
    "NanoClaw": "technical architecture and agent capabilities",
    "PicoClaw": "technical architecture and agent capabilities",
    "Advanced Packaging": "full technical breakdown: CoWoS generations, interposer stitching, hybrid bonding, TSV mechanics",
    "Agentic AI": "technical foundations: tool use, planning loops, memory architectures",
    "Agriculture": "crop science, precision agriculture, biotech applications",
    "Aluminum": "metallurgy, smelting processes, alloy properties",
    "Batteries": "cell chemistry, energy density curves, manufacturing processes",
    "Copper": "metallurgy, conductivity properties, extraction processes",
    "Data Center Infrastructure": "power delivery, cooling architectures, networking topology",
    "EUV Lithography": "optics physics, 13.5nm wavelength, pellicle challenges, High-NA roadmap",
    "Local-first AI": "on-device inference, model compression, edge deployment architectures",
    "Oil": "refining processes, hydrocarbon chemistry, extraction technology",
    "Prompt Injection": "attack vectors, defense mechanisms, alignment implications",
    "Quantum Computing": "qubit architectures, error correction, decoherence challenges",
    "Venture Capital": "fund structures, LP/GP mechanics, vintage year analysis",
    "Robotics": "actuators, control systems, perception stack, manipulation",
    "Semiconductors": "fabrication processes, transistor physics, node scaling",
    "Sensors": "MEMS, LiDAR, image sensors, signal processing",
}


def encode_path(path: str) -> str:
    return path.replace(" ", "%20").replace("/", "%2F")


def has_cross_vault_link(content: str, vault_name: str) -> bool:
    return f"obsidian://open?vault={vault_name}" in content


def get_investing_folder(path_str: str) -> str:
    """Get the investing vault folder for the note."""
    if "/Actors/" in path_str:
        return "Actors"
    elif "/Concepts/" in path_str:
        return "Concepts"
    elif "/Sectors/" in path_str:
        return "Sectors"
    elif "/Products/" in path_str:
        return "Products"
    elif "/Events/" in path_str:
        return "Events"
    elif "/Theses/" in path_str:
        return "Theses"
    return ""


def add_cross_vault_section(content: str, link_line: str) -> str:
    """Add a ### Cross-vault subsection with the link line.

    If ### Cross-vault already exists, append to it.
    If ## Related exists, add ### Cross-vault after it.
    Otherwise append at end.
    """
    if "### Cross-vault" in content:
        # Append to existing cross-vault section
        # Find the end of the cross-vault section (next ## or ### or end)
        cv_pos = content.index("### Cross-vault")
        after_header = content[cv_pos:]
        # Find next section header after cross-vault
        next_section = re.search(r'\n##[# ]', after_header[len("### Cross-vault"):])
        if next_section:
            insert_pos = cv_pos + len("### Cross-vault") + next_section.start()
            return content[:insert_pos] + "\n" + link_line + content[insert_pos:]
        else:
            # Append at end
            return content.rstrip() + "\n" + link_line + "\n"

    # Look for ## Related section
    related_match = re.search(r'^## Related\b', content, re.MULTILINE)
    if related_match:
        # Find the end of the Related section content
        related_pos = related_match.start()
        after_related = content[related_pos:]
        # Find next ## section after Related
        next_section = re.search(r'\n## (?!Related)', after_related)
        if next_section:
            insert_pos = related_pos + next_section.start()
        else:
            insert_pos = len(content.rstrip())

        block = f"\n\n### Cross-vault\n{link_line}\n"
        return content[:insert_pos] + block + content[insert_pos:]

    # No Related section — append at end
    block = f"\n### Cross-vault\n{link_line}\n"
    return content.rstrip() + "\n" + block


def main():
    dry_run = "--dry-run" in sys.argv

    changes = []

    for inv_path_str, tech_stem, tech_rel_path in PAIRS:
        inv_path = Path(inv_path_str)
        tech_path = TECH_VAULT / f"{tech_stem}.md"
        inv_stem = inv_path.stem
        inv_folder = get_investing_folder(inv_path_str)

        # --- Investing note → Technologies ---
        if inv_path.exists():
            content = inv_path.read_text(encoding="utf-8")
            if not has_cross_vault_link(content, "technologies"):
                encoded = encode_path(tech_rel_path)
                desc = INVESTING_DESC.get(tech_stem, "technical details and mechanisms")
                link = f"- [Technologies: {tech_stem}](obsidian://open?vault=technologies&file={encoded}) — {desc}"
                new_content = add_cross_vault_section(content, link)
                changes.append((inv_path, new_content, f"  + {inv_stem} → technologies/{tech_stem}"))
            else:
                if dry_run:
                    print(f"  SKIP {inv_stem} (already has technologies link)")

        # --- Technologies note → Investing ---
        if tech_path.exists():
            content = tech_path.read_text(encoding="utf-8")
            if not has_cross_vault_link(content, "investing"):
                inv_encoded = encode_path(f"{inv_folder}/{inv_stem}" if inv_folder else inv_stem)
                link = f"- [Investing: {inv_stem}](obsidian://open?vault=investing&file={inv_encoded}) — investment angle: market dynamics, company positioning, supply chain economics"
                new_content = add_cross_vault_section(content, link)
                changes.append((tech_path, new_content, f"  + technologies/{tech_stem} → {inv_stem}"))
            else:
                if dry_run:
                    print(f"  SKIP technologies/{tech_stem} (already has investing link)")
        elif dry_run:
            print(f"  MISSING {tech_path}")

    if dry_run:
        print(f"\n{len(changes)} files would be modified:")
        for _, _, desc in changes:
            print(desc.encode("ascii", "replace").decode())
        return

    for path, new_content, desc in changes:
        path.write_text(new_content, encoding="utf-8")
        print(desc.encode("ascii", "replace").decode())

    print(f"\nDone: {len(changes)} files modified.")


if __name__ == "__main__":
    main()
