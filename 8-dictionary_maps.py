#!/usr/bin/python3

# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python3
# Create an empty phone book (dictionary)
phone_book = {}
n = int(input())

for _ in range(n):
  name,number = input().split()
  phone_book[name]=number
  
while True:
  try:
    query = input().strip()
    if query in phone_book:
      print(f"{query}={phone_book[query]}")
    else:
      print("Not found")
  except EOFError:
    break
