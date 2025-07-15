import os
import re
import shutil
from pathlib import Path

# --- CONFIG ---
LESSONS_DIR = Path(__file__).parent
README_PATH = LESSONS_DIR / "README.md"
GITIGNORE_PATH = LESSONS_DIR / ".gitignore"
REQUIREMENTS_PATH = LESSONS_DIR / "requirements.txt"

# Dars papkasi nomi uchun regex (masalan, 06-dars, 24-dars.Functions)
LESSON_DIR_RE = re.compile(r"^(\d{1,2})-dars")

# Amaliyot papkasi nomlari
PRACTICE_NAMES = ["practice", "Practice",
                  "Practises", "Amaliyot", "Practices", "practices"]

# Foydali funksiya: nomni tozalash (faqat lotin harflari, raqam, _ va .)


def clean_name(name):
    name = name.replace(" ", "_").replace(
        ",", "_").replace("'", "").replace("`", "")
    name = re.sub(r"[^a-zA-Z0-9._-]", "_", name)
    return name


def get_lesson_dirs():
    """python_lessons ichidagi dars papkalarini aniqlaydi."""
    dirs = []
    for item in LESSONS_DIR.iterdir():
        match = LESSON_DIR_RE.match(item.name)
        if item.is_dir() and match:
            dirs.append((int(match.group(1)), item))
    # Raqam bo'yicha tartiblash
    return [d[1] for d in sorted(dirs, key=lambda x: x[0])]


def normalize_lesson_dir(lesson_dir):
    """Dars papkasini XX-dars formatiga keltiradi."""
    match = LESSON_DIR_RE.match(lesson_dir.name)
    if not match:
        return lesson_dir
    num = int(match.group(1))
    new_name = f"{num:02d}-dars"
    if lesson_dir.name != new_name:
        new_path = lesson_dir.parent / new_name
        if not new_path.exists():
            lesson_dir.rename(new_path)
        return new_path
    return lesson_dir


def move_practice_dirs(lesson_dir):
    """Amaliyot papkalarini yagona practice/ papkasiga birlashtiradi."""
    for name in PRACTICE_NAMES:
        p = lesson_dir / name
        if p.exists() and p.is_dir():
            target = lesson_dir / "practice"
            if not target.exists():
                p.rename(target)
            elif p != target:
                # Bir nechta practice papkasi bo'lsa, fayllarni birlashtirish
                for f in p.iterdir():
                    shutil.move(str(f), str(target / f.name))
                p.rmdir()


def clean_files_and_dirs(lesson_dir):
    """Fayl va papka nomlarini tozalaydi."""
    for item in lesson_dir.iterdir():
        if item.is_file():
            new_name = clean_name(item.name)
            if new_name != item.name:
                item.rename(item.parent / new_name)
        elif item.is_dir() and item.name != "practice":
            new_name = clean_name(item.name)
            if new_name != item.name:
                item.rename(item.parent / new_name)


def generate_readme(lesson_dirs):
    lines = [
        "# Python Asoslari Darslari\n",
        "\n",
        "Ushbu repozitoriyda Python dasturlash asoslari bo'yicha darslar va amaliyotlar jamlangan.\n",
        "\n",
        "## Darslar ro'yxati\n",
        "\n",
    ]
    for d in lesson_dirs:
        match = LESSON_DIR_RE.match(d.name)
        if not match:
            continue
        num = int(match.group(1))
        title = d.name
        # Dars fayllari ro'yxati
        files = [f for f in d.iterdir() if f.is_file() and f.suffix == ".py"]
        lines.append(
            f"- **{num:02d}-dars**: {', '.join(f.name for f in files) if files else 'Dars fayllari'}")
    lines += [
        "\n",
        "---\n",
        "\n",
        "### Foydalanish\n",
        "\n",
        "1. Har bir dars papkasiga kiring va kerakli `.py` faylni ishga tushiring.\n",
        "2. Amaliyotlar `practice/` papkasida.\n",
        "\n",
        "---\n",
        "\n",
        "> Muallif: Uktam Turgunov  ",
        "> GitHub: [your-profile](https://github.com/your-profile)\n"
    ]
    return "".join(lines)


def write_gitignore():
    content = """__pycache__/
*.pyc
.env
.venv
.idea/
.DS_Store
*.pyo
*.pyd
*.swp
*.bak
*.tmp
"""
    with open(GITIGNORE_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def write_requirements():
    # Minimal, foydalanuvchi kutubxonalarini aniqlash uchun (optional: pipreqs)
    with open(REQUIREMENTS_PATH, "w", encoding="utf-8") as f:
        f.write("# Zarur kutubxonalar shu yerga yoziladi\n")


def main():
    lesson_dirs = get_lesson_dirs()
    new_dirs = []
    for d in lesson_dirs:
        d2 = normalize_lesson_dir(d)
        move_practice_dirs(d2)
        clean_files_and_dirs(d2)
        new_dirs.append(d2)
    # README.md
    readme = generate_readme(new_dirs)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)
    # .gitignore va requirements.txt
    write_gitignore()
    write_requirements()
    print("Tartiblash va README.md generatsiyasi yakunlandi!")


if __name__ == "__main__":
    main()
