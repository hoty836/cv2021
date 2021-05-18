text = """Life is too short
you need java"""
text = text.replace("java", "python")

f1 = open("test.txt", 'w')
f1.write(text)
f1.close()

