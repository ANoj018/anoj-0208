# 1. Indexing and Slicing
#    Given the string s = "PythonPractice", what are the outputs of:
#    - s[1]
#    - s[-3:]
#    - s[2:7]
s = "PythonPractice"
print(s[1])      
print(s[-3:])    
print(s[2:7])    

# 2. Reverse a String
#    Write a one-liner to reverse the string "developer" using slicing.
s = "developer"
print(s[::-1])  

# 3. Count Vowels
#    Write a function that counts the number of vowels in a given string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(count_vowels("developers"))  

# 4. Check for Palindrome
#    Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]
print(is_palindrome("A man a plan a canal Panama")) 

# 5. Clean and Format String
#    Given text = "   hello world! welcome to Python.   ", write code to:
#    - Remove leading/trailing spaces
#    - Capitalize each word
#    - Replace the word "Python" with "Programming"
text = "   hello world! welcome to Python.   "
text = text.strip()  
text = text.title()  
text = text.replace("Python", "Programming") 
print(text)

# 6. Find Longest Word
#    Write a function that takes a sentence and returns the longest word in it.
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
print(find_longest_word("The doggggy is cute")) 

# 7. String Operators
#    Given s1 = "Py" and s2 = "thon", what are the results of:
#    - s1 + s2
#    - s1 * 3
#    - "y" in s1
s1 = "Py"
s2 = "thon"
print(s1 + s2)  
print(s1 * 3)   
print("y" in s1)  


# 8. Remove Duplicate Characters
#    Write a function that removes all duplicate characters from a string but keeps the first occurrence.
def remove_duplicates(text):
    result = ""
    for char in text:
        if char not in result:
            result += char
    return result
print(remove_duplicates("programming"))

# 9. Check for Anagram
#    Write a function that returns True if two strings are anagrams of each other.
def are_anagrams(str1, str2):   
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "world"))   

# 10. Word Frequency Counter
#     Write a function that takes a sentence and returns a dictionary of word frequencies.

def word_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
print(word_frequency("Hello world hello"))

# take a secret word as inout (wihtoutspaces) then encode the word using a custom cipher: replace all vowels with * reverse the string then shift each letter 2 place ahead in the alphabet (wrap around if needed, eg, y-a,z-b) finally print the resulting encoded word

word = input("Enter a secret word (no spaces): ")

vowels = "aeiouAEIOU"
no_vowels = ""
for letter in word:
    if letter in vowels:
        no_vowels += '*'
    else:
        no_vowels += letter

reversed_word = no_vowels[::-1]

encoded = ""
for letter in reversed_word:
    if letter.isalpha():
        if letter.islower():
            shifted = chr((ord(letter) - ord('a') + 2) % 26 + ord('a'))
        else:
            shifted = chr((ord(letter) - ord('A') + 2) % 26 + ord('A'))
        encoded += shifted
    else:
        encoded += letter

print("Encoded word:", encoded)

# 1. Take a number from the user and print whether it's even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Write a program to count the number of vowels in a given string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# 3. Ask the user to input a sentence and print the number of words in it.
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

# 4. Take a number from the user and print its multiplication table from 1 to 10 using a function.
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

num = int(input("Enter a number: "))
table(num)

# 5. Write a program to accept 5 numbers from the user, store them in a list, and print the maximum and minimum values.
numbers = []
for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)
print("Max:", max(numbers))
print("Min:", min(numbers))

# 6. Accept a string and check whether it is a palindrome or not (same forward and backward).
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 7. Create a loop that keeps asking the user to guess a secret number between 1 to 10 until they guess it correctly. (Use while loop and break)
secret = 7
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("Correct!")
        break

# 8. Accept 5 numbers from the user and store only the even numbers in a new list. Print the final list.
even_numbers = []
for i in range(5):
    n = int(input("Enter number: "))
    if n % 2 == 0:
        even_numbers.append(n)
print("Even numbers:", even_numbers)

# 9. Write a program that prints the Fibonacci sequence up to n terms. (Ask user for n)
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b

# 10. Accept a list of numbers and remove all duplicate values
nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print("Unique list:", unique)

 