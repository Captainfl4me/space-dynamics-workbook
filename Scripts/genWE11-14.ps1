python .\Scripts\add_temp_toc.py .\WE11.ipynb
nbmerge .\temp\WE11.ipynb .\WE12.ipynb .\WE13.ipynb .\WE14.ipynb > .\WE11-14.ipynb
jupyter nbconvert --clear-output --inplace .\WE11-14.ipynb
jupyter nbconvert --execute --to pdf .\WE11-14.ipynb --LatexPreprocessor.title="Workbook 3 Hand-in" --LatexPreprocessor.author_names="Nicolas THIERRY"
rm WE11-14.ipynb
rm .\temp -r -force