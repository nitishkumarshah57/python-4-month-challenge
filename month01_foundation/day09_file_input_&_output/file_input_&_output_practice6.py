# Day 09: file input and output in python
# Topic Recursion (dunction calling themselves) and file append("a") mode.

with open("wizard_archive.txt","w") as file:
    file.write("--- spell log ---\n")
    def archive_spell(power):
        with open("wizard_archive.txt","a") as file :
         if power <= 0:
            file.write("spell unleashed !\n")
            return
         else:
            file.write(f"Gathering power: {power}\n")
            archive_spell(power-1)
archive_spell(5) 
print("check your archive file !")           