nbmerge .\WE1.ipynb .\WE2.ipynb .\WE3.ipynb .\WE4.ipynb .\WE5.ipynb .\WE6.ipynb .\WE7.ipynb > WE1-7.ipynb
jupyter nbconvert --clear-output --inplace WE1-7.ipynb
jupyter nbconvert --execute --to pdf WE1-7.ipynb --LatexPreprocessor.title="Workbook 1 Hand-in" --LatexPreprocessor.author_names="Nicolas THIERRY"