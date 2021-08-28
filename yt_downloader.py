from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"Author: {yt.author}")
print(f"Length: {yt.length}")

ys = yt.streams.get_highest_resolution()

print("Downloading....")
ys.download()
print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')