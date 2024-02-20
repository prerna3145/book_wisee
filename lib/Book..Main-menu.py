import Book_details
import Book_user
import Book_issue
def Book():
    while True:
        print("*"*75)
        print("BOOK MENU")
        print("*"*50)
        print("1. Adding More Books")
        print("2. Removing Books")
        print("3. Updating A Book")
        print("4. Display Books")
        print("5. Search Book")
        print("6. Returning To Main Menu")
        Choice=int(input("*******Enter Your Choice*******"))
        print("-"*25)
        if Choice==1:
            Book_details.add_book()
        elif Choice==2:
            Book_details.delete_book()
        elif Choice==3:
            Book_details.update_book()
        elif Choice==4:
            Book_details.display_books()
        elif Choice==5:
            Book_details.Search_book()
        elif Choice==6:
            break
        else:
            print("Press Any Key To Continue To Main Menu")
            Key=input("Enter Any Key")
def User():
    while True:
        print("*"*75)
        print("USER DETAILS")
        print("*"*50)
        print("1. Add User")
        print("2. Display Details")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Returning To Main Menu")
        Choice=int(input("*******Enter Your Choice*******"))
        print("-"*25)
        if Choice==1:
            Book_user.adduser()
        elif Choice==2:
            Book_user.display()
        elif Choice==3:
            Book_user.search()
        elif Choice==4:
            Book_user.update()
        elif Choice==5:
            Book_user.delete()
        elif Choice==6:
            break
        else:
            print("Press Any Key To Continue To Main Menu")
            C=input("Enter A Key")
def Issue():
    while True:
        print("*"*75)
        print("............ISSUE BOOK............")
        print("*"*50)
        print("1. Issue Book")
        print("2. Search person detail")
        print("3. return books")
        print("4. update books")
        print("5. Return to Main Menu")
        print("*"*55)
        C=int(input("Enter Your Choice"))
        print("-"*30)
        if C==1:
            Book_issue.issue()
        elif C==2:
            Book_issue.search()
        elif C==3:
            Book_issue.returnbook()
        elif C==4:
            Book_issue.Updatebook()
        elif C==5:
            break
        else:
            print("Press Any Key To Continue And Back To Menu")
            C=input("Enter A Key")

while True:
    print("***************____Menu Drive____**************")
    print("="*25)
    print("1. Book Details Menu Drive")
    print("2. Book User Menu Drive")
    print("3. Book Issue And Depositing:")
    print("4. Exit")
    print("*"*50)
    C=int(input("Enter Your Choice:"))
    if C==1:
        Book()
    elif C==2:
        User()
    elif C==3:
        Issue()
    elif C==4:
        break
    else:
        print("Press Any Key To Continue And Back To Menu")
        C=input("Enter A Key")
    
        
