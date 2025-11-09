with open("demofile.txt", "a") as f:
  file.write(text +\n)
  f.write("running away")
#open and read the file after the appending:
with open("main.py") as f:
  print(f.read())



