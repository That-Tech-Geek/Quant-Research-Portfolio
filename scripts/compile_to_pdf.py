import os
import subprocess
import shutil
from pathlib import Path

def find_latex_binary(binary_name="pdflatex"):
    """Attempts to find the LaTeX binary in common paths if not in PATH."""
    # Check if it's already in PATH
    if shutil.which(binary_name):
        return binary_name
    
    # Common Windows paths for MiKTeX and TeX Live
    common_paths = [
        r"C:\Program Files\MiKTeX\miktex\bin\x64",
        r"C:\Program Files\MiKTeX\miktex\bin",
        r"C:\texlive\2024\bin\windows",
        r"C:\texlive\2023\bin\windows",
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64"),
    ]
    
    for path in common_paths:
        binary_path = os.path.join(path, f"{binary_name}.exe")
        if os.path.exists(binary_path):
            return binary_path
            
    return None

def compile_latex_to_pdf(papers_dir, output_dir):
    papers_path = Path(papers_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    pdflatex_bin = find_latex_binary("pdflatex")
    bibtex_bin = find_latex_binary("bibtex")
    
    if not pdflatex_bin:
        print("Error: pdflatex not found. Please install MiKTeX or TeX Live and add it to your PATH.")
        return

    print(f"Using pdflatex at: {pdflatex_bin}")
    
    for paper_folder in papers_path.iterdir():
        if paper_folder.is_dir():
            tex_files = list(paper_folder.glob("*.tex"))
            if not tex_files:
                continue
                
            tex_file = tex_files[0]
            print(f"\n--- Compiling: {tex_file.name} ---")
            
            # Change to the paper directory for compilation
            original_cwd = os.getcwd()
            os.chdir(paper_folder)
            
            try:
                # 1. First pdflatex pass
                print("Pass 1: Generating aux files...")
                subprocess.run([pdflatex_bin, "-interaction=nonstopmode", tex_file.name], check=False, capture_output=True)
                
                # 2. Bibtex pass (if .bib exists)
                if (paper_folder / "references.bib").exists() and bibtex_bin:
                    print("Running BibTeX...")
                    subprocess.run([bibtex_bin, tex_file.stem], check=False, capture_output=True)
                    
                # 3. Second pdflatex pass (to resolve citations)
                print("Pass 2: Resolving references...")
                subprocess.run([pdflatex_bin, "-interaction=nonstopmode", tex_file.name], check=False, capture_output=True)
                
                # 4. Third pdflatex pass (to finalize layout)
                print("Pass 3: Finalizing PDF...")
                subprocess.run([pdflatex_bin, "-interaction=nonstopmode", tex_file.name], check=False, capture_output=True)
                
                # Move resulting PDF to output_dir
                pdf_file = paper_folder / f"{tex_file.stem}.pdf"
                if pdf_file.exists():
                    target_pdf = output_path / f"{tex_file.stem}.pdf"
                    shutil.copy(pdf_file, target_pdf)
                    print(f"Success: {target_pdf.name} exported.")
                else:
                    print(f"Failed: PDF was not generated for {tex_file.name}.")
                    
                # Cleanup aux files
                for ext in [".aux", ".log", ".out", ".bib", ".blg", ".bbl", ".pdf"]:
                    aux_file = paper_folder / f"{tex_file.stem}{ext}"
                    # Don't delete original references.bib if it's the source
                    if ext == ".bib" and (paper_folder / "references.bib").exists():
                        continue
                    if aux_file.exists():
                        os.remove(aux_file)
                        
            except Exception as e:
                print(f"Exception during compilation of {tex_file.name}: {e}")
            finally:
                os.chdir(original_cwd)

if __name__ == "__main__":
    SOURCE_DIR = r"D:\Quant_Research_Library\papers"
    TARGET_DIR = r"D:\Quant_Research_Library\final-papers"
    compile_latex_to_pdf(SOURCE_DIR, TARGET_DIR)