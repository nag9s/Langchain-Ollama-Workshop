conda env list
conda create -n ml python=3.12.4 -y
    conda activate ml
    conda deactivate ml
# to disable base environment    
by default base environment will be activated.
to activate ml by default

(base) labuser@ip-172-31-4-210:~/Langchain-and-Ollama$ conda config --set auto_activate_base false

# activate ml environment
conda activate ml
pip install -r requirements.txt 

# misc
pip cache purge


# Optional Setup Git 
git config --global user.name myusername
git config --global user.email myemail