import pyperclip

text = input("Enter text to copy: ")

pyperclip.copy(text)

print("Text copied to clipboard!")

print("Clipboard contains:")
print(pyperclip.paste())
