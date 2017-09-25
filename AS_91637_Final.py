"""Chuan Law 22/05/15
AS 91637 Internal
Purchase Program
Version 1 - Create Customer_info class and frame 1 widgets 
Version 2 - Create parent frame and widgets
Verdion 3 - Create frame 2 (display) and widgets
Version 4 - Create frame 3 (summary) and widgets
Version 5 -  Implement code to make the Enter data button add purchase info
to the empty lists and display in summary frame.
Version 6 - Add in code to calculate purchase amount and add it to the 
summary scrolledtext
Version 7 - Add in code for total sales and add it to frame 3 (summary)
Version 8 - Implement Next and Previous Buttons to loop through each customer
and their purchases on the list and display their name and purchases.
Version 9 - Improve GUI appearance
Version 10 - To test for boundary inputs
Version 11 - To test for invalid/unexpected inputs
"""

from tkinter import*
import tkinter.scrolledtext as tkst

#define price of purchases
cap = 12.5
tshirt = 25
badge = 9

#create empty master list to hold both payment lists
master_list = []

class Customer_Info():
    """Create customer class"""
    def __init__(self, name, cellphone, purchase_amount):
        self.Name = name 
        self.Cellphone = cellphone
        self.Purchase_amount = purchase_amount

class Purchase_Info(Frame):
    """Create frame 1 and widgets"""
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.grid()  
        self.cash_list = [] #create empty cash list
        self.credit_list = [] #create empty credit list        

        #Create index variable
        self.index = 0
        
        #Collect Data | FRAME 1
        self.collect_data_frame = Frame(self, bg = "pale green")
        self.collect_data_frame.grid(row = 2, column = 0, columnspan =6)
        
        #Labels in Frame 1
        #name label
        name_label = Label(self.collect_data_frame, text = "Name: ", bg = "pale green")
        name_label.grid(row = 0, column = 0, sticky = W) 
        #textbox1 for name 
        self.name_TextBox = Entry(self.collect_data_frame)
        self.name_TextBox.grid(row = 0, column = 2, sticky = E)  

        #cellphone label
        cellphone_label = Label(self.collect_data_frame, text = "Cellphone: ", bg = "pale green")
        cellphone_label.grid(row = 1, column = 0, sticky = W) 
        #textbox1 for cellphone 
        self.cellphone_TextBox = Entry(self.collect_data_frame)
        self.cellphone_TextBox.grid(row = 1, column = 2, sticky = E)  

        #purchase label for purchase checkboxes
        purchase_label = Label(self.collect_data_frame, text = "Please tick the items to purchase ", bg = "pale green")
        purchase_label.grid(row = 2, column = 1, sticky = W) 

        #checkbuttons for purchase selections
        #cap checkbutton
        self.cap_var = IntVar()
        self.cap_purchase = Checkbutton(self.collect_data_frame, width = 10, text = "Cap $12.50", variable = self.cap_var, bg = "pale green")        
        self.cap_purchase.grid(row = 4, column = 0, sticky = S)
        #tshirt checkbutton
        self.tshirt_var = IntVar()
        self.tshirt_purchase = Checkbutton(self.collect_data_frame, width = 10, text = "T-Shirt $25", variable = self.tshirt_var, bg = "pale green") 
        self.tshirt_purchase.grid(row = 4, column = 1, sticky = S)   
        #badge checkbutton
        self.badge_var = IntVar()
        self.badge_purchase = Checkbutton(self.collect_data_frame, width = 10, text = "Badge $9.00", variable = self.badge_var, bg = "pale green")
        self.badge_purchase.grid(row = 4, column = 2, sticky = S)       

        #payment method label
        payment_label = Label(self.collect_data_frame, text = "Please indicate method of payment", bg = "pale green")
        payment_label.grid(row = 5, column = 1, sticky = W)  

        #radiobuttons for payment methods
        #to initialise the radiobutton to Cash on startup
        self.r = StringVar()
        self.r.set("1")        
        #cash_radiobutton
        cash_radiobutton = Radiobutton(self.collect_data_frame, variable = self.r, value ="1", text = "Cash", bg = "pale green")
        cash_radiobutton.grid(row = 6, column = 0, sticky = W)
        #credit_radiobutton
        credit_radiobutton = Radiobutton(self.collect_data_frame, variable = self.r, value ="2", text = "Credit Card", bg = "pale green")
        credit_radiobutton.grid(row = 6, column = 1, sticky = W)    

        #create button to enter data
        Enter_Data_Button = Button(self.collect_data_frame, text = "Enter Data", command = self.Enter_Data, bg = "medium spring green")
        Enter_Data_Button.grid(row = 6, column = 2, sticky = E)        

        #PARENT FRAME
        #Label for frame name
        self.frame_heading = Label(self, text = "Collecting Person Data", bg = "white", font = ("Times", "20", "bold"))
        self.frame_heading.grid(row = 0, column = 1, columnspan = 3)  

        #create buttons to change to display frame
        #show all button     
        self.show_all_button = Button(self, text = "Show All", command = self.change_to_display, bg = "medium spring green")
        self.show_all_button.grid(row = 1, column = 1, sticky = W) 

        #add new person button
        self.new_person_button = Button(self, text = "Add New Person", command = self.change_to_collectdata, bg = "medium spring green")
        self.new_person_button.grid(row = 1, column = 2, sticky = W)        

        #label for search bar
        search_label = Label(self, text = "Search for names of those paying by: ", bg = "white")
        search_label.grid(row = 3, column = 1, sticky = W)

        #radiobuttons for payment method search
        #to initialise the radiobutton to Not Defines on startup
        self.v = StringVar()
        self.v.set(" ")         
        #parent cash radiobutton
        p_cash_radiobutton = Radiobutton(self, variable = self.v, value ="1", text = "Cash", command = self.change_to_summary, bg = "white")
        p_cash_radiobutton.grid(row = 4, column = 0, columnspan = 2, sticky = S)
        #parent credit radiobutton
        p_credit_radiobutton = Radiobutton(self, variable = self.v, value ="2", text = "Credit Card", command = self.change_to_summary, bg = "white")
        p_credit_radiobutton.grid(row = 4, column = 1, columnspan = 3, sticky = S)  

        #to import logo and grid it
        #imports selected photo located in the same folder
        self.comp_logo_image = PhotoImage(file = "Logo.gif")
        #changes image file into label
        self.comp_logo_Label = Label(self, image = self.comp_logo_image)
        #it is no able to be gridded
        self.comp_logo_Label.grid(row = 0, column = 0, rowspan = 2, sticky = W)     
        
        #To hide Add new person button on startup
        self.new_person_button.grid_forget()        

        #Display Data | FRAME 2
        self.display_data_frame = Frame(self, bg = "pale green")
        #create labels in display data frame
        self.display_label = Label(self.display_data_frame, text = "(No customer purchases available) ", bg = "pale green", font = ("Arial", "12"))
        self.display_label.grid(row = 0, column = 0, columnspan = 2, sticky = W)          
        #create previous and next buttons
        #previous_button
        previous_button = Button(self.display_data_frame, text = "Previous", command = self.Move_Previous, bg = "medium spring green")
        previous_button.grid(row = 1, column = 0, sticky = S)
        #next_button
        next_button = Button(self.display_data_frame, text = "Next", command = self.Move_Next, bg = "medium spring green")
        next_button.grid(row = 1, column = 1, sticky = S)  

        #Summary Info | FRAME 3
        self.summary_frame = Frame(self, bg = "pale green")
        #create labels in frame 3
        self.summary_label = Label(self.summary_frame, text = "Names of those paying by Cash or Credit", bg = "pale green")
        self.summary_label.grid(row = 0, column = 0, sticky = W)
        #summary_heading_label for the scrolledtext
        self.summary_heading = Label(self.summary_frame, text = "Name" + "\t\t\t" + "Cellphone" + "\t" + "Amount $", bg = "pale green")
        self.summary_heading.grid(row = 1, column = 0, sticky = W)
        #scrollbar widget
        self.payment_scrolledText = tkst.ScrolledText(self.summary_frame, width = 40, height =9, bg = "pale green")
        self.payment_scrolledText.grid(row = 2, column = 0)   
        #label for total sales of payment
        self.total_sales_label = Label(self.summary_frame, text = "Total Sales by payment", bg = "pale green")
        self.total_sales_label.grid(row = 3, column = 0, sticky = W)
        #label for sales total calculation
        self.calc_sales_label = Label(self.summary_frame, text = " ", bg = "pale green")
        self.calc_sales_label.grid(row = 3, column = 1, sticky = W)        

    def change_to_collectdata(self):
        """Function to switch frame 1 to frame 2"""
        self.display_data_frame.grid_forget()
        self.summary_frame.grid_forget()
        self.collect_data_frame.grid(row = 2, column = 0, columnspan = 6)
        self.frame_heading.configure(text = "Collecting Person Data")
        master_list = [] #clears elements in master list to prevent duplication
    
        #To grid Add show all button 
        self.show_all_button.grid(row = 1, column = 1, sticky = W)
        #To hide Add new person button 
        self.new_person_button.grid_forget()        
    
        #to initialise payment radiobuttons correctly
        self.v.set("0")
        self.r.set("1")          
    
    def change_to_display(self):
        """Function to switch frame 2 back to frame 1"""
        self.collect_data_frame.grid_forget() #forgets current frame user may be on
        self.summary_frame.grid_forget()
        self.display_data_frame.grid(row = 2, column = 0, columnspan = 6) #grids Display Info Frame
        self.frame_heading.configure(text = "Displaying Person Data")
        #To grid Add new person button 
        self.new_person_button.grid(row = 1, column = 2, sticky = W)
        #To hide Add show all button 
        self.show_all_button.grid_forget()       

        #adds customer info from both payment lists into master list
        master_list.extend(self.cash_list)  
        master_list.extend(self.credit_list)      
        self.display_label.configure(text = self.customer_display())

        #to initialise payment radiobuttons correctly
        self.v.set("0")
        self.r.set("1")          

    def change_to_summary(self):
        """Function to switch from either frame 1 or frame 2 to frame 3"""
        #to enable textbox
        self.payment_scrolledText.configure(state = 'normal')        
        self.collect_data_frame.grid_forget()
        self.display_data_frame.grid_forget()
        self.summary_frame.grid(row = 2, column = 0, columnspan = 6)
        self.frame_heading.configure(text = "Summary of Sales")

        #To grid Add new person button 
        self.new_person_button.grid(row = 1, column = 2, sticky = W)  
        #To grid show all person button 
        self.show_all_button.grid(row = 1, column = 1, sticky = W)    

        #initializes the calculations
        self.cash_total = 0
        self.credit_total = 0

        #creates empty summary variables
        self.summary_cash = " "
        self.summary_credit = " "        

        var = self.v.get() #pulls self.r and sets it to var
        if var == "1":
            #to change name of list to cash payments
            self.summary_label.configure(text = "Names of those paying by Cash: ")
            #to display total sales calculation
            self.total_sales_label.configure(text = "Total Sales by Cash: ")
            for i in self.cash_list: #iterates through cash list
                self.summary_cash += i.Name #adds name
                self.summary_cash += "\t\t"
                self.summary_cash += i.Cellphone #adds cellphone
                self.summary_cash += "\t\t"
                purchase_amount = str(i.Purchase_amount) #changes purcahse amount to string
                self.summary_cash += purchase_amount #adds purchase amount as a string
                self.summary_cash += "\n"
                self.cash_total += i.Purchase_amount #adds up all customers total purchases
            self.cash_total = str(self.cash_total) #changes cash total into a string
            self.calc_sales_label.configure( text = "$ "+ self.cash_total) #replaces the label with the calculated cash total             

            #clears the information on the scrolledtext
            self.payment_scrolledText.delete(0.0, END)         
            #adds summary cash list into the scrolledtext
            self.payment_scrolledText.insert(0.0, self.summary_cash)

        elif var == "2": 
            #to change name of list to cash payments
            self.summary_label.configure(text = "Names of those paying by Credit: ")
            #to display total sales calculation
            self.total_sales_label.configure(text = "Total Sales by Credit: ")

            for i in self.credit_list: #iterates through credit list
                self.summary_credit += i.Name #adds name
                self.summary_credit += "\t\t"
                self.summary_credit += i.Cellphone #adds cellphone
                self.summary_credit += "\t\t"
                purchase_amount = str(i.Purchase_amount) #changes purcahse amount to string
                self.summary_credit += purchase_amount #adds purchase amount as a string
                self.summary_credit += "\n"
                self.credit_total += i.Purchase_amount #adds up all customers total purchases
            self.credit_total = str(self.credit_total) #changes credit total into a string
            self.calc_sales_label.configure( text = "$ "+ self.credit_total) #replaces the label with the calculated credit total

            #clears the information on the scrolledtext
            self.payment_scrolledText.delete(0.0, END)
            #adds summary credit list into the scrolledtext
            self.payment_scrolledText.insert(0.0, self.summary_credit)  
            
        #to disable scrolled text editing
        self.payment_scrolledText.configure(state = 'disabled')
            
    def Enter_Data(self):
        """Function to add purchase info of customers into payment lists"""
        #calculations are initialized
        purchase_amount = 0

        #to get amount of purchases by user
        var1 = self.cap_var.get() #gets variables of each checkbutton
        var2 = self.tshirt_var.get()
        var3 = self.badge_var.get()

        #checks to see which checkbuttons are selected
        if (var1 == 1): 
            #if cap checkbox is checked, customer amount is set to $12.5
            purchase_amount = cap
        if (var2 == 1):
            #if tshirt checkbox is checked, add $25 to customer amount
            purchase_amount = purchase_amount + tshirt
        if (var3 == 1):
            #if badge checkbox is checked, add $9 to customer amount
            purchase_amount = purchase_amount + badge            

        name = self.name_TextBox.get() #gets name textbox input
        cellphone = self.cellphone_TextBox.get() #gets cellphone textbox input

        var = self.r.get() #sets var to self.r
        if var == "1": #if user has selected cash payment option, purchase info is added to cash list
            #Boundary Tests
            if len(name) > 30: #checks if name is longer than 30 characters
                self.name_TextBox.delete(0, END) #if yes, clears what was entered
                self.name_TextBox.insert(INSERT, "*Name too long*")#to tell user that the input is out of bounds
                if len(cellphone) < 9 or len(cellphone) > 11: #checks if the cellphone length is less than 9 or longer than 11
                        self.cellphone_TextBox.delete(0, END) #if yes, clears what was entered
                        self.cellphone_TextBox.insert(INSERT, "*# Too long/ short*") #to tell user that the input is out of bounds                  
            elif len(cellphone) < 9 or len(cellphone) > 11:
                self.cellphone_TextBox.delete(0, END)
                self.cellphone_TextBox.insert(INSERT, "# Too long/ short") #to tell user that the input being out of bounds
            else: #if input is within the boundaries
                self.cash_list.append(Customer_Info(name, cellphone, purchase_amount)) #add customer info to cash list
                self.name_TextBox.delete(0, END) #clear textboxes for new inputs
                self.cellphone_TextBox.delete(0, END) 
             
            #to reset radiobuttons
            self.v.set("0")
            self.r.set("1")
          
        if var == "2": #if user has selected credit payment option, purchase info is added to credit list
            #Boundary Tests
            if len(name) > 30: #checks if name is longer than 30 characters
                self.name_TextBox.delete(0, END) #if yes, clears what was entered
                self.name_TextBox.insert(INSERT, "*Name too long*")#to tell user that the input is out of bounds
                if len(cellphone) < 9 or len(cellphone) > 11: #checks if the cellphone length is less than 9 or longer than 11
                    self.cellphone_TextBox.delete(0, END) #if yes, clears what was entered
                    self.cellphone_TextBox.insert(INSERT, "# Too long/ short") #to tell user that the input is out of bounds                  
            elif len(cellphone) < 9 or len(cellphone) > 11:
                self.cellphone_TextBox.delete(0, END)
                self.cellphone_TextBox.insert(INSERT, "# Too long/ short") #to tell user that the input being out of bounds
            else: #if input is within the boundaries
                self.credit_list.append(Customer_Info(name, cellphone, purchase_amount)) #add customer info to cash list
                self.name_TextBox.delete(0, END) #clear textboxes for new inputs
                self.cellphone_TextBox.delete(0, END) 
  
             #to reset radiobuttons
            self.v.set("0")
            self.r.set("1")

        #to deselect the checkbuttons
        self.cap_purchase.deselect()
        self.tshirt_purchase.deselect()
        self.badge_purchase.deselect()
        
    def customer_display(self):
        """Function to create label to show customer name and purchases"""
        #code to identify what purchases were selected
        purchase_selection = " " #creates empty string to add name and purcahse selections
        purchase_selection += master_list[self.index].Name + " is purchasing "
        item_selection = master_list[self.index].Purchase_amount #assigns customer purchase amount 

        if item_selection == 12.50: #checks if value for cap
            purchase_selection += "a Cap." #adds selection to string label
        elif item_selection == 25: #checks if value for tshirt
            purchase_selection += "a T-Shirt."
        elif item_selection == 9:  #checks if value for badge
            purchase_selection += "a Badge." 
        elif item_selection == 37.5:  #checks if value for cap, tshirt
            purchase_selection += "a Cap and a T-Shirt."   
        elif item_selection == 21.5: #checks if value for cap, badge
            purchase_selection += "a Cap and a Badge."  
        elif item_selection == 34: #checks if value for tshirt, badge
            purchase_selection += "a T-Shirt and a Badge."  
        elif item_selection == 46.5:#checks if value for all purchases
            purchase_selection += "a Cap, a T-Shirt and a Badge." 
        #once purchase selection for customer has been identified, configure label in frame 2
        self.display_label.configure(text = purchase_selection)
            
    def Move_Next(self):
        """Function to move forward through the list of customers """  
        if (self.index != len(master_list) - 1 ):
            self.index = self.index + 1 #changes index variable to move forwards
        else:
            self.index = 0
        self.customer_display() #calls customer_display method after moving
        
    def Move_Previous(self):
        """Function to move backwards through the list of customers """ 
        if (self.index == 0): #checks if the index is 0
            self.index = len(master_list) -1 
        else:
            self.index -= 1 #changes index variable to move backwards
        self.customer_display() #calls customer_display method after moving
        
#main     
root = Tk()
root.title("Purchase_Info")
app = Purchase_Info(root)
root.mainloop()

#end source code