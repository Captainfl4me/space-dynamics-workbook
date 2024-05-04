python .\Scripts\add_temp_toc.py .\WE1.ipynb
nbmerge .\temp\WE1.ipynb .\WE2.ipynb .\WE3.ipynb .\WE4.ipynb .\WE5.ipynb .\WE6.ipynb .\WE7.ipynb .\WE8.ipynb .\WE9.ipynb .\WE10.ipynb .\WE11.ipynb .\WE12.ipynb .\WE13.ipynb .\WE14.ipynb > .\WEFULL.ipynb
jupyter nbconvert --clear-output --inplace .\WEFULL.ipynb
jupyter nbconvert --execute --to pdf .\WEFULL.ipynb --LatexPreprocessor.title="Space Dynamics Workbook" --LatexPreprocessor.author_names="Nicolas THIERRY"
rm WEFULL.ipynb
rm .\temp -r -force