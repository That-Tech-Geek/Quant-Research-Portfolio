import os
import subprocess
from pathlib import Path

PAPERS_DIR = Path(r"D:\Quant_Research_Library\papers")
FINAL_DIR = Path(r"D:\Quant_Research_Library\final-papers")
FINAL_DIR.mkdir(parents=True, exist_ok=True)

def compile_paper(tex_file):
    print(f"Compiling {tex_file.name}...")
    # Run pdflatex twice for references/toc
    for _ in range(2):
        process = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-output-directory", str(tex_file.parent), str(tex_file)],
            capture_output=True,
            text=True
        )
    
    pdf_file = tex_file.with_suffix(".pdf")
    if pdf_file.exists():
        target_path = FINAL_DIR / pdf_file.name
        pdf_file.replace(target_path)
        print(f"Successfully exported to {target_path}")
    else:
        print(f"Failed to compile {tex_file.name}. Error: {process.stderr}")

if __name__ == "__main__":
    tex_files = list(PAPERS_DIR.glob("**/*.tex"))
    for tex_file in tex_files:
        try:
            # Note: This requires pdflatex in system PATH
            compile_paper(tex_file)
        except Exception as e:
            print(f"Error processing {tex_file.name}: {e}")
