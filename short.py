import pyshorteners
import pyperclip

def shorten_url():
    # Ask the user for the long URL
    long_url = input("Enter the URL to be shortened: ")
    
    try:
        # Use pyshorteners to shorten the URL
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        
        # Display the shortened URL
        print(f"Shortened URL: {short_url}")
        
        # Copy the shortened URL to the clipboard
        pyperclip.copy(short_url)
        print("The shortened URL has been copied to your clipboard!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    shorten_url()
