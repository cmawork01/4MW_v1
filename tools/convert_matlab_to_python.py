"""Generate Python placeholders from MATLAB .m files."""

from __future__ import annotations

from pathlib import Path
import re


FUNCTION_RE = re.compile(r"^function\s+(?:(?:\[[^\]]*\]|\w+)\s*=\s*)?(\w+)")


def extract_function_name(matlab_source: str) -> str | None:
    for line in matlab_source.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("%"):
            continue
        match = FUNCTION_RE.match(stripped)
        if match:
            return match.group(1)
        return None
    return None


def build_python_module(matlab_path: Path, matlab_source: str) -> str:
    function_name = extract_function_name(matlab_source)
    header = (
        f"# Auto-generated from {matlab_path.name}\n"
        "# NOTE: This is a placeholder stub. Manual translation required.\n\n"
        "from __future__ import annotations\n\n"
    )
    docstring = f'"""\nOriginal MATLAB source:\n\n{matlab_source}\n"""\n\n'
    if function_name:
        body = (
            f"def {function_name}(*args, **kwargs):\n"
            "    \"\"\"Placeholder for translated MATLAB function.\"\"\"\n"
            "    raise NotImplementedError(\n"
            "        \"This function requires manual translation from MATLAB.\"\n"
            "    )\n"
        )
    else:
        body = (
            "def main():\n"
            "    \"\"\"Placeholder for translated MATLAB script.\"\"\"\n"
            "    raise NotImplementedError(\n"
            "        \"This script requires manual translation from MATLAB.\"\n"
            "    )\n"
        )
    return f"{header}{docstring}{body}"


def convert_matlab_files(repo_root: Path) -> list[Path]:
    created = []
    for matlab_path in repo_root.rglob("*.m"):
        python_path = matlab_path.with_suffix(".py")
        matlab_source = matlab_path.read_text(encoding="utf-8", errors="ignore")
        python_source = build_python_module(matlab_path, matlab_source)
        python_path.write_text(python_source, encoding="utf-8")
        created.append(python_path)
    return created


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    created = convert_matlab_files(repo_root)
    print(f"Generated {len(created)} Python placeholder files.")


if __name__ == "__main__":
    main()
