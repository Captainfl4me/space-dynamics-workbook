python .\Scripts\add_temp_toc.py .\WE8.ipynb
nbmerge .\temp\WE8.ipynb .\WE9.ipynb .\WE10.ipynb > .\WE8-10.ipynb
jupyter nbconvert --clear-output --inplace .\WE8-10.ipynb
jupyter nbconvert --execute --to pdf .\WE8-10.ipynb --LatexPreprocessor.title="Workbook 2 Hand-in" --LatexPreprocessor.author_names="Nicolas THIERRY"
rm WE8-10.ipynb
rm .\temp -r -force