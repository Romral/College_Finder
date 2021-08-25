from tkinter import *
from tkinter import messagebox
import requests

class NewsApp:
    def __init__(self,app):
        self.app = app
        self.app.title("News App")
        self.app.geometry("1470x600")
        #Variables
        self.NewsCatButton = []
        self.newsCat = ['General', 'Entertainment', 'Business', 'Sports', 'Health', 'Science', 'Technology']
        #GUI
        dark_blue = '#081054'
        light_blue = '#0066CC' 
        font_color = 'white'
        self.title = Label(self.app, text="News App", font=('rockwell bold',30), bg=dark_blue, fg=font_color, relief=GROOVE, pady=4, bd=12).pack(fill=X)
        #title is the heading of the content
        F1 = LabelFrame(self.app, text="Category", bg=dark_blue, fg=font_color, font=('roboto slab',20,'bold'), relief=GROOVE, bd=10)
        F1.place(x=0, y=80, width=300, relheight=0.88)

        for i in range(len(self.newsCat)):
            b = Button(F1, text=self.newsCat[i].upper(), font=('roboto slab',14,'bold'), bd=7, width=20, height=2, bg=light_blue, fg=font_color)
            b.grid(row=i, column=0, padx=10, pady=2)
            b.bind('<Button-1>',self.NewsArea)
            self.NewsCatButton.append(b) #stores info for each button

        F2 = Frame(self.app, relief=GROOVE, bd=7)
        F2.place(x=320, y=80, relwidth=0.75, relheight=0.88)
        newsTitle = Label(F2, text="News Area", bg=light_blue, fg=font_color, bd=7, relief=GROOVE, font=('roboto slab',20,'bold')).pack(fill=X)
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.textarea = Text(F2, yscrollcommand=scroll_y.set,font=('Lora bold',10), bg=dark_blue, fg=font_color, height=34 )
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.insert(END,"\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\n\n\t\t\t PLEASE SELECT ANY CATEGORY TO SHOW HEADLINES FOR THAT PARTICULAR CATEGORY \n\t\t\t\t PLEASE BE PATIENT THERE MAY BE A DELAY DUE TO NETWORK ISSUES")
        self.textarea.pack(fill=X)

    def NewsArea(self, event): #event->button clicking
        type = 'general'
        type = event.widget.cget('text').lower()
        apiKey = 'ae1ca158c3cb4ef4b78d1c1f96952c0e'
        news_url = f'https://newsapi.org/v2/top-headlines?country=in&category={type}&apiKey={apiKey}'
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\n Read the latest News provided by our App\n\n")
        self.textarea.insert(END,"----------------------------------------------------------------\n\n")
        try:
            articles = (requests.get(news_url).json())['articles']
            if (articles != 0):
                for i in range(len(articles)):
                    self.textarea.insert(END, f"{articles[i]['title']}\n")
                    self.textarea.insert(END, f"{articles[i]['description']}\n\n")
                    self.textarea.insert(END, f"{articles[i]['content']}\n\n")
                    self.textarea.insert(END, f"read more...{articles[i]['url']}\n")
                    self.textarea.insert(END, "\n--------------------------------------------------------------\n")
                    self.textarea.insert(END, "--------------------------------------------------------------\n\n")
            else:
                self.textarea.insert(END,"Sorry.. No News Available")
        except Exception as e:
            messagebox.showerror('ERROR', "Sorry, unable to connect to the Internet or some issue with the App")                

app = Tk() #instance of tkinter frame, helps to display the root window and manages all the other components of the tkinter application
NewsApp(app)
app.state("zoomed") #displays in full screen ignoring the geometry

pic = PhotoImage(file = 'newsIcon.png')
app.iconphoto(False, pic)
app.mainloop()